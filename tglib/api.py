#!/bin/python3

REQ_DEBUG = 0
RESP_DEBUG = 0

__all__ = (
    'TelegramApi',
    'TelegramError',
)

from .logger import get_logger
logger = get_logger('TelegramApi')

import os
import re
import time
import asyncio
from typing import (Any,
                    Union,
                    Literal,
                    Optional,
                    Iterable)

from aiohttp import (
    FormData,
    ClientError,
    TCPConnector,
    ClientSession,
    ClientTimeout,
    ClientResponse
)
from .types import (
    TelegramType, # to serialize telegram objects
    InputFile,
    InputMedia,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo
)

try:
    import ssl
except ImportError:
    logger.info(
        "module 'ssl' not found, SSL_CONTEXT is None."
    )
    SSL_CONTEXT = None
else:
    try:
        import certifi
    except ImportError:
        logger.info(
            "module 'certifi' not found, using default CA."
        )
        SSL_CONTEXT = ssl.create_default_context()
    else:
        _cafile = certifi.where()
        if not os.path.isfile(_cafile):
            _cafile = None
            logger.info(
                "CA file not found, try to"
                " reinstall the module 'certifi'."
            )
        SSL_CONTEXT = ssl.create_default_context(
            cafile = _cafile
        )
        del _cafile

try:
    import ujson as json
except ImportError:
    import json
    logger.info(
        "module 'ujson' not found, the"
        " default 'json' was imported."
    )

def _serialize(
    val: Any,
    /,
    *,
    last: bool = True
) -> Union[Any, str, list, dict]:

    if isinstance(val, TelegramType):
        val = val.__dict__

    elif hasattr(val, '__dict__'):
        val = '{!r}'.format(val)

    if isinstance(val, (list, tuple, set)):
        res = [
            _serialize(x, last = False) for x in val
        ]
    elif isinstance(val, dict):
        res = {
            x: _serialize(val[x], last = False) for x in val if val[x] is not None
        }
    else:
        res = val

    if not last:
        return res
    else:
        return res if isinstance(res, str) else json.dumps(res, ensure_ascii = False)


def _format_url(token: str, method: str, /) -> str:
    return '/bot{}/{}'.format(token, method)


async def _parse_json(response: ClientResponse, /) -> Any:

    result = await response.json(loads = json.loads)

    if RESP_DEBUG:
        logger.debug(result)

    if result['ok'] is True:
        return result['result']
    else:
        raise TelegramError(
            {
                'error_code': result['error_code'],
                'description': result['description']
            }
        )


def _get_files(
    params: dict,
    /,
    *file_keys: str
) -> Optional[dict[str, dict[Literal['content', 'file_name'], Any]]]:

    files = {}
    for key in file_keys:
        if key in params:
            obj = params[key]
            if isinstance(obj, InputFile):
                try:
                    with open(obj.path, 'rb') as rb:
                        content = rb.read()
                except FileNotFoundError:
                    raise FileNotFoundError(
                        f"Inexistent file: {obj.path!r},"
                        ' check your InputFile object.'
                    )
                files[key] = {
                    'content': content,
                    'file_name': obj.file_name
                }
                del params[key]

    return files or None


def _convert_input_media(
    media: InputMedia,
    files: dict,
    types_check: tuple[type],
    /
) -> None:
    '''
    Used in _get_input_media_files() to check and add to files InputMedia objects.
    '''
    if not isinstance(media, types_check):
        available_types = ', '.join([t.__name__ for t in types_check])
        raise TypeError(
            f'Expected one of the following types:'
            f' {available_types}, got {media.__class__.__name__}.'
        )
    if isinstance(media.media, str):
        media_file = re.match(r'attach://(.*)', media.media)
        if media_file:
            path = media_file.group(1)
            try:
                with open(path, 'rb') as rb:
                    content = rb.read()
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Inexistent file: {path!r},"
                    ' check your InputMedia object;'
                    ' InputMedia.media must be in the'
                    ' format "attach://<file_name>" to'
                    ' post a file using multipart/form-data.'
                )
            files[path] = {
                'content': content,
                'file_name': path
            }


def _get_input_media_files(
    params: dict,
    /,
    *file_keys: str,
    types_check: type
) -> Optional[dict[str, dict[Literal['content', 'file_name'], Any]]]:

    assert hasattr(types_check, '__origin__') and types_check.__origin__ is Union
    types_check = types_check.__args__

    files = {}
    for key in file_keys:
        if key in params:
            obj = params[key]
            if isinstance(obj, Iterable):
                for t in obj:
                    _convert_input_media(t, files, types_check)
            else:
                _convert_input_media(obj, files, types_check)

    return files or None


def _prepare_data(
    params: Optional[dict],
    files: Optional[dict[str, dict[Literal['content', 'file_name'], Any]]],
    /
) -> Optional[FormData]:

    if params is None:
        return None

    data = FormData(params)

    if files is None:
        return data

    for key in files:

        content = files[key]['content']
        file_name = files[key]['file_name']

        data.add_field(
            key,
            content,
            filename = file_name
        )
    return data


class TelegramError(Exception):
    """
    Class to handle exceptions during Telegram requests.
    """


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0'
}
BASE_URL = 'https://api.telegram.org'
CLIENT_TIMEOUT = ClientTimeout(total = 300, connect = 3)


class TelegramApi:

    def __init__(
        self,
        token: str,
        proxy: Optional[str] = None,
        debug: Optional[bool] = None
    ):
        if not isinstance(token, str):
            raise TypeError(
                f"'token' must be str, got {token.__class__.__name__}."
            )
        if not isinstance(proxy, (str, type(None))):
            raise TypeError(
                f"'proxy' must be str or None, got {proxy.__class__.__name__}."
            )
        if debug:
            logger.setLevel(10)

        self._token = token
        self._session = None
        self._headers_and_proxy = {
            'proxy': proxy,
            'headers': HEADERS
        }
        logger.debug(self._headers_and_proxy)

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session

    def _get_session(self) -> ClientSession:

        if self.session is None or self.session.closed:
            self._session = ClientSession(
                base_url = BASE_URL,
                timeout = CLIENT_TIMEOUT,
                json_serialize = json.dumps,
                connector = TCPConnector(ssl = SSL_CONTEXT)
            )
            logger.debug('New session initialized.')

        return self.session


    async def _request(
        self,
        method: str,
        params: Optional[dict] = None,
        files: Optional[dict] = None,
        *,
        max_retries: int = 100,
        keep_session: Optional[bool] = None
    ):

        if params is not None:
            for key in params:
                params[key] = _serialize(params[key])

        if REQ_DEBUG:
            logger.debug(
                f'method: {method!r}, params: {params}, files: {files}'
            )

        current_try = 0

        while current_try < max_retries:

            current_try += 1
            self._get_session()
            start_time = time.time()
            try:
                # Convert the params to
                # a FormData instance at
                # each attempt, to prevent
                # a RuntimeError from aiohttp.
                data = _prepare_data(params, files)

                async with self.session.post(
                    url = _format_url(self._token, method),
                    data = data,
                    **self._headers_and_proxy
                ) as response:

                    result = await _parse_json(response)

                    if current_try != 1:
                        logger.info(
                            f'Request {method!r} succeeded'
                            f' after {current_try} retries.'
                        )
                    return result

            except (ClientError, TimeoutError) as exc:
                logger.info(
                    f'{exc.__class__.__name__} occurred in request'
                    f' {method!r}; current try: {current_try}/{max_retries}.'
                )
                await asyncio.sleep(3 - (time.time() - start_time))

            except BaseException as exc:
                exc = type(exc)(*[arg for arg in exc.args])
                # this because it causes too much traceback
                raise exc from None

            finally:
                if self.session.connector is not None:
                    if not (
                        keep_session
                        or self.session.connector._acquired
                    ):
                        await self.session.close()
                        logger.debug(
                            'Session closed because there'
                            ' are not connections in the pool.'
                        )
        else:
            raise TimeoutError(method)


###########################################################

    async def get_updates(self, params: dict, **kwargs):
        method = 'getUpdates'
        return await self._request(method, params, **kwargs)

    async def get_me(self):
        method = 'getMe'
        return await self._request(method)

    async def send_message(self, params: dict):
        method = 'sendMessage'
        return await self._request(method, params)

    async def log_out(self):
        method = 'logOut'
        return await self._request(method)

    async def close(self):
        method = 'close'
        return await self._request(method)

    async def forward_message(self, params: dict):
        method = 'forwardMessage'
        return await self._request(method, params)

    async def forward_messages(self, params: dict):
        method = 'forwardMessages'
        return await self._request(method, params)

    async def copy_message(self, params: dict):
        method = 'copyMessage'
        return await self._request(method, params)

    async def copy_messages(self, params: dict):
        method = 'copyMessages'
        return await self._request(method, params)

    async def send_photo(self, params: dict):
        method = 'sendPhoto'
        files = _get_files(params, 'photo')
        return await self._request(method, params, files)

    async def send_audio(self, params: dict):
        method = 'sendAudio'
        files = _get_files(params, 'audio', 'thumbnail')
        return await self._request(method, params, files)

    async def send_document(self, params: dict):
        method = 'sendDocument'
        files = _get_files(params, 'document', 'thumbnail')
        return await self._request(method, params, files)

    async def send_video(self, params: dict):
        method = 'sendVideo'
        files = _get_files(params, 'video', 'thumbnail')
        return await self._request(method, params, files)

    async def send_animation(self, params: dict):
        method = 'sendAnimation'
        files = _get_files(params, 'animation', 'thumbnail')
        return await self._request(method, params, files)

    async def send_voice(self, params: dict):
        method = 'sendVoice'
        files = _get_files(params, 'voice')
        return await self._request(method, params, files)

    async def send_video_note(self, params: dict):
        method = 'sendVideoNote'
        files = _get_files(params, 'video_note', 'thumbnail')
        return await self._request(method, params, files)

    async def send_media_group(self, params: dict):
        method = 'sendMediaGroup'
        files = _get_input_media_files(
            params,
            'media',
            types_check = Union[InputMediaPhoto, InputMediaAudio, InputMediaVideo, InputMediaDocument]
        )
        return await self._request(method, params, files)

    async def send_location(self, params: dict):
        method = 'sendLocation'
        return await self._request(method, params)

    async def send_venue(self, params: dict):
        method = 'sendVenue'
        return await self._request(method, params)

    async def send_contact(self, params: dict):
        method = 'sendContact'
        return await self._request(method, params)

    async def send_poll(self, params: dict):
        method = 'sendPoll'
        return await self._request(method, params)

    async def send_dice(self, params: dict):
        method = 'sendDice'
        return await self._request(method, params)

    async def send_chat_action(self, params: dict):
        method = 'sendChatAction'
        return await self._request(method, params)

    async def set_message_reaction(self, params: dict):
        method = 'setMessageReaction'
        return await self._request(method, params)

    async def get_user_profile_photos(self, params: dict):
        method = 'getUserProfilePhotos'
        return await self._request(method, params)

    async def get_file(self, params: dict):
        method = 'getFile'
        return await self._request(method, params)

    async def ban_chat_member(self, params: dict):
        method = 'banChatMember'
        return await self._request(method, params)

    async def unban_chat_member(self, params: dict):
        method = 'unbanChatMember'
        return await self._request(method, params)

    async def restrict_chat_member(self, params: dict):
        method = 'restrictChatMember'
        return await self._request(method, params)

    async def promote_chat_member(self, params: dict):
        method = 'promoteChatMember'
        return await self._request(method, params)

    async def set_chat_administrator_custom_title(self, params: dict):
        method = 'setChatAdministratorCustomTitle'
        return await self._request(method, params)

    async def ban_chat_sender_chat(self, params: dict):
        method = 'banChatSenderChat'
        return await self._request(method, params)

    async def unban_chat_sender_chat(self, params: dict):
        method = 'unbanChatSenderChat'
        return await self._request(method, params)

    async def set_chat_permissions(self, params: dict):
        method = 'setChatPermissions'
        return await self._request(method, params)

    async def export_chat_invite_link(self, params: dict):
        method = 'exportChatInviteLink'
        return await self._request(method, params)

    async def create_chat_invite_link(self, params: dict):
        method = 'createChatInviteLink'
        return await self._request(method, params)

    async def edit_chat_invite_link(self, params: dict):
        method = 'editChatInviteLink'
        return await self._request(method, params)

    async def revoke_chat_invite_link(self, params: dict):
        method = 'revokeChatInviteLink'
        return await self._request(method, params)

    async def approve_chat_join_request(self, params: dict):
        method = 'approveChatJoinRequest'
        return await self._request(method, params)

    async def decline_chat_join_request(self, params: dict):
        method = 'declineChatJoinRequest'
        return await self._request(method, params)

    async def set_chat_photo(self, params: dict):
        method = 'setChatPhoto'
        files = _get_files(params, 'photo')
        return await self._request(method, params, files)

    async def delete_chat_photo(self, params: dict):
        method = 'deleteChatPhoto'
        return await self._request(method, params)

    async def set_chat_title(self, params: dict):
        method = 'setChatTitle'
        return await self._request(method, params)

    async def set_chat_description(self, params: dict):
        method = 'setChatDescription'
        return await self._request(method, params)

    async def pin_chat_message(self, params: dict):
        method = 'pinChatMessage'
        return await self._request(method, params)

    async def unpin_chat_message(self, params: dict):
        method = 'unpinChatMessage'
        return await self._request(method, params)

    async def unpin_all_chat_messages(self, params: dict):
        method = 'unpinAllChatMessages'
        return await self._request(method, params)

    async def leave_chat(self, params: dict):
        method = 'leaveChat'
        return await self._request(method, params)

    async def get_chat(self, params: dict):
        method = 'getChat'
        return await self._request(method, params)

    async def get_chat_administrators(self, params: dict):
        method = 'getChatAdministrators'
        return await self._request(method, params)

    async def get_chat_member_count(self, params: dict):
        method = 'getChatMemberCount'
        return await self._request(method, params)

    async def get_chat_member(self, params: dict):
        method = 'getChatMember'
        return await self._request(method, params)

    async def set_chat_sticker_set(self, params: dict):
        method = 'setChatStickerSet'
        return await self._request(method, params)

    async def delete_chat_sticker_set(self, params: dict):
        method = 'deleteChatStickerSet'
        return await self._request(method, params)

    async def get_forum_topic_icon_stickers(self):
        method = 'getForumTopicIconStickers'
        return await self._request(method)

    async def create_forum_topic(self, params: dict):
        method = 'createForumTopic'
        return await self._request(method, params)

    async def edit_forum_topic(self, params: dict):
        method = 'editForumTopic'
        return await self._request(method, params)

    async def close_forum_topic(self, params: dict):
        method = 'closeForumTopic'
        return await self._request(method, params)

    async def reopen_forum_topic(self, params: dict):
        method = 'reopenForumTopic'
        return await self._request(method, params)

    async def delete_forum_topic(self, params: dict):
        method = 'deleteForumTopic'
        return await self._request(method, params)

    async def unpin_all_forum_topic_messages(self, params: dict):
        method = 'unpinAllForumTopicMessages'
        return await self._request(method, params)

    async def edit_general_forum_topic(self, params: dict):
        method = 'editGeneralForumTopic'
        return await self._request(method, params)

    async def close_general_forum_topic(self, params: dict):
        method = 'closeGeneralForumTopic'
        return await self._request(method, params)

    async def reopen_general_forum_topic(self, params: dict):
        method = 'reopenGeneralForumTopic'
        return await self._request(method, params)

    async def hide_general_forum_topic(self, params: dict):
        method = 'hideGeneralForumTopic'
        return await self._request(method, params)

    async def unhide_general_forum_topic(self, params: dict):
        method = 'unhideGeneralForumTopic'
        return await self._request(method, params)

    async def unpin_all_general_forum_topic_messages(self, params: dict):
        method = 'unpinAllGeneralForumTopicMessages'
        return await self._request(method, params)

    async def answer_callback_query(self, params: dict):
        method = 'answerCallbackQuery'
        return await self._request(method, params)

    async def get_user_chat_boosts(self, params: dict):
        method = 'getUserChatBoosts'
        return await self._request(method, params)

    async def set_my_commands(self, params: dict):
        method = 'setMyCommands'
        return await self._request(method, params)

    async def delete_my_commands(self, params: dict):
        method = 'deleteMyCommands'
        return await self._request(method, params)

    async def get_my_commands(self, params: dict):
        method = 'getMyCommands'
        return await self._request(method, params)

    async def set_my_name(self, params: dict):
        method = 'setMyName'
        return await self._request(method, params)

    async def get_my_name(self, params: dict):
        method = 'getMyName'
        return await self._request(method, params)

    async def set_my_description(self, params: dict):
        method = 'setMyDescription'
        return await self._request(method, params)

    async def get_my_description(self, params: dict):
        method = 'getMyDescription'
        return await self._request(method, params)

    async def set_my_short_description(self, params: dict):
        method = 'setMyShortDescription'
        return await self._request(method, params)

    async def get_my_short_description(self, params: dict):
        method = 'getMyShortDescription'
        return await self._request(method, params)

    async def set_chat_menu_button(self, params: dict):
        method = 'setChatMenuButton'
        return await self._request(method, params)

    async def get_chat_menu_button(self, params: dict):
        method = 'getChatMenuButton'
        return await self._request(method, params)

    async def set_my_default_administrator_rights(self, params: dict):
        method = 'setMyDefaultAdministratorRights'
        return await self._request(method, params)

    async def get_my_default_administrator_rights(self, params: dict):
        method = 'getMyDefaultAdministratorRights'
        return await self._request(method, params)

    async def edit_message_text(self, params: dict):
        method = 'editMessageText'
        return await self._request(method, params)

    async def edit_message_caption(self, params: dict):
        method = 'editMessageCaption'
        return await self._request(method, params)

    async def edit_message_media(self, params: dict):
        method = 'editMessageMedia'
        files = _get_input_media_files(params, 'media', types_check = InputMedia)
        return await self._request(method, params, files)

    async def edit_message_live_location(self, params: dict):
        method = 'editMessageLiveLocation'
        return await self._request(method, params)

    async def stop_message_live_location(self, params: dict):
        method = 'stopMessageLiveLocation'
        return await self._request(method, params)

    async def edit_message_reply_markup(self, params: dict):
        method = 'editMessageReplyMarkup'
        return await self._request(method, params)

    async def stop_poll(self, params: dict):
        method = 'stopPoll'
        return await self._request(method, params)

    async def delete_message(self, params: dict):
        method = 'deleteMessage'
        return await self._request(method, params)

    async def delete_messages(self, params: dict):
        method = 'deleteMessages'
        return await self._request(method, params)

    async def send_sticker(self, params: dict):
        method = 'sendSticker'
        files = _get_files(params, 'sticker')
        return await self._request(method, params, files)

    async def get_sticker_set(self, params: dict):
        method = 'getStickerSet'
        return await self._request(method, params)

    async def get_custom_emoji_stickers(self, params: dict):
        method = 'getCustomEmojiStickers'
        return await self._request(method, params)

    async def upload_sticker_file(self, params: dict):
        method = 'uploadStickerFile'
        files = _get_files(params, 'sticker')
        return await self._request(method, params, files)

    async def create_new_sticker_set(self, params: dict):
        method = 'createNewStickerSet'
        return await self._request(method, params)

    async def add_sticker_to_set(self, params: dict):
        method = 'addStickerToSet'
        return await self._request(method, params)

    async def set_sticker_position_in_set(self, params: dict):
        method = 'setStickerPositionInSet'
        return await self._request(method, params)

    async def delete_sticker_from_set(self, params: dict):
        method = 'deleteStickerFromSet'
        return await self._request(method, params)

    async def set_sticker_emoji_list(self, params: dict):
        method = 'setStickerEmojiList'
        return await self._request(method, params)

    async def set_sticker_keywords(self, params: dict):
        method = 'setStickerKeywords'
        return await self._request(method, params)

    async def set_sticker_mask_position(self, params: dict):
        method = 'setStickerMaskPosition'
        return await self._request(method, params)

    async def set_sticker_set_title(self, params: dict):
        method = 'setStickerSetTitle'
        return await self._request(method, params)

    async def set_sticker_set_thumbnail(self, params: dict):
        method = 'setStickerSetThumbnail'
        files = _get_files(params, 'thumbnail')
        return await self._request(method, params, files)

    async def set_custom_emoji_sticker_set_thumbnail(self, params: dict):
        method = 'setCustomEmojiStickerSetThumbnail'
        return await self._request(method, params)

    async def delete_sticker_set(self, params: dict):
        method = 'deleteStickerSet'
        return await self._request(method, params)

    async def answer_inline_query(self, params: dict):
        method = 'answerInlineQuery'
        return await self._request(method, params)

    async def answer_web_app_query(self, params: dict):
        method = 'answerWebAppQuery'
        return await self._request(method, params)

    async def send_invoice(self, params: dict):
        method = 'sendInvoice'
        return await self._request(method, params)

    async def create_invoice_link(self, params: dict):
        method = 'createInvoiceLink'
        return await self._request(method, params)

    async def answer_shipping_query(self, params: dict):
        method = 'answerShippingQuery'
        return await self._request(method, params)

    async def answer_pre_checkout_query(self, params: dict):
        method = 'answerPreCheckoutQuery'
        return await self._request(method, params)

    async def set_passport_data_errors(self, params: dict):
        method = 'setPassportDataErrors'
        return await self._request(method, params)

    async def send_game(self, params: dict):
        method = 'sendGame'
        return await self._request(method, params)

    async def set_game_score(self, params: dict):
        method = 'setGameScore'
        return await self._request(method, params)

    async def get_game_high_scores(self, params: dict):
        method = 'getGameHighScores'
        return await self._request(method, params)
