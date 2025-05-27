#!/bin/env python3

from __future__ import annotations

__all__ = (
    'REPLY_MARKUP_TYPES', # Union of all the reply markups
    'AcceptedGiftTypes',
    'AffiliateInfo',
    'Animation',
    'Audio',
    'Birthdate',
    'BackgroundFill', # Deserialized in _dese_background_fill()
    'BackgroundFillFreeformGradient',
    'BackgroundFillGradient',
    'BackgroundFillSolid',
    'BackgroundType', # Deserialized in _dese_background_type()
    'BackgroundTypeChatTheme',
    'BackgroundTypeFill',
    'BackgroundTypePattern',
    'BackgroundTypeWallpaper',
    'BotCommand',
    'BotCommandScope', # No deserialization.
    'BotCommandScopeAllChatAdministrators',
    'BotCommandScopeAllGroupChats',
    'BotCommandScopeAllPrivateChats',
    'BotCommandScopeChat',
    'BotCommandScopeChatAdministrators',
    'BotCommandScopeChatMember',
    'BotCommandScopeDefault',
    'BotDescription',
    'BotName',
    'BotShortDescription',
    'BusinessBotRights',
    'BusinessConnection',
    'BusinessIntro',
    'BusinessLocation',
    'BusinessMessagesDeleted',
    'BusinessOpeningHours',
    'BusinessOpeningHoursInterval',
    'CallbackGame',
    'CallbackQuery',
    'Chat',
    'ChatAdministratorRights',
    'ChatBackground',
    'ChatBoost',
    'ChatBoostAdded',
    'ChatBoostRemoved',
    'ChatBoostSource', # Deserialized in _dese_chat_boost_source()
    'ChatBoostSourceGiftCode',
    'ChatBoostSourceGiveaway',
    'ChatBoostSourcePremium',
    'ChatBoostUpdated',
    'ChatFullInfo',
    'ChatInviteLink',
    'ChatJoinRequest',
    'ChatLocation',
    'ChatMember', # Deserialized in _dese_chat_member()
    'ChatMemberAdministrator',
    'ChatMemberBanned',
    'ChatMemberLeft',
    'ChatMemberMember',
    'ChatMemberOwner',
    'ChatMemberRestricted',
    'ChatMemberUpdated',
    'ChatPermissions',
    'ChatPhoto',
    'ChatShared',
    'ChosenInlineResult',
    'Contact',
    'CopyTextButton',
    'Dice',
    'Document',
    'EncryptedCredentials',
    'EncryptedPassportElement',
    'ExternalReplyInfo',
    'File',
    'ForceReply',
    'ForumTopic',
    'ForumTopicClosed',
    'ForumTopicCreated',
    'ForumTopicEdited',
    'ForumTopicReopened',
    'Game',
    'GameHighScore',
    'GeneralForumTopicHidden',
    'GeneralForumTopicUnhidden',
    'Gift',
    'GiftInfo',
    'Gifts',
    'Giveaway',
    'GiveawayCompleted',
    'GiveawayCreated',
    'GiveawayWinners',
    'InaccessibleMessage',
    'InlineKeyboardButton',
    'InlineKeyboardMarkup',
    'InlineQuery',
    'InlineQueryResult', # No deserialization.
    'InlineQueryResultArticle',
    'InlineQueryResultAudio',
    'InlineQueryResultCachedAudio',
    'InlineQueryResultCachedDocument',
    'InlineQueryResultCachedGif',
    'InlineQueryResultCachedMpeg4Gif',
    'InlineQueryResultCachedPhoto',
    'InlineQueryResultCachedSticker',
    'InlineQueryResultCachedVideo',
    'InlineQueryResultCachedVoice',
    'InlineQueryResultContact',
    'InlineQueryResultDocument',
    'InlineQueryResultGame',
    'InlineQueryResultGif',
    'InlineQueryResultLocation',
    'InlineQueryResultMpeg4Gif',
    'InlineQueryResultPhoto',
    'InlineQueryResultVenue',
    'InlineQueryResultVideo',
    'InlineQueryResultVoice',
    'InlineQueryResultsButton',
    'InputContactMessageContent',
    'InputFile',
    'InputInvoiceMessageContent',
    'InputLocationMessageContent',
    'InputMedia', # No deserialization.
    'InputMediaAnimation',
    'InputMediaAudio',
    'InputMediaDocument',
    'InputMediaPhoto',
    'InputMediaVideo',
    'InputMessageContent', # No deserialization.
    'InputPaidMedia',
    'InputPaidMediaPhoto',
    'InputPaidMediaVideo',
    'InputPollOption',
    'InputProfilePhoto', # No deserialization.
    'InputProfilePhotoAnimated',
    'InputProfilePhotoStatic',
    'InputSticker', # No deserialization
    'InputStoryContent',
    'InputStoryContentPhoto',
    'InputStoryContentVideo',
    'InputTextMessageContent',
    'InputVenueMessageContent',
    'Invoice',
    'KeyboardButton',
    'KeyboardButtonPollType',
    'KeyboardButtonRequestChat',
    'KeyboardButtonRequestUsers',
    'LabeledPrice',
    'LinkPreviewOptions',
    'Location',
    'LocationAddress',
    'LoginUrl',
    'MaskPosition',
    'MaybeInaccessibleMessage', # Deserialized in _dese_maybe_inaccessible_message()
    'MenuButton', # Deserialized in _dese_menu_button()
    'MenuButtonCommands',
    'MenuButtonDefault',
    'MenuButtonWebApp',
    'Message',
    'MessageAutoDeleteTimerChanged',
    'MessageEntity',
    'MessageId',
    'MessageOrigin', # Deserialized in _dese_message_origin()
    'MessageOriginChannel',
    'MessageOriginChat',
    'MessageOriginHiddenUser',
    'MessageOriginUser',
    'MessageReactionCountUpdated',
    'MessageReactionUpdated',
    'OrderInfo',
    'OwnedGift', # Deserialized in _dese_owned_gift()
    'OwnedGifts',
    'OwnedGiftRegular',
    'OwnedGiftUnique',
    'PaidMedia', # Deserialized in _dese_paid_media()
    'PaidMediaInfo',
    'PaidMediaPhoto',
    'PaidMediaPreview',
    'PaidMediaPurchased',
    'PaidMediaVideo',
    'PaidMessagePriceChanged',
    'PassportData',
    'PassportElementError', # No deserialization.
    'PassportElementErrorDataField',
    'PassportElementErrorFile',
    'PassportElementErrorFiles',
    'PassportElementErrorFrontSide',
    'PassportElementErrorReverseSide',
    'PassportElementErrorSelfie',
    'PassportElementErrorTranslationFile',
    'PassportElementErrorTranslationFiles',
    'PassportElementErrorUnspecified',
    'PassportFile',
    'PhotoSize',
    'Poll',
    'PollAnswer',
    'PollOption',
    'PreCheckoutQuery',
    'PreparedInlineMessage',
    'ProximityAlertTriggered',
    'ReactionCount',
    'ReactionType', # Deserialized in _dese_reaction_type()
    'ReactionTypeCustomEmoji',
    'ReactionTypeEmoji',
    'ReactionTypePaid',
    'RefundedPayment',
    'ReplyKeyboardMarkup',
    'ReplyKeyboardRemove',
    'ReplyParameters',
    'ResponseParameters',
    'RevenueWithdrawalState', # Deserialized in _dese_revenue_withdrawal_state()
    'RevenueWithdrawalStateFailed',
    'RevenueWithdrawalStatePending',
    'RevenueWithdrawalStateSucceeded',
    'SentWebAppMessage',
    'SharedUser',
    'ShippingAddress',
    'ShippingOption',
    'ShippingQuery',
    'StarAmount',
    'StarTransaction',
    'StarTransactions',
    'Sticker',
    'StickerSet',
    'Story',
    'StoryArea',
    'StoryAreaPosition',
    'StoryAreaType',
    'StoryAreaTypeLink',
    'StoryAreaTypeLocation',
    'StoryAreaTypeSuggestedReaction',
    'StoryAreaTypeUniqueGift',
    'StoryAreaTypeWeather',
    'SuccessfulPayment',
    'SwitchInlineQueryChosenChat',
    'TextQuote',
    'TransactionPartner', # Deserialized in _dese_transaction_partner()
    'TransactionPartnerAffiliateProgram',
    'TransactionPartnerChat',
    'TransactionPartnerFragment',
    'TransactionPartnerOther',
    'TransactionPartnerTelegramAds',
    'TransactionPartnerTelegramApi',
    'TransactionPartnerUser',
    'UniqueGift',
    'UniqueGiftBackdrop',
    'UniqueGiftBackdropColors',
    'UniqueGiftInfo',
    'UniqueGiftModel',
    'UniqueGiftSymbol',
    'Update',
    'User',
    'UserChatBoosts',
    'UserProfilePhotos',
    'UsersShared',
    'Venue',
    'Video',
    'VideoChatEnded',
    'VideoChatParticipantsInvited',
    'VideoChatScheduled',
    'VideoChatStarted',
    'VideoNote',
    'Voice',
    'WebAppData',
    'WebAppInfo',
    'WriteAccessAllowed',
)
import os
from typing import (
    Self,
    Union,
    Literal,
    Optional,
    Callable,
)
from .constants import *


def _check_dict(res: dict, /) -> dict:
    '''
    Function to replace the dict key 'from' with 'from_user'.
    '''
    if isinstance(res, dict):
        if 'from' in res:
            res['from_user'] = res['from']
            del res['from']
        return res
    else:
        raise TypeError(
            'Expected dict as parameter in'
            f' _check_dict(), got {res.__class__.__name__}.'
        )


class TelegramType:
    ...


def _parse_result(_dese):
    '''
    Decorator to parse the result of a Telegram object.
    '''
    def wrap(cls: type, res: Optional[dict], *, check_dict: bool = True) -> Optional[TelegramType]:
        '''
        Method to deserialize a Telegram object.
        '''
        if check_dict:
            if res is None: return None
            return _dese(cls, _check_dict(res))
        else:
            return _dese(cls, res)

    return wrap


class AcceptedGiftTypes(TelegramType):
    '''
    https://core.telegram.org/bots/api#acceptedgifttypes

    This object describes the types of gifts that can be gifted to a user or a chat.

    :param unlimited_gifts: :obj:`True`, if unlimited regular gifts are accepted.
    :type unlimited_gifts: :obj:`bool`
    :param limited_gifts: :obj:`True`, if limited regular gifts are accepted.
    :type limited_gifts: :obj:`bool`
    :param unique_gifts: :obj:`True`, if unique gifts or gifts that can be upgraded to unique for free are accepted.
    :type unique_gifts: :obj:`bool`
    :param premium_subscription: :obj:`True`, if a Telegram Premium subscription is accepted.
    :type premium_subscription: :obj:`bool`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['unlimited_gifts'] = res.get('unlimited_gifts')
        obj['limited_gifts'] = res.get('limited_gifts')
        obj['unique_gifts'] = res.get('unique_gifts')
        obj['premium_subscription'] = res.get('premium_subscription')
        return cls(**obj)

    def __init__(
        self,
        unlimited_gifts: bool,
        limited_gifts: bool,
        unique_gifts: bool,
        premium_subscription: bool
    ):
        self.unlimited_gifts = unlimited_gifts
        self.limited_gifts = limited_gifts
        self.unique_gifts = unique_gifts
        self.premium_subscription = premium_subscription


class AffiliateInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#affiliateinfo

    Contains information about the affiliate that received a commission via this transaction.

    :param commission_per_mille: The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users.
    :type commission_per_mille: :obj:`int`
    :param amount: Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds.
    :type amount: :obj:`int`
    :param affiliate_user: The bot or the user that received an affiliate commission if it was received by a bot or a user.
    :type affiliate_user: :obj:`~apitele.types.User`, optional
    :param affiliate_chat: The chat that received an affiliate commission if it was received by a chat.
    :type affiliate_chat: :obj:`~apitele.types.Chat`, optional
    :param nanostar_amount: The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds.
    :type nanostar_amount: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res:dict):
        obj = {}
        obj['commission_per_mille'] = res.get('commission_per_mille')
        obj['amount'] = res.get('amount')
        obj['affiliate_user'] = User._dese(res.get('affiliate_user'))
        obj['affiliate_chat'] = Chat._dese(res.get('affiliate_chat'))
        obj['nanostar_amount'] = res.get('nanostar_amount')
        return cls(**obj)

    def __init__(
        self,
        commission_per_mille: int,
        amount: int,
        affiliate_user: Optional[User] = None,
        affiliate_chat: Optional[Chat] = None,
        nanostar_amount: Optional[int] = None
    ):
        self.commission_per_mille = commission_per_mille
        self.amount = amount
        self.affiliate_user = affiliate_user
        self.affiliate_chat = affiliate_chat
        self.nanostar_amount = nanostar_amount


class Animation(TelegramType):
    '''
    https://core.telegram.org/bots/api#animation

    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param width: Video width as defined by sender.
    :type width: :obj:`int`
    :param height: Video height as defined by sender.
    :type height: :obj:`int`
    :param duration: Duration of the video in seconds as defined by sender.
    :type duration: :obj:`int`
    :param thumbnail: Animation thumbnail as defined by sender.
    :type thumbnail: :obj:`~apitele.types.PhotoSize`, optional
    :param file_name: Original animation filename as defined by sender.
    :type file_name: :obj:`str`, optional
    :param mime_type: MIME type of the file as defined by sender.
    :type mime_type: :obj:`str`, optional
    :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['width'] = res.get('width')
        obj['height'] = res.get('height')
        obj['duration'] = res.get('duration')
        obj['thumbnail'] = PhotoSize._dese(res.get('thumbnail'))
        obj['file_name'] = res.get('file_name')
        obj['mime_type'] = res.get('mime_type')
        obj['file_size'] = res.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Audio(TelegramType):
    '''
    https://core.telegram.org/bots/api#audio

    This object represents an audio file to be treated as music by the Telegram clients.

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param duration: Duration of the audio in seconds as defined by sender.
    :type duration: :obj:`int`
    :param performer: Performer of the audio as defined by sender or by audio tags.
    :type performer: :obj:`str`, optional
    :param title: Title of the audio as defined by sender or by audio tags.
    :type title: :obj:`str`, optional
    :param file_name: Original filename as defined by sender.
    :type file_name: :obj:`str`, optional
    :param mime_type: MIME type of the file as defined by sender.
    :type mime_type: :obj:`str`, optional
    :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`, optional
    :param thumbnail: Thumbnail of the album cover to which the music file belongs.
    :type thumbnail: :obj:`~apitele.types.PhotoSize`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['duration'] = res.get('duration')
        obj['performer'] = res.get('performer')
        obj['title'] = res.get('title')
        obj['file_name'] = res.get('file_name')
        obj['mime_type'] = res.get('mime_type')
        obj['file_size'] = res.get('file_size')
        obj['thumbnail'] = PhotoSize._dese(res.get('thumbnail'))
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        thumbnail: Optional[PhotoSize] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail


class BackgroundFillFreeformGradient(TelegramType):
    '''
    https://core.telegram.org/bots/api#backgroundfillfreeformgradient

    The background is a freeform gradient that rotates after every message in the chat.

    :param colors: A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format.
    :type colors: :obj:`list` of :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['colors'] = res.get('colors')
        return cls(**obj)

    def __init__(
        self,
        colors: list[int]
    ):
        self.type = DEFAULT_BACKGROUND_FILL_FREEFORM_GRADIENT
        self.colors = colors


class BackgroundFillGradient(TelegramType):
    '''
    https://core.telegram.org/bots/api#backgroundfillgradient

    The background is a gradient fill.

    :param top_color: Top color of the gradient in the RGB24 format.
    :type top_color: :obj:`int`
    :param bottom_color: Bottom color of the gradient in the RGB24 format.
    :type bottom_color: :obj:`int`
    :param rotation_angle: Clockwise rotation angle of the background fill in degrees; 0-359.
    :type rotation_angle: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['top_color'] = res.get('top_color')
        obj['bottom_color'] = res.get('bottom_color')
        obj['rotation_angle'] = res.get('rotation_angle')
        return cls(**obj)

    def __init__(
        self,
        top_color: int,
        bottom_color: int,
        rotation_angle: int
    ):
        self.type = DEFAULT_BACKGROUND_FILL_GRADIENT
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.rotation_angle = rotation_angle


class BackgroundFillSolid(TelegramType):
    '''
    https://core.telegram.org/bots/api#backgroundfillsolid

    The background is filled using the selected color.

    :param color: The color of the background fill in the RGB24 format.
    :type color: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['color'] = res.get('color')
        return cls(**obj)

    def __init__(
        self,
        color: int
    ):
        self.type = DEFAULT_BACKGROUND_FILL_SOLID
        self.color = color


class BackgroundTypeChatTheme(TelegramType):
    '''
    https://core.telegram.org/bots/api#backgroundtypechattheme

    The background is taken directly from a built-in chat theme.

    :param theme_name: Name of the chat theme, which is usually an emoji.
    :type theme_name: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['theme_name'] = res.get('theme_name')
        return cls(**obj)

    def __init__(
        self,
        theme_name: str
    ):
        self.type = DEFAULT_BACKGROUND_TYPE_CHAT_THEME
        self.theme_name = theme_name


class BackgroundTypeFill(TelegramType):
    '''
    https://core.telegram.org/bots/api#backgroundtypefill

    The background is automatically filled based on the selected colors.

    :param fill: The background fill.
    :type fill: :obj:`~apitele.types.BackgroundFill`
    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100.
    :type dark_theme_dimming: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['fill'] = _dese_background_fill(res.get('fill'))
        obj['dark_theme_dimming'] = res.get('dark_theme_dimming')
        return cls(**obj)

    def __init__(
        self,
        fill: BackgroundFill,
        dark_theme_dimming: int
    ):
        self.type = DEFAULT_BACKGROUND_TYPE_FILL
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming


class BackgroundTypePattern(TelegramType):
    '''
    https://core.telegram.org/bots/api#backgroundtypepattern

    The background is a PNG or TGV (gzipped subset of SVG with MIME type
    “application/x-tgwallpattern”) pattern to be combined with the background fill chosen by the user.

    :param document: Document with the pattern.
    :type document: :obj:`~apitele.types.Document`
    :param fill: The background fill that is combined with the pattern.
    :type fill: :obj:`~apitele.types.BackgroundFill`
    :param intensity: Intensity of the pattern when it is shown above the filled background; 0-100.
    :type intensity: :obj:`int`
    :param is_inverted: :obj:`True`, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only.
    :type is_inverted: :obj:`True`, optional
    :param is_moving: :obj:`True`, if the background moves slightly when the device is tilted.
    :type is_moving: :obj:`True`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['document'] = Document._dese(res.get('document'))
        obj['fill'] = _dese_background_fill(res.get('fill'))
        obj['intensity'] = res.get('intensity')
        obj['is_inverted'] = res.get('is_inverted')
        obj['is_moving'] = res.get('is_moving')
        return cls(**obj)

    def __init__(
        self,
        document: Document,
        fill: BackgroundFill,
        intensity: int,
        is_inverted: Optional[Literal[True]] = None,
        is_moving: Optional[Literal[True]] = None
    ):
        self.type = DEFAULT_BACKGROUND_TYPE_PATTERN
        self.document = document
        self.fill = fill
        self.intensity = intensity
        self.is_inverted = is_inverted
        self.is_moving = is_moving


class BackgroundTypeWallpaper(TelegramType):
    '''
    https://core.telegram.org/bots/api#backgroundtypewallpaper

    The background is a wallpaper in the JPEG format.

    :param document: Document with the wallpaper.
    :type document: :obj:`~apitele.types.Document`
    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100.
    :type dark_theme_dimming: :obj:`int`
    :param is_blurred: :obj:`True`, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12.
    :type is_blurred: :obj:`True`, optional
    :param is_moving: :obj:`True`, if the background moves slightly when the device is tilted.
    :type is_moving: :obj:`True`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['document'] = Document._dese(res.get('document'))
        obj['dark_theme_dimming'] = res.get('dark_theme_dimming')
        obj['is_blurred'] = res.get('is_blurred')
        obj['is_moving'] = res.get('is_moving')
        return cls(**obj)

    def __init__(
        self,
        document: Document,
        dark_theme_dimming: int,
        is_blurred: Optional[Literal[True]] = None,
        is_moving: Optional[Literal[True]] = None
    ):
        self.type = DEFAULT_BACKGROUND_TYPE_WALLPAPER
        self.document = document
        self.dark_theme_dimming = dark_theme_dimming
        self.is_blurred = is_blurred
        self.is_moving = is_moving


class Birthdate(TelegramType):
    '''
    https://core.telegram.org/bots/api#birthdate

    :param day: Day of the user's birth; 1-31.
    :type day: :obj:`int`
    :param month: Month of the user's birth; 1-12.
    :type month: :obj:`int`
    :param year: Year of the user's birth.
    :type year: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['day'] = res.get('day')
        obj['month'] = res.get('month')
        obj['year'] = res.get('year')
        return cls(**obj)

    def __init__(
        self,
        day: int,
        month: int,
        year: Optional[int] = None
    ):
        self.day = day
        self.month = month
        self.year = year


class BotCommand(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommand

    This object represents a bot command.

    :param command: Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    :type command: :obj:`str`
    :param description: Description of the command; 1-256 characters.
    :type description: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['command'] = res.get('command')
        obj['description'] = res.get('description')
        return cls(**obj)

    def __init__(
        self,
        command: str,
        description: str
    ):
        self.command = command
        self.description = description


class BotCommandScopeAllChatAdministrators(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscopeallchatadministrators

    Represents the :obj:`scope <apitele.types.BotCommandScope>` of bot commands, covering all group and supergroup chat administrators.
    '''
    def __init__(self):
        self.type = DEFAULT_BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS


class BotCommandScopeAllGroupChats(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscopeallgroupchats

    Represents the :obj:`scope <apitele.types.BotCommandScope>` of bot commands, covering all group and supergroup chats.
    '''
    def __init__(self):
        self.type = DEFAULT_BOT_COMMAND_SCOPE_ALL_GROUP_CHATS


class BotCommandScopeAllPrivateChats(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscopeallprivatechats

    Represents the :obj:`scope <apitele.types.BotCommandScope>` of bot commands, covering all private chats.
    '''
    def __init__(self):
        self.type = DEFAULT_BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS


class BotCommandScopeChat(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscopechat

    Represents the :obj:`scope <apitele.types.BotCommandScope>` of bot commands, covering a specific chat.

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
    :type chat_id: :obj:`int` or :obj:`str`
    '''
    def __init__(
        self,
        chat_id: Union[int, str]
    ):
        self.type = DEFAULT_BOT_COMMAND_SCOPE_CHAT
        self.chat_id = chat_id


class BotCommandScopeChatAdministrators(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscopechatadministrators

    Represents the :obj:`scope <apitele.types.BotCommandScope>` of bot commands, covering all administrators of a specific group or supergroup chat.

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
    :type chat_id: :obj:`int` or :obj:`str`
    '''
    def __init__(
        self,
        chat_id: Union[int, str]
    ):
        self.type = DEFAULT_BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS
        self.chat_id = chat_id


class BotCommandScopeChatMember(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscopechatmember

    Represents the :obj:`scope <apitele.types.BotCommandScope>` of bot commands, covering a specific member of a group or supergroup chat.

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
    :type chat_id: :obj:`int` or :obj:`str`
    :param user_id: Unique identifier of the target user.
    :type user_id: :obj:`int`
    '''
    def __init__(
        self,
        chat_id: Union[int, str],
        user_id: int
    ):
        self.type = DEFAULT_BOT_COMMAND_SCOPE_CHAT_MEMBER
        self.chat_id = chat_id
        self.user_id = user_id


class BotCommandScopeDefault(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscopedefault

    Represents the default :obj:`scope <apitele.types.BotCommandScope>` of bot commands. Default commands are used if no commands
    with a `narrower scope <https://core.telegram.org/bots/api#determining-list-of-commands>`_ are specified for the user.
    '''
    def __init__(self):
        self.type = DEFAULT_BOT_COMMAND_SCOPE_DEFAULT


class BotDescription(TelegramType):
    '''
    https://core.telegram.org/bots/api#botdescription

    This object represents the bot's description.

    :param description: The bot's description.
    :type description: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['description'] = res.get('description')
        return cls(**obj)

    def __init__(
        self,
        description: str
    ):
        self.description = description


class BotName(TelegramType):
    '''
    https://core.telegram.org/bots/api#botname

    This object represents the bot's name.

    :param name: The bot's name.
    :type name: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        return cls(**obj)

    def __init__(
        self,
        name: str
    ):
        self.name = name


class BotShortDescription(TelegramType):
    '''
    https://core.telegram.org/bots/api#botshortdescription

    This object represents the bot's short description.

    :param short_description: The bot's short description.
    :type short_description: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['short_description'] = res.get('short_description')
        return cls(**obj)

    def __init__(
        self,
        short_description: str
    ):
        self.short_description = short_description


class BusinessBotRights(TelegramType):
    '''
    https://core.telegram.org/bots/api#businessbotrights

    Represents the rights of a business bot.

    :param can_reply: :obj:`True`, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours.
    :type can_reply: :obj:`True`, optional
    :param can_read_messages: :obj:`True`, if the bot can mark incoming private messages as read.
    :type can_read_messages: :obj:`True`, optional
    :param can_delete_sent_messages: :obj:`True`, if the bot can delete messages sent by the bot.
    :type can_delete_sent_messages: :obj:`True`, optional
    :param can_delete_all_messages: :obj:`True`, if the bot can delete all private messages in managed chats.
    :type can_delete_all_messages: :obj:`True`, optional
    :param can_edit_name: :obj:`True`, if the bot can edit the first and last name of the business account.
    :type can_edit_name: :obj:`True`, optional
    :param can_edit_bio: :obj:`True`, if the bot can edit the bio of the business account.
    :type can_edit_bio: :obj:`True`, optional
    :param can_edit_profile_photo: :obj:`True`, if the bot can edit the profile photo of the business account.
    :type can_edit_profile_photo: :obj:`True`, optional
    :param can_edit_username: :obj:`True`, if the bot can edit the username of the business account.
    :type can_edit_username: :obj:`True`, optional
    :param can_change_gift_settings: :obj:`True`, if the bot can change the privacy settings pertaining to gifts for the business account.
    :type can_change_gift_settings: :obj:`True`, optional
    :param can_view_gifts_and_stars: :obj:`True`, if the bot can view gifts and the amount of Telegram Stars owned by the business account.
    :type can_view_gifts_and_stars: :obj:`True`, optional
    :param can_convert_gifts_to_stars: :obj:`True`, if the bot can convert regular gifts owned by the business account to Telegram Stars.
    :type can_convert_gifts_to_stars: :obj:`True`, optional
    :param can_transfer_and_upgrade_gifts: :obj:`True`, if the bot can transfer and upgrade gifts owned by the business account.
    :type can_transfer_and_upgrade_gifts: :obj:`True`, optional
    :param can_transfer_stars: :obj:`True`, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts.
    :type can_transfer_stars: :obj:`True`, optional
    :param can_manage_stories: :obj:`True`, if the bot can post, edit and delete stories on behalf of the business account.
    :type can_manage_stories: :obj:`True`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['can_reply'] = res.get('can_reply')
        obj['can_read_messages'] = res.get('can_read_messages')
        obj['can_delete_sent_messages'] = res.get('can_delete_sent_messages')
        obj['can_delete_all_messages'] = res.get('can_delete_all_messages')
        obj['can_edit_name'] = res.get('can_edit_name')
        obj['can_edit_bio'] = res.get('can_edit_bio')
        obj['can_edit_profile_photo'] = res.get('can_edit_profile_photo')
        obj['can_edit_username'] = res.get('can_edit_username')
        obj['can_change_gift_settings'] = res.get('can_change_gift_settings')
        obj['can_view_gifts_and_stars'] = res.get('can_view_gifts_and_stars')
        obj['can_convert_gifts_to_stars'] = res.get('can_convert_gifts_to_stars')
        obj['can_transfer_and_upgrade_gifts'] = res.get('can_transfer_and_upgrade_gifts')
        obj['can_transfer_stars'] = res.get('can_transfer_stars')
        obj['can_manage_stories'] = res.get('can_manage_stories')
        return cls(**obj)

    def __init__(
        self,
        can_reply: Optional[Literal[True]] = None,
        can_read_messages: Optional[Literal[True]] = None,
        can_delete_sent_messages: Optional[Literal[True]] = None,
        can_delete_all_messages: Optional[Literal[True]] = None,
        can_edit_name: Optional[Literal[True]] = None,
        can_edit_bio: Optional[Literal[True]] = None,
        can_edit_profile_photo: Optional[Literal[True]] = None,
        can_edit_username: Optional[Literal[True]] = None,
        can_change_gift_settings: Optional[Literal[True]] = None,
        can_view_gifts_and_stars: Optional[Literal[True]] = None,
        can_convert_gifts_to_stars: Optional[Literal[True]] = None,
        can_transfer_and_upgrade_gifts: Optional[Literal[True]] = None,
        can_transfer_stars: Optional[Literal[True]] = None,
        can_manage_stories: Optional[Literal[True]] = None
    ):
        self.can_reply = can_reply
        self.can_read_messages = can_read_messages
        self.can_delete_sent_messages = can_delete_sent_messages
        self.can_delete_all_messages = can_delete_all_messages
        self.can_edit_name = can_edit_name
        self.can_edit_bio = can_edit_bio
        self.can_edit_profile_photo = can_edit_profile_photo
        self.can_edit_username = can_edit_username
        self.can_change_gift_settings = can_change_gift_settings
        self.can_view_gifts_and_stars = can_view_gifts_and_stars
        self.can_convert_gifts_to_stars = can_convert_gifts_to_stars
        self.can_transfer_and_upgrade_gifts = can_transfer_and_upgrade_gifts
        self.can_transfer_stars = can_transfer_stars
        self.can_manage_stories = can_manage_stories


class BusinessConnection(TelegramType):
    '''
    https://core.telegram.org/bots/api#businessconnection

    Describes the connection of the bot with a business account.

    :param id: Unique identifier of the business connection.
    :type id: :obj:`str`
    :param user: Business account user that created the business connection.
    :type user: :obj:`~apitele.types.User`
    :param user_chat_id: Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type user_chat_id: :obj:`int`
    :param date: Date the connection was established in Unix time.
    :type date: :obj:`int`
    :param is_enabled: :obj:`True`, if the connection is active.
    :type is_enabled: :obj:`bool`
    :param rights: Rights of the business bot.
    :type rights: :obj:`~apitele.types.BusinessBotRights`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['user'] = User._dese(res.get('user'))
        obj['user_chat_id'] = res.get('user_chat_id')
        obj['date'] = res.get('date')
        obj['is_enabled'] = res.get('is_enabled')
        obj['rights'] = BusinessBotRights._dese(res.get('rights'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        user: User,
        user_chat_id: int,
        date: int,
        is_enabled: bool,
        rights: Optional[BusinessBotRights] = None,
    ):
        self.id = id
        self.user = user
        self.user_chat_id = user_chat_id
        self.date = date
        self.is_enabled = is_enabled
        self.rights = rights


class BusinessIntro(TelegramType):
    '''
    https://core.telegram.org/bots/api#businessintro

    :param title: Title text of the business intro.
    :type title: :obj:`str`, optional
    :param message: Message text of the business intro.
    :type message: :obj:`str`, optional
    :param sticker: Sticker of the business intro.
    :type sticker: :obj:`~apitele.types.Sticker`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['title'] = res.get('title')
        obj['message'] = res.get('message')
        obj['sticker'] = Sticker._dese(res.get('sticker'))
        return cls(**obj)

    def __init__(
        self,
        title: Optional[str] = None,
        message: Optional[str] = None,
        sticker: Optional[Sticker] = None
    ):
        self.title = title
        self.message = message
        self.sticker = sticker


class BusinessLocation(TelegramType):
    '''
    https://core.telegram.org/bots/api#businesslocation

    :param address: Address of the business.
    :type address: :obj:`str`
    :param location: Location of the business.
    :type location: :obj:`~apitele.types.Location`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['address'] = res.get('address')
        obj['location'] = Location._dese(res.get('location'))
        return cls(**obj)

    def __init__(
        self,
        address: str,
        location: Optional[Location] = None
    ):
        self.address = address
        self.location = location


class BusinessMessagesDeleted(TelegramType):
    '''
    https://core.telegram.org/bots/api#businessmessagesdeleted

    This object is received when messages are deleted from a connected business account.

    :param business_connection_id: Unique identifier of the business connection.
    :type business_connection_id: :obj:`str`
    :param chat: Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.
    :type chat: :obj:`~apitele.types.Chat`
    :param message_ids: A JSON-serialized list of identifiers of deleted messages in the chat of the business account.
    :type message_ids: :obj:`list` of :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['business_connection_id'] = res.get('business_connection_id')
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['message_ids'] = res.get('message_ids')
        return cls(**obj)

    def __init__(
        self,
        business_connection_id: str,
        chat: Chat,
        message_ids: list[int]
    ):
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids


class BusinessOpeningHours(TelegramType):
    '''
    https://core.telegram.org/bots/api#businessopeninghours

    :param time_zone_name: Unique name of the time zone for which the opening hours are defined.
    :type time_zone_name: :obj:`str`
    :param opening_hours: List of time intervals describing business opening hours.
    :type opening_hours: :obj:`list` of :obj:`~apitele.types.BusinessOpeningHoursInterval`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['time_zone_name'] = res.get('time_zone_name')
        obj['opening_hours'] = [BusinessOpeningHoursInterval._dese(kwargs) for kwargs in res.get('opening_hours')]
        return cls(**obj)

    def __init__(
        self,
        time_zone_name: str,
        opening_hours: list[BusinessOpeningHoursInterval]
    ):
        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours


class BusinessOpeningHoursInterval(TelegramType):
    '''
    https://core.telegram.org/bots/api#businessopeninghoursinterval

    :param opening_minute: The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60.
    :type opening_minute: :obj:`int`
    :param closing_minute: The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60.
    :type closing_minute: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['opening_minute'] = res.get('opening_minute')
        obj['closing_minute'] = res.get('closing_minute')
        return cls(**obj)

    def __init__(
        self,
        opening_minute: int,
        closing_minute: int
    ):
        self.opening_minute = opening_minute
        self.closing_minute = closing_minute


class CallbackGame(TelegramType):
    '''
    https://core.telegram.org/bots/api#callbackgame

    A placeholder, currently holds no information. Use `BotFather <https://t.me/botfather>`_ to set up your game.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        ...


class CallbackQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#callbackquery

    This object represents an incoming callback query from a callback button in an
    `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
    If the button that originated the query was attached to a message sent by the bot,
    the field message will be present. If the button was attached to a message sent via
    the bot (in `inline mode <https://core.telegram.org/bots/api#inline-mode>`_),
    the field *inline_message_id* will be present.
    Exactly one of the fields *data* or *game_short_name* will be present.

    :param id: Unique identifier for this query.
    :type id: :obj:`str`
    :param from_user: Sender.
    :type from_user: :obj:`~apitele.types.User`
    :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in `games <https://core.telegram.org/bots/api#games>`_.
    :type chat_instance: :obj:`str`
    :param message: Message sent by the bot with the callback button that originated the query.
    :type message: :obj:`~apitele.types.MaybeInaccessibleMessage`, optional
    :param inline_message_id: Identifier of the message sent via the bot in inline mode, that originated the query.
    :type inline_message_id: :obj:`str`, optional
    :param data: Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.
    :type data: :obj:`str`, optional
    :param game_short_name: Short name of a `Game <https://core.telegram.org/bots/api#games>`_ to be returned, serves as the unique identifier for the game.
    :type game_short_name: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['chat_instance'] = res.get('chat_instance')
        obj['message'] = _dese_maybe_inaccessible_message(res.get('message'))
        obj['inline_message_id'] = res.get('inline_message_id')
        obj['data'] = res.get('data')
        obj['game_short_name'] = res.get('game_short_name')
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        chat_instance: str,
        message: Optional[MaybeInaccessibleMessage] = None,
        inline_message_id: Optional[str] = None,
        data: Optional[str] = None,
        game_short_name: Optional[str] = None
    ):
        self.id = id
        self.from_user = from_user
        self.chat_instance = chat_instance
        self.message = message
        self.inline_message_id = inline_message_id
        self.data = data
        self.game_short_name = game_short_name


class Chat(TelegramType):
    '''
    https://core.telegram.org/bots/api#chat

    This object represents a chat.

    :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`
    :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”.
    :type type: :obj:`str`
    :param title: Title, for supergroups, channels and group chats.
    :type title: :obj:`str`, optional
    :param username: Username, for private chats, supergroups and channels if available.
    :type username: :obj:`str`, optional
    :param first_name: First name of the other party in a private chat.
    :type first_name: :obj:`str`, optional
    :param last_name: Last name of the other party in a private chat.
    :type last_name: :obj:`str`, optional
    :param is_forum: :obj:`True`, if the supergroup chat is a forum (has `topics <https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups>`_ enabled).
    :type is_forum: :obj:`True`, optional
    :param photo: Chat photo. Returned only in :meth:`~apitele.Client.get_chat`.
    :type photo: :obj:`~apitele.types.ChatPhoto`, optional
    :param active_usernames: If non-empty, the list of all `active chat usernames <https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames>`_; for private chats, supergroups and channels. Returned only in :meth:`~apitele.Client.get_chat`.
    :type active_usernames: :obj:`list` of :obj:`str`, optional
    :param birthdate: For private chats, the date of birth of the user. Returned only in :meth:`~apitele.Client.get_chat`.
    :type birthdate: :obj:`~apitele.types.Birthdate`, optional
    :param business_intro: For private chats with business accounts, the intro of the business. Returned only in :meth:`~apitele.Client.get_chat`.
    :type business_intro: :obj:`~apitele.types.BusinessIntro`
    :param business_location: For private chats with business accounts, the location of the business. Returned only in :meth:`~apitele.Client.get_chat`.
    :type business_location: :obj:`~apitele.types.BusinessLocation`
    :param business_opening_hours: For private chats with business accounts, the opening hours of the business. Returned only in :meth:`~apitele.Client.get_chat`.
    :type business_opening_hours: :obj:`~apitele.types.BusinessOpeningHours`, optional
    :param personal_chat: For private chats, the personal channel of the user. Returned only in :meth:`~apitele.Client.get_chat`.
    :type personal_chat: :obj:`~apitele.types.Chat`, optional
    :param available_reactions: List of available reactions allowed in the chat. If omitted, then all :obj:`emoji reactions <apitele.types.ReactionTypeEmoji>` are allowed. Returned only in :meth:`~apitele.Client.get_chat`.
    :type available_reactions: :obj:`list` of :obj:`~apitele.types.ReactionType`, optional
    :param accent_color_id: Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See `accent colors <https://core.telegram.org/bots/api#accent-colors>`_ for more details. Returned only in :meth:`~apitele.Client.get_chat`.
    :type accent_color_id: :obj:`int`, optional
    :param background_custom_emoji_id: Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Returned only in :meth:`~apitele.Client.get_chat`.
    :type background_custom_emoji_id: :obj:`str`, optional
    :param profile_accent_color_id: Identifier of the accent color for the chat's profile background. See `profile accent colors <https://core.telegram.org/bots/api#profile-accent-colors>`_ for more details. Returned only in :meth:`~apitele.Client.get_chat`.
    :type profile_accent_color_id: :obj:`int`, optional
    :param profile_background_custom_emoji_id: Custom emoji identifier of the emoji chosen by the chat for its profile background. Returned only in :meth:`~apitele.Client.get_chat`.
    :type profile_background_custom_emoji_id: :obj:`str`, optional
    :param emoji_status_custom_emoji_id: Custom emoji identifier of the emoji status of the chat or the other party in a private chat. Returned only in :meth:`~apitele.Client.get_chat`.
    :type emoji_status_custom_emoji_id: :obj:`str`, optional
    :param emoji_status_expiration_date: Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any. Returned only in :meth:`~apitele.Client.get_chat`.
    :type emoji_status_expiration_date: :obj:`int`, optional
    :param bio: Bio of the other party in a private chat. Returned only in :meth:`~apitele.Client.get_chat`.
    :type bio: :obj:`str`, optional
    :param has_private_forwards: :obj:`True`, if privacy settings of the other party in the private chat allows to use ``tg://user?id=<user_id>`` links only in chats with the user. Returned only in :meth:`~apitele.Client.get_chat`.
    :type has_private_forwards: :obj:`True`, optional
    :param has_restricted_voice_and_video_messages: :obj:`True`, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in :meth:`~apitele.Client.get_chat`.
    :type has_restricted_voice_and_video_messages: :obj:`True`, optional
    :param join_to_send_messages: :obj:`True`, if users need to join the supergroup before they can send messages. Returned only in :meth:`~apitele.Client.get_chat`.
    :type join_to_send_messages: :obj:`True`, optional
    :param join_by_request: :obj:`True`, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in :meth:`~apitele.Client.get_chat`.
    :type join_by_request: :obj:`True`, optional
    :param description: Description, for groups, supergroups and channel chats. Returned only in :meth:`~apitele.Client.get_chat`.
    :type description: :obj:`str`, optional
    :param invite_link: Primary invite link, for groups, supergroups and channel chats. Returned only in :meth:`~apitele.Client.get_chat`.
    :type invite_link: :obj:`str`, optional
    :param pinned_message: The most recent pinned message (by sending date). Returned only in :meth:`~apitele.Client.get_chat`.
    :type pinned_message: :obj:`~apitele.types.Message`, optional
    :param permissions: Default chat member permissions, for groups and supergroups. Returned only in :meth:`~apitele.Client.get_chat`.
    :type permissions: :obj:`~apitele.types.ChatPermissions`, optional
    :param slow_mode_delay: For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds. Returned only in :meth:`~apitele.Client.get_chat`.
    :type slow_mode_delay: :obj:`int`, optional
    :param unrestrict_boost_count: For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Returned only in :meth:`~apitele.Client.get_chat`.
    :type unrestrict_boost_count: :obj:`int`, optional
    :param message_auto_delete_time: The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in :meth:`~apitele.Client.get_chat`.
    :type message_auto_delete_time: :obj:`int`, optional
    :param has_aggressive_anti_spam_enabled: :obj:`True`, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in :meth:`~apitele.Client.get_chat`.
    :type has_aggressive_anti_spam_enabled: :obj:`True`, optional
    :param has_hidden_members: :obj:`True`, if non-administrators can only get the list of bots and administrators in the chat. Returned only in :meth:`~apitele.Client.get_chat`.
    :type has_hidden_members: :obj:`True`, optional
    :param has_protected_content: :obj:`True`, if messages from the chat can't be forwarded to other chats. Returned only in :meth:`~apitele.Client.get_chat`.
    :type has_protected_content: :obj:`True`, optional
    :param has_visible_history: :obj:`True`, if new chat members will have access to old messages; available only to chat administrators. Returned only in :meth:`~apitele.Client.get_chat`.
    :type has_visible_history: :obj:`True`, optional
    :param sticker_set_name: For supergroups, name of group sticker set. Returned only in :meth:`~apitele.Client.get_chat`.
    :type sticker_set_name: :obj:`str`, optional
    :param can_set_sticker_set: :obj:`True`, if the bot can change the group sticker set. Returned only in :meth:`~apitele.Client.get_chat`.
    :type can_set_sticker_set: :obj:`True`, optional
    :param custom_emoji_sticker_set_name: For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. Returned only in :meth:`~apitele.Client.get_chat`.
    :type custom_emoji_sticker_set_name: :obj:`str`, optional
    :param linked_chat_id: Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in :meth:`~apitele.Client.get_chat`.
    :type linked_chat_id: :obj:`int`, optional
    :param location: For supergroups, the location to which the supergroup is connected. Returned only in :meth:`~apitele.Client.get_chat`.
    :type location: :obj:`~apitele.types.ChatLocation`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['type'] = res.get('type')
        obj['title'] = res.get('title')
        obj['username'] = res.get('username')
        obj['first_name'] = res.get('first_name')
        obj['last_name'] = res.get('last_name')
        obj['is_forum'] = res.get('is_forum')
        obj['photo'] = ChatPhoto._dese(res.get('photo'))
        obj['active_usernames'] = res.get('active_usernames')
        obj['birthdate'] = Birthdate._dese(res.get('birthdate'))
        obj['business_intro'] = BusinessIntro._dese(res.get('business_intro'))
        obj['business_location'] = BusinessLocation._dese(res.get('business_location'))
        obj['business_opening_hours'] = BusinessOpeningHours._dese(res.get('business_opening_hours'))
        obj['personal_chat'] = Chat._dese(res.get('personal_chat'))
        obj['available_reactions'] = [_dese_reaction_type(kwargs) for kwargs in res.get('available_reactions')] if 'available_reactions' in res else None
        obj['accent_color_id'] = res.get('accent_color_id')
        obj['background_custom_emoji_id'] = res.get('background_custom_emoji_id')
        obj['profile_accent_color_id'] = res.get('profile_accent_color_id')
        obj['profile_background_custom_emoji_id'] = res.get('profile_background_custom_emoji_id')
        obj['emoji_status_custom_emoji_id'] = res.get('emoji_status_custom_emoji_id')
        obj['emoji_status_expiration_date'] = res.get('emoji_status_expiration_date')
        obj['bio'] = res.get('bio')
        obj['has_private_forwards'] = res.get('has_private_forwards')
        obj['has_restricted_voice_and_video_messages'] = res.get('has_restricted_voice_and_video_messages')
        obj['join_to_send_messages'] = res.get('join_to_send_messages')
        obj['join_by_request'] = res.get('join_by_request')
        obj['description'] = res.get('description')
        obj['invite_link'] = res.get('invite_link')
        obj['pinned_message'] = Message._dese(res.get('pinned_message'))
        obj['permissions'] = ChatPermissions._dese(res.get('permissions'))
        obj['slow_mode_delay'] = res.get('slow_mode_delay')
        obj['unrestrict_boost_count'] = res.get('unrestrict_boost_count')
        obj['message_auto_delete_time'] = res.get('message_auto_delete_time')
        obj['has_aggressive_anti_spam_enabled'] = res.get('has_aggressive_anti_spam_enabled')
        obj['has_hidden_members'] = res.get('has_hidden_members')
        obj['has_protected_content'] = res.get('has_protected_content')
        obj['has_visible_history'] = res.get('has_visible_history')
        obj['sticker_set_name'] = res.get('sticker_set_name')
        obj['can_set_sticker_set'] = res.get('can_set_sticker_set')
        obj['custom_emoji_sticker_set_name'] = res.get('custom_emoji_sticker_set_name')
        obj['linked_chat_id'] = res.get('linked_chat_id')
        obj['location'] = ChatLocation._dese(res.get('location'))
        return cls(**obj)

    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        is_forum: Optional[Literal[True]] = None,
        photo: Optional[ChatPhoto] = None,
        active_usernames: Optional[list[str]] = None,
        birthdate: Optional[Birthdate] = None,
        business_intro: Optional[BusinessIntro] = None,
        business_location: Optional[BusinessLocation] = None,
        business_opening_hours: Optional[BusinessOpeningHours] = None,
        personal_chat: Optional[Chat] = None,
        available_reactions: Optional[list[ReactionType]] = None,
        accent_color_id: Optional[int] = None,
        background_custom_emoji_id: Optional[str] = None,
        profile_accent_color_id: Optional[int] = None,
        profile_background_custom_emoji_id: Optional[str] = None,
        emoji_status_custom_emoji_id: Optional[str] = None,
        emoji_status_expiration_date: Optional[int] = None,
        bio: Optional[str] = None,
        has_private_forwards: Optional[Literal[True]] = None,
        has_restricted_voice_and_video_messages: Optional[Literal[True]] = None,
        join_to_send_messages: Optional[Literal[True]] = None,
        join_by_request: Optional[Literal[True]] = None,
        description: Optional[str] = None,
        invite_link: Optional[str] = None,
        pinned_message: Optional[Message] = None,
        permissions: Optional[ChatPermissions] = None,
        slow_mode_delay: Optional[int] = None,
        unrestrict_boost_count: Optional[int] = None,
        message_auto_delete_time: Optional[int] = None,
        has_aggressive_anti_spam_enabled: Optional[Literal[True]] = None,
        has_hidden_members: Optional[Literal[True]] = None,
        has_protected_content: Optional[Literal[True]] = None,
        has_visible_history: Optional[Literal[True]] = None,
        sticker_set_name: Optional[str] = None,
        can_set_sticker_set: Optional[Literal[True]] = None,
        custom_emoji_sticker_set_name: Optional[str] = None,
        linked_chat_id: Optional[int] = None,
        location: Optional[ChatLocation] = None
    ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.photo = photo
        self.active_usernames = active_usernames
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
        self.available_reactions = available_reactions
        self.accent_color_id = accent_color_id
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location


class ChatAdministratorRights(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatadministratorrights

    Represents the rights of an administrator in a chat.

    :param is_anonymous: :obj:`True`, if the user's presence in the chat is hidden.
    :type is_anonymous: :obj:`bool`
    :param can_manage_chat: :obj:`True`, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
    :type can_manage_chat: :obj:`bool`
    :param can_delete_messages: :obj:`True`, if the administrator can delete messages of other users.
    :type can_delete_messages: :obj:`bool`
    :param can_manage_video_chats: :obj:`True`, if the administrator can manage video chats.
    :type can_manage_video_chats: :obj:`bool`
    :param can_restrict_members: :obj:`True`, if the administrator can restrict, ban or unban chat members, or access supergroup statistics.
    :type can_restrict_members: :obj:`bool`
    :param can_promote_members: :obj:`True`, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user).
    :type can_promote_members: :obj:`bool`
    :param can_change_info: :obj:`True`, if the user is allowed to change the chat title, photo and other settings.
    :type can_change_info: :obj:`bool`
    :param can_invite_users: :obj:`True`, if the user is allowed to invite new users to the chat.
    :type can_invite_users: :obj:`bool`
    :param can_post_stories: :obj:`True`, if the administrator can post stories to the chat.
    :type can_post_stories: :obj:`bool`
    :param can_edit_stories: :obj:`True`, if the administrator can edit stories posted by other users.
    :type can_edit_stories: :obj:`bool`
    :param can_delete_stories: :obj:`True`, if the administrator can delete stories posted by other users.
    :type can_delete_stories: :obj:`bool`
    :param can_post_messages: :obj:`True`, if the administrator can post messages in the channel, or access channel statistics; for channels only.
    :type can_post_messages: :obj:`bool`, optional
    :param can_edit_messages: :obj:`True`, if the administrator can edit messages of other users and can pin messages; for channels only.
    :type can_edit_messages: :obj:`bool`, optional
    :param can_pin_messages: :obj:`True`, if the user is allowed to pin messages; for groups and supergroups only.
    :type can_pin_messages: :obj:`bool`, optional
    :param can_manage_topics: :obj:`True`, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only.
    :type can_manage_topics: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['is_anonymous'] = res.get('is_anonymous')
        obj['can_manage_chat'] = res.get('can_manage_chat')
        obj['can_delete_messages'] = res.get('can_delete_messages')
        obj['can_manage_video_chats'] = res.get('can_manage_video_chats')
        obj['can_restrict_members'] = res.get('can_restrict_members')
        obj['can_promote_members'] = res.get('can_promote_members')
        obj['can_change_info'] = res.get('can_change_info')
        obj['can_invite_users'] = res.get('can_invite_users')
        obj['can_post_stories'] = res.get('can_post_stories')
        obj['can_edit_stories'] = res.get('can_edit_stories')
        obj['can_delete_stories'] = res.get('can_delete_stories')
        obj['can_post_messages'] = res.get('can_post_messages')
        obj['can_edit_messages'] = res.get('can_edit_messages')
        obj['can_pin_messages'] = res.get('can_pin_messages')
        obj['can_manage_topics'] = res.get('can_manage_topics')
        return cls(**obj)

    def __init__(
        self,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_stories: bool,
        can_edit_stories: bool,
        can_delete_stories: bool,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None
    ):
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics


class ChatBackground(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatbackground

    This object represents a chat background.

    :param type: Type of the background.
    :type type: :obj:`~apitele.types.BackgroundType`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['type'] = _dese_background_type(res.get('type'))
        return cls(**obj)

    def __init__(
        self,
        type: BackgroundType
    ):
        self.type = type


class ChatBoost(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboost

    This object contains information about a chat boost.

    :param boost_id: Unique identifier of the boost.
    :type boost_id: :obj:`str`
    :param add_date: Point in time (Unix timestamp) when the chat was boosted.
    :type add_date: :obj:`int`
    :param expiration_date: Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged.
    :type expiration_date: :obj:`int`
    :param source: Source of the added boost.
    :type source: :obj:`~apitele.types.ChatBoostSource`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['boost_id'] = res.get('boost_id')
        obj['add_date'] = res.get('add_date')
        obj['expiration_date'] = res.get('expiration_date')
        obj['source'] = _dese_chat_boost_source(res.get('source'))
        return cls(**obj)

    def __init__(
        self,
        boost_id: str,
        add_date: int,
        expiration_date: int,
        source: ChatBoostSource
    ):
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source


class ChatBoostAdded(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostadded

    This object represents a service message about a user boosting a chat.

    :param boost_count: Number of boosts added by the user.
    :type boost_count: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['boost_count'] = res.get('boost_count')
        return cls(**obj)

    def __init__(
        self,
        boost_count: int
    ):
        self.boost_count = boost_count


class ChatBoostRemoved(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostremoved

    This object represents a boost removed from a chat.

    :param chat: Chat which was boosted.
    :type chat: :obj:`~apitele.types.Chat`
    :param boost_id: Unique identifier of the boost.
    :type boost_id: :obj:`str`
    :param remove_date: Point in time (Unix timestamp) when the boost was removed.
    :type remove_date: :obj:`int`
    :param source: Source of the removed boost.
    :type source: :obj:`~apitele.types.ChatBoostSource`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['boost_id'] = res.get('boost_id')
        obj['remove_date'] = res.get('remove_date')
        obj['source'] = _dese_chat_boost_source(res.get('source'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        boost_id: str,
        remove_date: int,
        source: ChatBoostSource
    ):
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source


class ChatBoostSourceGiftCode(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostsourcegiftcode

    The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such
    code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

    :param user: User for which the gift code was created.
    :type user: :obj:`~apitele.types.User`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        return cls(**obj)

    def __init__(
        self,
        user: User
    ):
        self.source = DEFAULT_CHAT_BOOST_SOURCE_GIFT_CODE
        self.user = user


class ChatBoostSourceGiveaway(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostsourcegiveaway

    The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway.
    This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription
    for Telegram Premium giveaways and *prize_star_count* / 500 times for one year for Telegram Star giveaways.

    :param giveaway_message_id: Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.
    :type giveaway_message_id: :obj:`int`
    :param user: User that won the prize in the giveaway if any.
    :type user: :obj:`~apitele.types.User`, optional
    :param prize_star_count: The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.
    :type prize_star_count: :obj:`int`, optional
    :param is_unclaimed: :obj:`True`, if the giveaway was completed, but there was no user to win the prize.
    :type is_unclaimed: :obj:`True`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['giveaway_message_id'] = res.get('giveaway_message_id')
        obj['user'] = User._dese(res.get('user'))
        obj['prize_star_count'] = res.get('prize_star_count')
        obj['is_unclaimed'] = res.get('is_unclaimed')
        return cls(**obj)

    def __init__(
        self,
        giveaway_message_id: int,
        user: Optional[User] = None,
        prize_star_count: Optional[int] = None,
        is_unclaimed: Optional[Literal[True]] = None
    ):
        self.source = DEFAULT_CHAT_BOOST_SOURCE_GIVEAWAY
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.prize_star_count = prize_star_count
        self.is_unclaimed = is_unclaimed


class ChatBoostSourcePremium(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostsourcepremium

    The boost was obtained by subscribing to Telegram Premium or
    by gifting a Telegram Premium subscription to another user.

    :param user: User that boosted the chat.
    :type user: :obj:`~apitele.types.User`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        return cls(**obj)

    def __init__(
        self,
        user: User
    ):
        self.source = DEFAULT_CHAT_BOOST_SOURCE_PREMIUM
        self.user = user


class ChatBoostUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostupdated

    This object represents a boost added to a chat or changed.

    :param chat: Chat which was boosted.
    :type chat: :obj:`~apitele.types.Chat`
    :param boost: Information about the chat boost.
    :type boost: :obj:`~apitele.types.ChatBoost`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['boost'] = ChatBoost._dese(res.get('boost'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        boost: ChatBoost
    ):
        self.chat = chat
        self.boost = boost


class ChatFullInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatfullinfo

    This object contains full information about a chat.

    :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`
    :param type: Type of the chat, can be either “private”, “group”, “supergroup” or “channel”.
    :type type: :obj:`str`
    :param accent_color_id: Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See `accent colors <https://core.telegram.org/bots/api#accent-colors>`_ for more details.
    :type accent_color_id: :obj:`int`
    :param max_reaction_count: The maximum number of reactions that can be set on a message in the chat.
    :type max_reaction_count: :obj:`int`
    :param accepted_gift_types: Information about types of gifts that are accepted by the chat or by the corresponding user for private chats.
    :type accepted_gift_types: :obj:`~apitele.types.AcceptedGiftTypes`
    :param title: Title, for supergroups, channels and group chats.
    :type title: :obj:`str`, optional
    :param username: Username, for private chats, supergroups and channels if available.
    :type username: :obj:`str`, optional
    :param first_name: First name of the other party in a private chat.
    :type first_name: :obj:`str`, optional
    :param last_name: Last name of the other party in a private chat.
    :type last_name: :obj:`str`, optional
    :param is_forum: :obj:`True`, if the supergroup chat is a forum (has `topics <https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups>`_ enabled).
    :type is_forum: :obj:`True`, optional
    :param photo: Chat photo.
    :type photo: :obj:`~apitele.types.ChatPhoto`, optional
    :param active_usernames: If non-empty, the list of all `active chat usernames <https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames>`_; for private chats, supergroups and channels.
    :type active_usernames: :obj:`list` of :obj:`str`, optional
    :param birthdate: For private chats, the date of birth of the user.
    :type birthdate: :obj:`~apitele.types.Birthdate`, optional
    :param business_intro: For private chats with business accounts, the intro of the business.
    :type business_intro: :obj:`~apitele.types.BusinessIntro`, optional
    :param business_location: For private chats with business accounts, the location of the business.
    :type business_location: :obj:`~apitele.types.BusinessLocation`, optional
    :param business_opening_hours: For private chats with business accounts, the opening hours of the business.
    :type business_opening_hours: :obj:`~apitele.types.BusinessOpeningHours`, optional
    :param personal_chat: For private chats, the personal channel of the user.
    :type personal_chat: :obj:`~apitele.types.Chat`, optional
    :param available_reactions: List of available reactions allowed in the chat. If omitted, then all :obj:`emoji reactions <apitele.types.ReactionTypeEmoji>` are allowed.
    :type available_reactions: :obj:`list` of :obj:`~apitele.types.ReactionType`, optional
    :param background_custom_emoji_id: Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background.
    :type background_custom_emoji_id: :obj:`str`, optional
    :param profile_accent_color_id: Identifier of the accent color for the chat's profile background. See `profile accent colors <https://core.telegram.org/bots/api#profile-accent-colors>`_ for more details.
    :type profile_accent_color_id: :obj:`int`, optional
    :param profile_background_custom_emoji_id: Custom emoji identifier of the emoji chosen by the chat for its profile background.
    :type profile_background_custom_emoji_id: :obj:`str`, optional
    :param emoji_status_custom_emoji_id: Custom emoji identifier of the emoji status of the chat or the other party in a private chat.
    :type emoji_status_custom_emoji_id: :obj:`str`, optional
    :param emoji_status_expiration_date: Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any.
    :type emoji_status_expiration_date: :obj:`int`, optional
    :param bio: Bio of the other party in a private chat.
    :type bio: :obj:`str`, optional
    :param has_private_forwards: :obj:`True`, if privacy settings of the other party in the private chat allows to use ``tg://user?id=<user_id>`` links only in chats with the user.
    :type has_private_forwards: :obj:`True`, optional
    :param has_restricted_voice_and_video_messages: :obj:`True`, if the privacy settings of the other party restrict sending voice and video note messages in the private chat.
    :type has_restricted_voice_and_video_messages: :obj:`True`, optional
    :param join_to_send_messages: :obj:`True`, if users need to join the supergroup before they can send messages.
    :type join_to_send_messages: :obj:`True`, optional
    :param join_by_request: :obj:`True`, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators.
    :type join_by_request: :obj:`True`, optional
    :param description: Description, for groups, supergroups and channel chats.
    :type description: :obj:`str`, optional
    :param invite_link: Primary invite link, for groups, supergroups and channel chats.
    :type invite_link: :obj:`str`, optional
    :param pinned_message: The most recent pinned message (by sending date).
    :type pinned_message: :obj:`~apitele.types.Message`, optional
    :param can_send_paid_media: :obj:`True`, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.
    :type can_send_paid_media: :obj:`True`, optional
    :param permissions: Default chat member permissions, for groups and supergroups.
    :type permissions: :obj:`~apitele.types.ChatPermissions`, optional
    :param slow_mode_delay: For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds.
    :type slow_mode_delay: :obj:`int`, optional
    :param unrestrict_boost_count: For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions.
    :type unrestrict_boost_count: :obj:`int`, optional
    :param message_auto_delete_time: The time after which all messages sent to the chat will be automatically deleted; in seconds.
    :type message_auto_delete_time: :obj:`int`, optional
    :param has_aggressive_anti_spam_enabled: :obj:`True`, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.
    :type has_aggressive_anti_spam_enabled: :obj:`True`, optional
    :param has_hidden_members: :obj:`True`, if non-administrators can only get the list of bots and administrators in the chat.
    :type has_hidden_members: :obj:`True`, optional
    :param has_protected_content: :obj:`True`, if messages from the chat can't be forwarded to other chats.
    :type has_protected_content: :obj:`True`, optional
    :param has_visible_history: :obj:`True`, if new chat members will have access to old messages; available only to chat administrators.
    :type has_visible_history: :obj:`True`, optional
    :param sticker_set_name: For supergroups, name of the group sticker set.
    :type sticker_set_name: :obj:`str`, optional
    :param can_set_sticker_set: :obj:`True`, if the bot can change the group sticker set.
    :type can_set_sticker_set: :obj:`True`, optional
    :param custom_emoji_sticker_set_name: For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.
    :type custom_emoji_sticker_set_name: :obj:`str`, optional
    :param linked_chat_id: Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type linked_chat_id: :obj:`int`, optional
    :param location: For supergroups, the location to which the supergroup is connected.
    :type location: :obj:`~apitele.types.ChatLocation`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['type'] = res.get('type')
        obj['accent_color_id'] = res.get('accent_color_id')
        obj['max_reaction_count'] = res.get('max_reaction_count')
        obj['accepted_gift_types'] = AcceptedGiftTypes._dese(res.get('accepted_gift_types'))
        obj['title'] = res.get('title')
        obj['username'] = res.get('username')
        obj['first_name'] = res.get('first_name')
        obj['last_name'] = res.get('last_name')
        obj['is_forum'] = res.get('is_forum')
        obj['photo'] = ChatPhoto._dese(res.get('photo'))
        obj['active_usernames'] = res.get('active_usernames')
        obj['birthdate'] = Birthdate._dese(res.get('birthdate'))
        obj['business_intro'] = BusinessIntro._dese(res.get('business_intro'))
        obj['business_location'] = BusinessLocation._dese(res.get('business_location'))
        obj['business_opening_hours'] = BusinessOpeningHours._dese(res.get('business_opening_hours'))
        obj['personal_chat'] = Chat._dese(res.get('personal_chat'))
        obj['available_reactions'] = [_dese_reaction_type(kwargs) for kwargs in res.get('available_reactions')] if 'available_reactions' in res else None
        obj['background_custom_emoji_id'] = res.get('background_custom_emoji_id')
        obj['profile_accent_color_id'] = res.get('profile_accent_color_id')
        obj['profile_background_custom_emoji_id'] = res.get('profile_background_custom_emoji_id')
        obj['emoji_status_custom_emoji_id'] = res.get('emoji_status_custom_emoji_id')
        obj['emoji_status_expiration_date'] = res.get('emoji_status_expiration_date')
        obj['bio'] = res.get('bio')
        obj['has_private_forwards'] = res.get('has_private_forwards')
        obj['has_restricted_voice_and_video_messages'] = res.get('has_restricted_voice_and_video_messages')
        obj['join_to_send_messages'] = res.get('join_to_send_messages')
        obj['join_by_request'] = res.get('join_by_request')
        obj['description'] = res.get('description')
        obj['invite_link'] = res.get('invite_link')
        obj['pinned_message'] = Message._dese(res.get('pinned_message'))
        obj['permissions'] = ChatPermissions._dese(res.get('permissions'))
        obj['can_send_paid_media'] = res.get('can_send_paid_media')
        obj['slow_mode_delay'] = res.get('slow_mode_delay')
        obj['unrestrict_boost_count'] = res.get('unrestrict_boost_count')
        obj['message_auto_delete_time'] = res.get('message_auto_delete_time')
        obj['has_aggressive_anti_spam_enabled'] = res.get('has_aggressive_anti_spam_enabled')
        obj['has_hidden_members'] = res.get('has_hidden_members')
        obj['has_protected_content'] = res.get('has_protected_content')
        obj['has_visible_history'] = res.get('has_visible_history')
        obj['sticker_set_name'] = res.get('sticker_set_name')
        obj['can_set_sticker_set'] = res.get('can_set_sticker_set')
        obj['custom_emoji_sticker_set_name'] = res.get('custom_emoji_sticker_set_name')
        obj['linked_chat_id'] = res.get('linked_chat_id')
        obj['location'] = ChatLocation._dese(res.get('location'))
        return cls(**obj)

    def __init__(
        self,
        id: int,
        type: str,
        accent_color_id: int,
        max_reaction_count: int,
        accepted_gift_types: AcceptedGiftTypes,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        is_forum: Optional[Literal[True]] = None,
        photo: Optional[ChatPhoto] = None,
        active_usernames: Optional[list[str]] = None,
        birthdate: Optional[Birthdate] = None,
        business_intro: Optional[BusinessIntro] = None,
        business_location: Optional[BusinessLocation] = None,
        business_opening_hours: Optional[BusinessOpeningHours] = None,
        personal_chat: Optional[Chat] = None,
        available_reactions: Optional[list[ReactionType]] = None,
        background_custom_emoji_id: Optional[str] = None,
        profile_accent_color_id: Optional[int] = None,
        profile_background_custom_emoji_id: Optional[str] = None,
        emoji_status_custom_emoji_id: Optional[str] = None,
        emoji_status_expiration_date: Optional[int] = None,
        bio: Optional[str] = None,
        has_private_forwards: Optional[Literal[True]] = None,
        has_restricted_voice_and_video_messages: Optional[Literal[True]] = None,
        join_to_send_messages: Optional[Literal[True]] = None,
        join_by_request: Optional[Literal[True]] = None,
        description: Optional[str] = None,
        invite_link: Optional[str] = None,
        pinned_message: Optional[Message] = None,
        permissions: Optional[ChatPermissions] = None,
        can_send_paid_media: Optional[Literal[True]] = None,
        slow_mode_delay: Optional[int] = None,
        unrestrict_boost_count: Optional[int] = None,
        message_auto_delete_time: Optional[int] = None,
        has_aggressive_anti_spam_enabled: Optional[Literal[True]] = None,
        has_hidden_members: Optional[Literal[True]] = None,
        has_protected_content: Optional[Literal[True]] = None,
        has_visible_history: Optional[Literal[True]] = None,
        sticker_set_name: Optional[str] = None,
        can_set_sticker_set: Optional[Literal[True]] = None,
        custom_emoji_sticker_set_name: Optional[str] = None,
        linked_chat_id: Optional[int] = None,
        location: Optional[ChatLocation] = None
    ):
        self.id = id
        self.type = type
        self.accent_color_id = accent_color_id
        self.max_reaction_count = max_reaction_count
        self.accepted_gift_types = accepted_gift_types
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.photo = photo
        self.active_usernames = active_usernames
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
        self.available_reactions = available_reactions
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.can_send_paid_media = can_send_paid_media
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location


class ChatInviteLink(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatinvitelink

    Represents an invite link for a chat.

    :param invite_link: The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.
    :type invite_link: :obj:`str`
    :param creator: Creator of the link.
    :type creator: :obj:`~apitele.types.User`
    :param creates_join_request: :obj:`True`, if users joining the chat via the link need to be approved by chat administrators.
    :type creates_join_request: :obj:`bool`
    :param is_primary: :obj:`True`, if the link is primary.
    :type is_primary: :obj:`bool`
    :param is_revoked: :obj:`True`, if the link is revoked.
    :type is_revoked: :obj:`bool`
    :param name: Invite link name.
    :type name: :obj:`str`, optional
    :param expire_date: Point in time (Unix timestamp) when the link will expire or has been expired.
    :type expire_date: :obj:`int`, optional
    :param member_limit: The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.
    :type member_limit: :obj:`int`, optional
    :param pending_join_request_count: Number of pending join requests created using this link.
    :type pending_join_request_count: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['invite_link'] = res.get('invite_link')
        obj['creator'] = User._dese(res.get('creator'))
        obj['creates_join_request'] = res.get('creates_join_request')
        obj['is_primary'] = res.get('is_primary')
        obj['is_revoked'] = res.get('is_revoked')
        obj['name'] = res.get('name')
        obj['expire_date'] = res.get('expire_date')
        obj['member_limit'] = res.get('member_limit')
        obj['pending_join_request_count'] = res.get('pending_join_request_count')
        return cls(**obj)

    def __init__(
        self,
        invite_link: str,
        creator: User,
        creates_join_request: bool,
        is_primary: bool,
        is_revoked: bool,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        pending_join_request_count: Optional[int] = None
    ):
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count


class ChatJoinRequest(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatjoinrequest

    Represents a join request sent to a chat.

    :param chat: Chat to which the request was sent.
    :type chat: :obj:`~apitele.types.Chat`
    :param from_user: User that sent the join request.
    :type from_user: :obj:`~apitele.types.User`
    :param user_chat_id: Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user.
    :type user_chat_id: :obj:`int`
    :param date: Date the request was sent in Unix time.
    :type date: :obj:`int`
    :param bio: Bio of the user.
    :type bio: :obj:`str`, optional
    :param invite_link: Chat invite link that was used by the user to send the join request.
    :type invite_link: :obj:`~apitele.types.ChatInviteLink`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['user_chat_id'] = res.get('user_chat_id')
        obj['date'] = res.get('date')
        obj['bio'] = res.get('bio')
        obj['invite_link'] = ChatInviteLink._dese(res.get('invite_link'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        from_user: User,
        user_chat_id: int,
        date: int,
        bio: Optional[str] = None,
        invite_link: Optional[ChatInviteLink] = None
    ):
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link


class ChatLocation(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatlocation

    Represents a location to which a chat is connected.

    :param location: The location to which the supergroup is connected. Can't be a live location.
    :type location: :obj:`~apitele.types.Location`
    :param address: Location address; 1-64 characters, as defined by the chat owner.
    :type address: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['location'] = Location._dese(res.get('location'))
        obj['address'] = res.get('address')
        return cls(**obj)

    def __init__(
        self,
        location: Location,
        address: str
    ):
        self.location = location
        self.address = address


class ChatMemberAdministrator(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmemberadministrator

    Represents a :obj:`chat member <apitele.types.ChatMember>` that has some additional privileges.

    :param user: Information about the user.
    :type user: :obj:`~apitele.types.User`
    :param can_be_edited: :obj:`True`, if the bot is allowed to edit administrator privileges of that user.
    :type can_be_edited: :obj:`bool`
    :param is_anonymous: :obj:`True`, if the user's presence in the chat is hidden.
    :type is_anonymous: :obj:`bool`
    :param can_manage_chat: :obj:`True`, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
    :type can_manage_chat: :obj:`bool`
    :param can_delete_messages: :obj:`True`, if the administrator can delete messages of other users.
    :type can_delete_messages: :obj:`bool`
    :param can_manage_video_chats: :obj:`True`, if the administrator can manage video chats.
    :type can_manage_video_chats: :obj:`bool`
    :param can_restrict_members: :obj:`True`, if the administrator can restrict, ban or unban chat members, or access supergroup statistics.
    :type can_restrict_members: :obj:`bool`
    :param can_promote_members: :obj:`True`, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user).
    :type can_promote_members: :obj:`bool`
    :param can_change_info: :obj:`True`, if the user is allowed to change the chat title, photo and other settings.
    :type can_change_info: :obj:`bool`
    :param can_invite_users: :obj:`True`, if the user is allowed to invite new users to the chat.
    :type can_invite_users: :obj:`bool`
    :param can_post_stories: :obj:`True`, if the administrator can post stories to the chat.
    :type can_post_stories: :obj:`bool`
    :param can_edit_stories: :obj:`True`, if the administrator can edit stories posted by other users.
    :type can_edit_stories: :obj:`bool`
    :param can_delete_stories: :obj:`True`, if the administrator can delete stories posted by other users.
    :type can_delete_stories: :obj:`bool`
    :param can_post_messages: :obj:`True`, if the administrator can post messages in the channel, or access channel statistics; for channels only.
    :type can_post_messages: :obj:`bool`, optional
    :param can_edit_messages: :obj:`True`, if the administrator can edit messages of other users and can pin messages; for channels only.
    :type can_edit_messages: :obj:`bool`, optional
    :param can_pin_messages: :obj:`True`, if the user is allowed to pin messages; for groups and supergroups only.
    :type can_pin_messages: :obj:`bool`, optional
    :param can_manage_topics: :obj:`True`, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only.
    :type can_manage_topics: :obj:`bool`, optional
    :param custom_title: Custom title for this user.
    :type custom_title: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        obj['can_be_edited'] = res.get('can_be_edited')
        obj['is_anonymous'] = res.get('is_anonymous')
        obj['can_manage_chat'] = res.get('can_manage_chat')
        obj['can_delete_messages'] = res.get('can_delete_messages')
        obj['can_manage_video_chats'] = res.get('can_manage_video_chats')
        obj['can_restrict_members'] = res.get('can_restrict_members')
        obj['can_promote_members'] = res.get('can_promote_members')
        obj['can_change_info'] = res.get('can_change_info')
        obj['can_invite_users'] = res.get('can_invite_users')
        obj['can_post_stories'] = res.get('can_post_stories')
        obj['can_edit_stories'] = res.get('can_edit_stories')
        obj['can_delete_stories'] = res.get('can_delete_stories')
        obj['can_post_messages'] = res.get('can_post_messages')
        obj['can_edit_messages'] = res.get('can_edit_messages')
        obj['can_pin_messages'] = res.get('can_pin_messages')
        obj['can_manage_topics'] = res.get('can_manage_topics')
        obj['custom_title'] = res.get('custom_title')
        return cls(**obj)

    def __init__(
        self,
        user: User,
        can_be_edited: bool,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_stories: bool,
        can_edit_stories: bool,
        can_delete_stories: bool,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        custom_title: Optional[str] = None
    ):
        self.status = DEFAULT_CHAT_MEMBER_ADMINISTRATOR
        self.user = user
        self.can_be_edited = can_be_edited
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.custom_title = custom_title


class ChatMemberBanned(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmemberbanned

    Represents a :obj:`chat member <apitele.types.ChatMember>` that was banned in the chat and can't return to the chat or view chat messages.

    :param user: Information about the user.
    :type user: :obj:`~apitele.types.User`
    :param until_date: Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever.
    :type until_date: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        obj['until_date'] = res.get('until_date')
        return cls(**obj)

    def __init__(
        self,
        user: User,
        until_date: int
    ):
        self.status = DEFAULT_CHAT_MEMBER_BANNED
        self.user = user
        self.until_date = until_date


class ChatMemberLeft(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmemberleft

    Represents a :obj:`chat member <apitele.types.ChatMember>` that isn't currently a member of the chat, but may join it themselves.

    :param user: Information about the user.
    :type user: :obj:`~apitele.types.User`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        return cls(**obj)

    def __init__(
        self,
        user: User
    ):
        self.status = DEFAULT_CHAT_MEMBER_LEFT
        self.user = user


class ChatMemberMember(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmembermember

    Represents a :obj:`chat member <apitele.types.ChatMember>` that has no additional privileges or restrictions.

    :param user: Information about the user.
    :type user: :obj:`~apitele.types.User`
    :param until_date: Date when the user's subscription will expire; Unix time.
    :type until_date: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        obj['until_date'] = res.get('until_date')
        return cls(**obj)

    def __init__(
        self,
        user: User,
        until_date: Optional[int] = None
    ):
        self.status = DEFAULT_CHAT_MEMBER_MEMBER
        self.user = user
        self.until_date = until_date


class ChatMemberOwner(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmemberowner

    Represents a :obj:`chat member <apitele.types.ChatMember>` that owns the chat and has all administrator privileges.

    :param user: Information about the user.
    :type user: :obj:`~apitele.types.User`
    :param is_anonymous: :obj:`True`, if the user's presence in the chat is hidden.
    :type is_anonymous: :obj:`bool`
    :param custom_title: Custom title for this user.
    :type custom_title: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        obj['is_anonymous'] = res.get('is_anonymous')
        obj['custom_title'] = res.get('custom_title')
        return cls(**obj)

    def __init__(
        self,
        user: User,
        is_anonymous: bool,
        custom_title: Optional[str] = None
    ):
        self.status = DEFAULT_CHAT_MEMBER_OWNER
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title


class ChatMemberRestricted(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmemberrestricted

    Represents a :obj:`chat member <apitele.types.ChatMember>` that is under certain restrictions in the chat. Supergroups only.

    :param user: Information about the user.
    :type user: :obj:`~apitele.types.User`
    :param is_member: :obj:`True`, if the user is a member of the chat at the moment of the request.
    :type is_member: :obj:`bool`
    :param can_send_messages: :obj:`True`, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues.
    :type can_send_messages: :obj:`bool`
    :param can_send_audios: :obj:`True`, if the user is allowed to send audios.
    :type can_send_audios: :obj:`bool`
    :param can_send_documents: :obj:`True`, if the user is allowed to send documents.
    :type can_send_documents: :obj:`bool`
    :param can_send_photos: :obj:`True`, if the user is allowed to send photos.
    :type can_send_photos: :obj:`bool`
    :param can_send_videos: :obj:`True`, if the user is allowed to send videos.
    :type can_send_videos: :obj:`bool`
    :param can_send_video_notes: :obj:`True`, if the user is allowed to send video notes.
    :type can_send_video_notes: :obj:`bool`
    :param can_send_voice_notes: :obj:`True`, if the user is allowed to send voice notes.
    :type can_send_voice_notes: :obj:`bool`
    :param can_send_polls: :obj:`True`, if the user is allowed to send polls.
    :type can_send_polls: :obj:`bool`
    :param can_send_other_messages: :obj:`True`, if the user is allowed to send animations, games, stickers and use inline bots.
    :type can_send_other_messages: :obj:`bool`
    :param can_add_web_page_previews: :obj:`True`, if the user is allowed to add web page previews to their messages.
    :type can_add_web_page_previews: :obj:`bool`
    :param can_change_info: :obj:`True`, if the user is allowed to change the chat title, photo and other settings.
    :type can_change_info: :obj:`bool`
    :param can_invite_users: :obj:`True`, if the user is allowed to invite new users to the chat.
    :type can_invite_users: :obj:`bool`
    :param can_pin_messages: :obj:`True`, if the user is allowed to pin messages.
    :type can_pin_messages: :obj:`bool`
    :param can_manage_topics: :obj:`True`, if the user is allowed to create forum topics.
    :type can_manage_topics: :obj:`bool`
    :param until_date: Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever.
    :type until_date: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user'] = User._dese(res.get('user'))
        obj['is_member'] = res.get('is_member')
        obj['can_send_messages'] = res.get('can_send_messages')
        obj['can_send_audios'] = res.get('can_send_audios')
        obj['can_send_documents'] = res.get('can_send_documents')
        obj['can_send_photos'] = res.get('can_send_photos')
        obj['can_send_videos'] = res.get('can_send_videos')
        obj['can_send_video_notes'] = res.get('can_send_video_notes')
        obj['can_send_voice_notes'] = res.get('can_send_voice_notes')
        obj['can_send_polls'] = res.get('can_send_polls')
        obj['can_send_other_messages'] = res.get('can_send_other_messages')
        obj['can_add_web_page_previews'] = res.get('can_add_web_page_previews')
        obj['can_change_info'] = res.get('can_change_info')
        obj['can_invite_users'] = res.get('can_invite_users')
        obj['can_pin_messages'] = res.get('can_pin_messages')
        obj['can_manage_topics'] = res.get('can_manage_topics')
        obj['until_date'] = res.get('until_date')
        return cls(**obj)

    def __init__(
        self,
        user: User,
        is_member: bool,
        can_send_messages: bool,
        can_send_audios: bool,
        can_send_documents: bool,
        can_send_photos: bool,
        can_send_videos: bool,
        can_send_video_notes: bool,
        can_send_voice_notes: bool,
        can_send_polls: bool,
        can_send_other_messages: bool,
        can_add_web_page_previews: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_pin_messages: bool,
        can_manage_topics: bool,
        until_date: int
    ):
        self.status = DEFAULT_CHAT_MEMBER_RESTRICTED
        self.user = user
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.until_date = until_date


class ChatMemberUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmemberupdated

    This object represents changes in the status of a chat member.

    :param chat: Chat the user belongs to.
    :type chat: :obj:`~apitele.types.Chat`
    :param from_user: Performer of the action, which resulted in the change.
    :type from_user: :obj:`~apitele.types.User`
    :param date: Date the change was done in Unix time.
    :type date: :obj:`int`
    :param old_chat_member: Previous information about the chat member.
    :type old_chat_member: :obj:`~apitele.types.ChatMember`
    :param new_chat_member: New information about the chat member.
    :type new_chat_member: :obj:`~apitele.types.ChatMember`
    :param invite_link: Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
    :type invite_link: :obj:`~apitele.types.ChatInviteLink`, optional
    :param via_join_request: :obj:`True`, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator.
    :type via_join_request: :obj:`bool`, optional
    :param via_chat_folder_invite_link: :obj:`True`, if the user joined the chat via a chat folder invite link.
    :type via_chat_folder_invite_link: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['date'] = res.get('date')
        obj['old_chat_member'] = _dese_chat_member(res.get('old_chat_member'))
        obj['new_chat_member'] = _dese_chat_member(res.get('new_chat_member'))
        obj['invite_link'] = ChatInviteLink._dese(res.get('invite_link'))
        obj['via_join_request'] = res.get('via_join_request')
        obj['via_chat_folder_invite_link'] = res.get('via_chat_folder_invite_link')
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        from_user: User,
        date: int,
        old_chat_member: ChatMember,
        new_chat_member: ChatMember,
        invite_link: Optional[ChatInviteLink] = None,
        via_join_request: Optional[bool] = None,
        via_chat_folder_invite_link: Optional[bool] = None
    ):
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_join_request = via_join_request
        self.via_chat_folder_invite_link = via_chat_folder_invite_link


class ChatPermissions(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatpermissions

    Describes actions that a non-administrator user is allowed to take in a chat.

    :param can_send_messages: :obj:`True`, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues.
    :type can_send_messages: :obj:`bool`, optional
    :param can_send_audios: :obj:`True`, if the user is allowed to send audios.
    :type can_send_audios: :obj:`bool`, optional
    :param can_send_documents: :obj:`True`, if the user is allowed to send documents.
    :type can_send_documents: :obj:`bool`, optional
    :param can_send_photos: :obj:`True`, if the user is allowed to send photos.
    :type can_send_photos: :obj:`bool`, optional
    :param can_send_videos: :obj:`True`, if the user is allowed to send videos.
    :type can_send_videos: :obj:`bool`, optional
    :param can_send_video_notes: :obj:`True`, if the user is allowed to send video notes.
    :type can_send_video_notes: :obj:`bool`, optional
    :param can_send_voice_notes: :obj:`True`, if the user is allowed to send voice notes.
    :type can_send_voice_notes: :obj:`bool`, optional
    :param can_send_polls: :obj:`True`, if the user is allowed to send polls.
    :type can_send_polls: :obj:`bool`, optional
    :param can_send_other_messages: :obj:`True`, if the user is allowed to send animations, games, stickers and use inline bots.
    :type can_send_other_messages: :obj:`bool`, optional
    :param can_add_web_page_previews: :obj:`True`, if the user is allowed to add web page previews to their messages.
    :type can_add_web_page_previews: :obj:`bool`, optional
    :param can_change_info: :obj:`True`, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups.
    :type can_change_info: :obj:`bool`, optional
    :param can_invite_users: :obj:`True`, if the user is allowed to invite new users to the chat.
    :type can_invite_users: :obj:`bool`, optional
    :param can_pin_messages: :obj:`True`, if the user is allowed to pin messages. Ignored in public supergroups.
    :type can_pin_messages: :obj:`bool`, optional
    :param can_manage_topics: :obj:`True`, if the user is allowed to create forum topics. If omitted defaults to the value of *can_pin_messages*.
    :type can_manage_topics: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['can_send_messages'] = res.get('can_send_messages')
        obj['can_send_audios'] = res.get('can_send_audios')
        obj['can_send_documents'] = res.get('can_send_documents')
        obj['can_send_photos'] = res.get('can_send_photos')
        obj['can_send_videos'] = res.get('can_send_videos')
        obj['can_send_video_notes'] = res.get('can_send_video_notes')
        obj['can_send_voice_notes'] = res.get('can_send_voice_notes')
        obj['can_send_polls'] = res.get('can_send_polls')
        obj['can_send_other_messages'] = res.get('can_send_other_messages')
        obj['can_add_web_page_previews'] = res.get('can_add_web_page_previews')
        obj['can_change_info'] = res.get('can_change_info')
        obj['can_invite_users'] = res.get('can_invite_users')
        obj['can_pin_messages'] = res.get('can_pin_messages')
        obj['can_manage_topics'] = res.get('can_manage_topics')
        return cls(**obj)

    def __init__(
        self,
        can_send_messages: Optional[bool] = None,
        can_send_audios: Optional[bool] = None,
        can_send_documents: Optional[bool] = None,
        can_send_photos: Optional[bool] = None,
        can_send_videos: Optional[bool] = None,
        can_send_video_notes: Optional[bool] = None,
        can_send_voice_notes: Optional[bool] = None,
        can_send_polls: Optional[bool] = None,
        can_send_other_messages: Optional[bool] = None,
        can_add_web_page_previews: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None
    ):
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics


class ChatPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatphoto

    This object represents a chat photo.

    :param small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    :type small_file_id: :obj:`str`
    :param small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type small_file_unique_id: :obj:`str`
    :param big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    :type big_file_id: :obj:`str`
    :param big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type big_file_unique_id: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['small_file_id'] = res.get('small_file_id')
        obj['small_file_unique_id'] = res.get('small_file_unique_id')
        obj['big_file_id'] = res.get('big_file_id')
        obj['big_file_unique_id'] = res.get('big_file_unique_id')
        return cls(**obj)

    def __init__(
        self,
        small_file_id: str,
        small_file_unique_id: str,
        big_file_id: str,
        big_file_unique_id: str
    ):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id


class ChatShared(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatshared

    This object contains information about the chat whose identifier was shared
    with the bot using a :obj:`~apitele.types.KeyboardButtonRequestChat` button.

    :param request_id: Identifier of the request.
    :type request_id: :obj:`int`
    :param chat_id: Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means.
    :type chat_id: :obj:`int`
    :param title: Title of the chat, if the title was requested by the bot.
    :type title: :obj:`str`, optional
    :param username: Username of the chat, if the username was requested by the bot and available.
    :type username: :obj:`str`, optional
    :param photo: Available sizes of the chat photo, if the photo was requested by the bot.
    :type photo: :obj:`list` of :obj:`~apitele.types.PhotoSize`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['request_id'] = res.get('request_id')
        obj['chat_id'] = res.get('chat_id')
        obj['title'] = res.get('title')
        obj['username'] = res.get('username')
        obj['photo'] = [PhotoSize._dese(kwargs) for kwargs in res.get('photo')] if 'photo' in res else None
        return cls(**obj)

    def __init__(
        self,
        request_id: int,
        chat_id: int,
        title: Optional[str] = None,
        username: Optional[str] = None,
        photo: Optional[list[PhotoSize]] = None,
    ):
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo


class ChosenInlineResult(TelegramType):
    '''
    https://core.telegram.org/bots/api#choseninlineresult

    Represents a :obj:`result <apitele.types.InlineQueryResult>` of an
    inline query that was chosen by the user and sent to their chat partner.

    **Note**: It is necessary to enable
    `inline feedback <https://core.telegram.org/bots/inline#collecting-feedback>`_ via
    `@BotFather <https://t.me/botfather>`_ in order to receive these objects in updates.

    :param result_id: The unique identifier for the result that was chosen.
    :type result_id: :obj:`str`
    :param from_user: The user that chose the result.
    :type from_user: :obj:`~apitele.types.User`
    :param query: The query that was used to obtain the result.
    :type query: :obj:`str`
    :param location: Sender location, only for bots that require user location.
    :type location: :obj:`~apitele.types.Location`, optional
    :param inline_message_id: Identifier of the sent inline message. Available only if there is an :obj:`inline keyboard <apitele.types.InlineKeyboardMarkup>` attached to the message. Will be also received in :obj:`callback queries <apitele.types.CallbackQuery>` and can be used to `edit <https://core.telegram.org/bots/api#updating-messages>`_ the message.
    :type inline_message_id: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['result_id'] = res.get('result_id')
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['query'] = res.get('query')
        obj['location'] = Location._dese(res.get('location'))
        obj['inline_message_id'] = res.get('inline_message_id')
        return cls(**obj)

    def __init__(
        self,
        result_id: str,
        from_user: User,
        query: str,
        location: Optional[Location] = None,
        inline_message_id: Optional[str] = None
    ):
        self.result_id = result_id
        self.from_user = from_user
        self.query = query
        self.location = location
        self.inline_message_id = inline_message_id


class Contact(TelegramType):
    '''
    https://core.telegram.org/bots/api#contact

    This object represents a phone contact.

    :param phone_number: Contact's phone number.
    :type phone_number: :obj:`str`
    :param first_name: Contact's first name.
    :type first_name: :obj:`str`
    :param last_name: Contact's last name.
    :type last_name: :obj:`str`, optional
    :param user_id: Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type user_id: :obj:`int`, optional
    :param vcard: Additional data about the contact in the form of a `vCard <https://en.wikipedia.org/wiki/VCard>`_.
    :type vcard: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['phone_number'] = res.get('phone_number')
        obj['first_name'] = res.get('first_name')
        obj['last_name'] = res.get('last_name')
        obj['user_id'] = res.get('user_id')
        obj['vcard'] = res.get('vcard')
        return cls(**obj)

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        user_id: Optional[int] = None,
        vcard: Optional[str] = None
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard


class CopyTextButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#copytextbutton

    This object represents an inline keyboard button that copies specified text to the clipboard.

    :param text: The text to be copied to the clipboard; 1-256 characters.
    :type text: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['text'] = res.get('text')
        return cls(**obj)

    def __init__(
        self,
        text: str
    ):
        self.text = text


class Dice(TelegramType):
    '''
    https://core.telegram.org/bots/api#dice

    This object represents an animated emoji that displays a random value.

    :param emoji: Emoji on which the dice throw animation is based.
    :type emoji: :obj:`str`
    :param value: Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base emoji, 1-64 for “🎰” base emoji.
    :type value: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['emoji'] = res.get('emoji')
        obj['value'] = res.get('value')
        return cls(**obj)

    def __init__(
        self,
        emoji: str,
        value: int
    ):
        self.emoji = emoji
        self.value = value


class Document(TelegramType):
    '''
    https://core.telegram.org/bots/api#document

    This object represents a general file (as opposed to :obj:`photos <apitele.types.PhotoSize>`,
    :obj:`voice messages <apitele.types.Voice>` and :obj:`audio files <apitele.types.Audio>`).

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param thumbnail: Document thumbnail as defined by sender.
    :type thumbnail: :obj:`~apitele.types.PhotoSize`, optional
    :param file_name: Original filename as defined by sender.
    :type file_name: :obj:`str`, optional
    :param mime_type: MIME type of the file as defined by sender.
    :type mime_type: :obj:`str`, optional
    :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['thumbnail'] = PhotoSize._dese(res.get('thumbnail'))
        obj['file_name'] = res.get('file_name')
        obj['mime_type'] = res.get('mime_type')
        obj['file_size'] = res.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        thumbnail: Optional[PhotoSize] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class EncryptedCredentials(TelegramType):
    '''
    https://core.telegram.org/bots/api#encryptedcredentials

    Describes data required for decrypting and
    authenticating :obj:`~apitele.types.EncryptedPassportElement`. See the
    `Telegram Passport Documentation <https://core.telegram.org/passport#receiving-information>`_
    for a complete description of the data decryption and authentication processes.

    :param data: Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for :obj:`~apitele.types.EncryptedPassportElement` decryption and authentication.
    :type data: :obj:`str`
    :param hash: Base64-encoded data hash for data authentication.
    :type hash: :obj:`str`
    :param secret: Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption.
    :type secret: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['data'] = res.get('data')
        obj['hash'] = res.get('hash')
        obj['secret'] = res.get('secret')
        return cls(**obj)

    def __init__(
        self,
        data: str,
        hash: str,
        secret: str
    ):
        self.data = data
        self.hash = hash
        self.secret = secret


class EncryptedPassportElement(TelegramType):
    '''
    https://core.telegram.org/bots/api#encryptedpassportelement

    Describes documents or other Telegram Passport elements shared with the bot by the user.

    :param type: Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
    :type type: :obj:`str`
    :param hash: Base64-encoded element hash for using in :obj:`~apitele.types.PassportElementErrorUnspecified`.
    :type hash: :obj:`str`
    :param data: Base64-encoded encrypted Telegram Passport element data provided by the user; available only for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying :obj:`~apitele.types.EncryptedCredentials`.
    :type data: :obj:`str`, optional
    :param phone_number: User's verified phone number; available only for “phone_number” type.
    :type phone_number: :obj:`str`, optional
    :param email: User's verified email address; available only for “email” type.
    :type email: :obj:`str`, optional
    :param files: Array of encrypted files with documents provided by the user; available only for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying :obj:`~apitele.types.EncryptedCredentials`.
    :type files: :obj:`list` of :obj:`~apitele.types.PassportFile`, optional
    :param front_side: Encrypted file with the front side of the document, provided by the user; available only for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying :obj:`~apitele.types.EncryptedCredentials`.
    :type front_side: :obj:`~apitele.types.PassportFile`, optional
    :param reverse_side: Encrypted file with the reverse side of the document, provided by the user; available only for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying :obj:`~apitele.types.EncryptedCredentials`.
    :type reverse_side: :obj:`~apitele.types.PassportFile`, optional
    :param selfie: Encrypted file with the selfie of the user holding a document, provided by the user; available if requested for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying :obj:`~apitele.types.EncryptedCredentials`.
    :type selfie: :obj:`~apitele.types.PassportFile`, optional
    :param translation: Array of encrypted files with translated versions of documents provided by the user; available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying :obj:`~apitele.types.EncryptedCredentials`.
    :type translation: :obj:`list` of :obj:`~apitele.types.PassportFile`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['type'] = res.get('type')
        obj['hash'] = res.get('hash')
        obj['data'] = res.get('data')
        obj['phone_number'] = res.get('phone_number')
        obj['email'] = res.get('email')
        obj['files'] = [PassportFile._dese(kwargs) for kwargs in res.get('files')] if 'files' in res else None
        obj['front_side'] = PassportFile._dese(res.get('front_side'))
        obj['reverse_side'] = PassportFile._dese(res.get('reverse_side'))
        obj['selfie'] = PassportFile._dese(res.get('selfie'))
        obj['translation'] = [PassportFile._dese(kwargs) for kwargs in res.get('translation')] if 'translation' in res else None
        return cls(**obj)

    def __init__(
        self,
        type: str,
        hash: str,
        data: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        files: Optional[list[PassportFile]] = None,
        front_side: Optional[PassportFile] = None,
        reverse_side: Optional[PassportFile] = None,
        selfie: Optional[PassportFile] = None,
        translation: Optional[list[PassportFile]] = None
    ):
        self.type = type
        self.hash = hash
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation


class ExternalReplyInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#externalreplyinfo

    This object contains information about a message that is
    being replied to, which may come from another chat or forum topic.

    :param origin: Origin of the message replied to by the given message.
    :type origin: :obj:`~apitele.types.MessageOrigin`
    :param chat: Chat the original message belongs to. Available only if the chat is a supergroup or a channel.
    :type chat: :obj:`~apitele.types.Chat`, optional
    :param message_id: Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.
    :type message_id: :obj:`int`, optional
    :param link_preview_options: Options used for link preview generation for the original message, if it is a text message.
    :type link_preview_options: :obj:`~apitele.types.LinkPreviewOptions`, optional
    :param animation: Message is an animation, information about the animation.
    :type animation: :obj:`~apitele.types.Animation`, optional
    :param audio: Message is an audio file, information about the file.
    :type audio: :obj:`~apitele.types.Audio`, optional
    :param document: Message is a general file, information about the file.
    :type document: :obj:`~apitele.types.Document`, optional
    :param paid_media: Message contains paid media; information about the paid media.
    :type paid_media: :obj:`~apitele.types.PaidMediaInfo`, optional
    :param photo: Message is a photo, available sizes of the photo.
    :type photo: :obj:`list` of :obj:`~apitele.types.PhotoSize`, optional
    :param sticker: Message is a sticker, information about the sticker.
    :type sticker: :obj:`~apitele.types.Sticker`, optional
    :param story: Message is a forwarded story.
    :type story: :obj:`~apitele.types.Story`, optional
    :param video: Message is a video, information about the video.
    :type video: :obj:`~apitele.types.Video`, optional
    :param video_note: Message is a `video note <https://telegram.org/blog/video-messages-and-telescope>`_, information about the video message.
    :type video_note: :obj:`~apitele.types.VideoNote`, optional
    :param voice: Message is a voice message, information about the file.
    :type voice: :obj:`~apitele.types.Voice`, optional
    :param has_media_spoiler: :obj:`True`, if the message media is covered by a spoiler animation.
    :type has_media_spoiler: :obj:`True`, optional
    :param contact: Message is a shared contact, information about the contact.
    :type contact: :obj:`~apitele.types.Contact`, optional
    :param dice: Message is a dice with random value.
    :type dice: :obj:`~apitele.types.Dice`, optional
    :param game: Message is a game, information about the game. `More about games » <https://core.telegram.org/bots/api#games>`_.
    :type game: :obj:`~apitele.types.Game`, optional
    :param giveaway: Message is a scheduled giveaway, information about the giveaway.
    :type giveaway: :obj:`~apitele.types.Giveaway`, optional
    :param giveaway_winners: A giveaway with public winners was completed.
    :type giveaway_winners: :obj:`~apitele.types.GiveawayWinners`, optional
    :param invoice: Message is an invoice for a `payment <https://core.telegram.org/bots/api#payments>`_, information about the invoice. `More about payments » <https://core.telegram.org/bots/api#payments>`_.
    :type invoice: :obj:`~apitele.types.Invoice`, optional
    :param location: Message is a shared location, information about the location.
    :type location: :obj:`~apitele.types.Location`, optional
    :param poll: Message is a native poll, information about the poll.
    :type poll: :obj:`~apitele.types.Poll`, optional
    :param venue: Message is a venue, information about the venue.
    :type venue: :obj:`~apitele.types.Venue`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['origin'] = _dese_message_origin(res.get('origin'))
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['message_id'] = res.get('message_id')
        obj['link_preview_options'] = LinkPreviewOptions._dese(res.get('link_preview_options'))
        obj['animation'] = Animation._dese(res.get('animation'))
        obj['audio'] = Audio._dese(res.get('audio'))
        obj['document'] = Document._dese(res.get('document'))
        obj['paid_media'] = PaidMediaInfo._dese(res.get('paid_media'))
        obj['photo'] = [PhotoSize._dese(kwargs) for kwargs in res.get('photo')] if 'photo' in res else None
        obj['sticker'] = Sticker._dese(res.get('sticker'))
        obj['story'] = Story._dese(res.get('story'))
        obj['video'] = Video._dese(res.get('video'))
        obj['video_note'] = VideoNote._dese(res.get('video_note'))
        obj['voice'] = Voice._dese(res.get('voice'))
        obj['has_media_spoiler'] = res.get('has_media_spoiler')
        obj['contact'] = Contact._dese(res.get('contact'))
        obj['dice'] = Dice._dese(res.get('dice'))
        obj['game'] = Game._dese(res.get('game'))
        obj['giveaway'] = Giveaway._dese(res.get('giveaway'))
        obj['giveaway_winners'] = GiveawayWinners._dese(res.get('giveaway_winners'))
        obj['invoice'] = Invoice._dese(res.get('invoice'))
        obj['location'] = Location._dese(res.get('location'))
        obj['poll'] = Poll._dese(res.get('poll'))
        obj['venue'] = Venue._dese(res.get('venue'))
        return cls(**obj)

    def __init__(
        self,
        origin: MessageOrigin,
        chat: Optional[Chat] = None,
        message_id: Optional[int] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        animation: Optional[Animation] = None,
        audio: Optional[Audio] = None,
        document: Optional[Document] = None,
        paid_media: Optional[PaidMediaInfo] = None,
        photo: Optional[list[PhotoSize]] = None,
        sticker: Optional[Sticker] = None,
        story: Optional[Story] = None,
        video: Optional[Video] = None,
        video_note: Optional[VideoNote] = None,
        voice: Optional[Voice] = None,
        has_media_spoiler: Optional[Literal[True]] = None,
        contact: Optional[Contact] = None,
        dice: Optional[Dice] = None,
        game: Optional[Game] = None,
        giveaway: Optional[Giveaway] = None,
        giveaway_winners: Optional[GiveawayWinners] = None,
        invoice: Optional[Invoice] = None,
        location: Optional[Location] = None,
        poll: Optional[Poll] = None,
        venue: Optional[Venue] = None
    ):
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue


class File(TelegramType):
    '''
    https://core.telegram.org/bots/api#file

    This object represents a file ready to be downloaded. The file can be
    downloaded via the link ``https://api.telegram.org/file/bot<token>/<file_path>``.
    It is guaranteed that the link will be valid for at least 1 hour. When the link
    expires, a new one can be requested by calling :meth:`~apitele.Client.get_file`.

        The maximum file size to download is 20 MB

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`, optional
    :param file_path: File path. Use ``https://api.telegram.org/file/bot<token>/<file_path>`` to get the file.
    :type file_path: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['file_size'] = res.get('file_size')
        obj['file_path'] = res.get('file_path')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_size: Optional[int] = None,
        file_path: Optional[str] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path


class ForceReply(TelegramType):
    '''
    https://core.telegram.org/bots/api#forcereply

    Upon receiving a message with this object, Telegram clients will display a reply
    interface to the user (act as if the user has selected the bot's message and tapped 'Reply').
    This can be extremely useful if you want to create user-friendly step-by-step interfaces without
    having to sacrifice `privacy mode <https://core.telegram.org/bots/features#privacy-mode>`_.

        **Example**: A `poll bot <https://t.me/PollBot>`_ for groups runs in privacy mode
        (only receives commands, replies to its messages and mentions).
        There could be two ways to create a new poll:

        - Explain the user how to send a command with parameters (e.g. /newpoll question answer1 answer2). May be appealing for hardcore users but lacks modern day polish.
        - Guide the user through a step-by-step process. 'Please send me your question', 'Cool, now let's add the first answer option', 'Great. Keep adding answer options, then send /done when you're ready'.

        The last option is definitely more attractive. And if you
        use :obj:`~apitele.types.ForceReply` in your bot's questions,
        it will receive the user's answers even if it only receives
        replies, commands and mentions - without any extra work for the user.

    :param input_field_placeholder: The placeholder to be shown in the input field when the reply is active; 1-64 characters.
    :type input_field_placeholder: :obj:`str`, optional
    :param selective: Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the *text* of the :obj:`~apitele.types.Message` object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.
    :type selective: :obj:`bool`, optional
    '''
    def __init__(
        self,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None
    ):
        self.force_reply: Literal[True] = True
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective


class ForumTopic(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopic

    This object represents a forum topic.

    :param message_thread_id: Unique identifier of the forum topic.
    :type message_thread_id: :obj:`int`
    :param name: Name of the topic.
    :type name: :obj:`str`
    :param icon_color: Color of the topic icon in RGB format.
    :type icon_color: :obj:`int`
    :param icon_custom_emoji_id: Unique identifier of the custom emoji shown as the topic icon.
    :type icon_custom_emoji_id: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['message_thread_id'] = res.get('message_thread_id')
        obj['name'] = res.get('name')
        obj['icon_color'] = res.get('icon_color')
        obj['icon_custom_emoji_id'] = res.get('icon_custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        message_thread_id: int,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: Optional[str] = None
    ):
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicClosed(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopicclosed

    This object represents a service message about a forum
    topic closed in the chat. Currently holds no information.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        ...


class ForumTopicCreated(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopiccreated

    This object represents a service message about a new forum topic created in the chat.

    :param name: Name of the topic.
    :type name: :obj:`str`
    :param icon_color: Color of the topic icon in RGB format.
    :type icon_color: :obj:`int`
    :param icon_custom_emoji_id: Unique identifier of the custom emoji shown as the topic icon.
    :type icon_custom_emoji_id: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        obj['icon_color'] = res.get('icon_color')
        obj['icon_custom_emoji_id'] = res.get('icon_custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: Optional[str] = None
    ):
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicEdited(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopicedited

    This object represents a service message about an edited forum topic.

    :param name: New name of the topic, if it was edited.
    :type name: :obj:`str`, optional
    :param icon_custom_emoji_id: New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed.
    :type icon_custom_emoji_id: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        obj['icon_custom_emoji_id'] = res.get('icon_custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        name: Optional[str] = None,
        icon_custom_emoji_id: Optional[str] = None
    ):
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicReopened(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopicreopened

    This object represents a service message about a forum
    topic reopened in the chat. Currently holds no information.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        ...


class Game(TelegramType):
    '''
    https://core.telegram.org/bots/api#game

    This object represents a game.
    Use BotFather to create and edit games,
    their short names will act as unique identifiers.

    :param title: Title of the game.
    :type title: :obj:`str`
    :param description: Description of the game.
    :type description: :obj:`str`
    :param photo: Photo that will be displayed in the game message in chats.
    :type photo: :obj:`list` of :obj:`~apitele.types.PhotoSize`
    :param text: Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls :meth:`~apitele.Client.set_game_score`, or manually edited using :meth:`~apitele.Client.edit_message_text`. 0-4096 characters.
    :type text: :obj:`str`, optional
    :param text_entities: Special entities that appear in *text*, such as usernames, URLs, bot commands, etc.
    :type text_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param animation: Animation that will be displayed in the game message in chats. Upload via `BotFather <https://t.me/botfather>`_.
    :type animation: :obj:`~apitele.types.Animation`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['title'] = res.get('title')
        obj['description'] = res.get('description')
        obj['photo'] = [PhotoSize._dese(kwargs) for kwargs in res.get('photo')]
        obj['text'] = res.get('text')
        obj['text_entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('text_entities')] if 'text_entities' in res else None
        obj['animation'] = Animation._dese(res.get('animation'))
        return cls(**obj)

    def __init__(
        self,
        title: str,
        description: str,
        photo: list[PhotoSize],
        text: Optional[str] = None,
        text_entities: Optional[list[MessageEntity]] = None,
        animation: Optional[Animation] = None
    ):
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation


class GameHighScore(TelegramType):
    '''
    https://core.telegram.org/bots/api#gamehighscore

    This object represents one row of the high scores table for a game.

    :param position: Position in high score table for the game.
    :type position: :obj:`int`
    :param user: User.
    :type user: :obj:`~apitele.types.User`
    :param score: Score.
    :type score: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['position'] = res.get('position')
        obj['user'] = User._dese(res.get('user'))
        obj['score'] = res.get('score')
        return cls(**obj)

    def __init__(
        self,
        position: int,
        user: User,
        score: int
    ):
        self.position = position
        self.user = user
        self.score = score


class GeneralForumTopicHidden(TelegramType):
    '''
    https://core.telegram.org/bots/api#generalforumtopichidden

    This object represents a service message about General forum
    topic hidden in the chat. Currently holds no information.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        ...


class GeneralForumTopicUnhidden(TelegramType):
    '''
    https://core.telegram.org/bots/api#generalforumtopicunhidden

    This object represents a service message about General forum
    topic unhidden in the chat. Currently holds no information.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        ...


class Gift(TelegramType):
    '''
    https://core.telegram.org/bots/api#gift

    This object represents a gift that can be sent by the bot.

    :param id: Unique identifier of the gift.
    :type id: :obj:`str`
    :param sticker: The sticker that represents the gift.
    :type sticker: :obj:`~apitele.types.Sticker`
    :param star_count: The number of Telegram Stars that must be paid to send the sticker.
    :type star_count: :obj:`int`
    :param upgrade_star_count: The number of Telegram Stars that must be paid to upgrade the gift to a unique one.
    :type upgrade_star_count: :obj:`int`, optional
    :param total_count: The total number of the gifts of this type that can be sent; for limited gifts only.
    :type total_count: :obj:`int`, optional
    :param remaining_count: The number of remaining gifts of this type that can be sent; for limited gifts only.
    :type remaining_count: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['sticker'] = Sticker._dese(res.get('sticker'))
        obj['star_count'] = res.get('star_count')
        obj['upgrade_star_count'] = res.get('upgrade_star_count')
        obj['total_count'] = res.get('total_count')
        obj['remaining_count'] = res.get('remaining_count')
        return cls(**obj)

    def __init__(
        self,
        id: str,
        sticker: Sticker,
        star_count: int,
        upgrade_star_count: Optional[int] = None,
        total_count: Optional[int] = None,
        remaining_count: Optional[int] = None
    ):
        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.upgrade_star_count = upgrade_star_count
        self.total_count = total_count
        self.remaining_count = remaining_count


class GiftInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#giftinfo

    Describes a service message about a regular gift that was sent or received.

    :param gift: Information about the gift.
    :type gift: :obj:`~apitele.types.Gift`
    :param owned_gift_id: Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts.
    :type owned_gift_id: :obj:`str`, optional
    :param convert_star_count: Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible.
    :type convert_star_count: :obj:`int`, optional
    :param prepaid_upgrade_star_count: Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift.
    :type prepaid_upgrade_star_count: :obj:`int`, optional
    :param can_be_upgraded: :obj:`True`, if the gift can be upgraded to a unique gift.
    :type can_be_upgraded: :obj:`True`, optional
    :param text: Text of the message that was added to the gift.
    :type text: :obj:`str`, optional
    :param entities: Special entities that appear in the text.
    :type entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param is_private: :obj:`True`, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them.
    :type is_private: :obj:`True`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['gift'] = Gift._dese(res.get('gift'))
        obj['owned_gift_id'] = res.get('owned_gift_id')
        obj['convert_star_count'] = res.get('convert_star_count')
        obj['prepaid_upgrade_star_count'] = res.get('prepaid_upgrade_star_count')
        obj['can_be_upgraded'] = res.get('can_be_upgraded')
        obj['text'] = res.get('text')
        obj['entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('entities')] if 'entities' in res else None
        obj['is_private'] = res.get('is_private')
        return cls(**obj)

    def __init__(
        self,
        gift: Gift,
        owned_gift_id: Optional[str] = None,
        convert_star_count: Optional[int] = None,
        prepaid_upgrade_star_count: Optional[int] = None,
        can_be_upgraded: Optional[Literal[True]] = None,
        text: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        is_private: Optional[Literal[True]] = None
    ):
        self.gift = gift
        self.owned_gift_id = owned_gift_id
        self.convert_star_count = convert_star_count
        self.prepaid_upgrade_star_count = prepaid_upgrade_star_count
        self.can_be_upgraded = can_be_upgraded
        self.text = text
        self.entities = entities
        self.is_private = is_private


class Gifts(TelegramType):
    '''
    https://core.telegram.org/bots/api#gifts

    This object represent a list of gifts.

    :param gifts: The list of gifts.
    :type gifts: :obj:`list` of :obj:`~apitele.types.Gift`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['gifts'] = [Gift._dese(kwargs) for kwargs in res.get('gifts')]
        return cls(**obj)

    def __init__(
        self,
        gifts: list[Gift]
    ):
        self.gifts = gifts


class Giveaway(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveaway

    This object represents a message about a scheduled giveaway.

    :param chats: The list of chats which the user must join to participate in the giveaway.
    :type chats: :obj:`list` of :obj:`~apitele.types.Chat`
    :param winners_selection_date: Point in time (Unix timestamp) when winners of the giveaway will be selected.
    :type winners_selection_date: :obj:`int`
    :param winner_count: The number of users which are supposed to be selected as winners of the giveaway.
    :type winner_count: :obj:`int`
    :param only_new_members: :obj:`True`, if only users who join the chats after the giveaway started should be eligible to win.
    :type only_new_members: :obj:`True`, optional
    :param has_public_winners: :obj:`True`, if the list of giveaway winners will be visible to everyone
    :type has_public_winners: :obj:`True`, optional
    :param prize_description: Description of additional giveaway prize.
    :type prize_description: :obj:`str`, optional
    :param country_codes: A list of two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.
    :type country_codes: :obj:`list` of :obj:`str`, optional
    :param prize_star_count: The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.
    :type prize_star_count: :obj:`int`, optional
    :param premium_subscription_month_count: The number of months the Telegram Premium subscription won from the giveaway will be active for.
    :type premium_subscription_month_count: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chats'] = [Chat._dese(kwargs) for kwargs in res.get('chats')]
        obj['winners_selection_date'] = res.get('winners_selection_date')
        obj['winner_count'] = res.get('winner_count')
        obj['only_new_members'] = res.get('only_new_members')
        obj['has_public_winners'] = res.get('has_public_winners')
        obj['prize_description'] = res.get('prize_description')
        obj['country_codes'] = res.get('country_codes')
        obj['prize_star_count'] = res.get('prize_star_count')
        obj['premium_subscription_month_count'] = res.get('premium_subscription_month_count')
        return cls(**obj)

    def __init__(
        self,
        chats: list[Chat],
        winners_selection_date: int,
        winner_count: int,
        only_new_members: Optional[Literal[True]] = None,
        has_public_winners: Optional[Literal[True]] = None,
        prize_description: Optional[str] = None,
        country_codes: Optional[list[str]] = None,
        prize_star_count: Optional[int] = None,
        premium_subscription_month_count: Optional[int] = None
    ):
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.prize_star_count = prize_star_count
        self.premium_subscription_month_count = premium_subscription_month_count


class GiveawayCompleted(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveawaycompleted

    This object represents a service message about the completion of a giveaway without public winners.

    :param winner_count: Number of winners in the giveaway.
    :type winner_count: :obj:`int`
    :param unclaimed_prize_count: Number of undistributed prizes.
    :type unclaimed_prize_count: :obj:`int`, optional
    :param giveaway_message: Message with the giveaway that was completed, if it wasn't deleted.
    :type giveaway_message: :obj:`~apitele.types.Message`, optional
    :param is_star_giveaway: :obj:`True`, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.
    :type is_star_giveaway: :obj:`True`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['winner_count'] = res.get('winner_count')
        obj['unclaimed_prize_count'] = res.get('unclaimed_prize_count')
        obj['giveaway_message'] = Message._dese(res.get('giveaway_message'))
        obj['is_star_giveaway'] = res.get('is_star_giveaway')
        return cls(**obj)

    def __init__(
        self,
        winner_count: int,
        unclaimed_prize_count: Optional[int] = None,
        giveaway_message: Optional[Message] = None,
        is_star_giveaway: Optional[Literal[True]] = None
    ):
        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message
        self.is_star_giveaway = is_star_giveaway


class GiveawayCreated(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveawaycreated

    This object represents a service message about the creation of a scheduled giveaway.

    :param prize_star_count: The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.
    :type prize_star_count: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['prize_star_count'] = res.get('prize_star_count')
        return cls(**obj)

    def __init__(
        self,
        prize_star_count: Optional[int] = None
    ):
        self.prize_star_count = prize_star_count


class GiveawayWinners(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveawaywinners

    This object represents a message about the completion of a giveaway with public winners.

    :param chat: The chat that created the giveaway.
    :type chat: :obj:`~apitele.types.Chat`
    :param giveaway_message_id: Identifier of the message with the giveaway in the chat.
    :type giveaway_message_id: :obj:`int`
    :param winners_selection_date: Point in time (Unix timestamp) when winners of the giveaway were selected.
    :type winners_selection_date: :obj:`int`
    :param winner_count: Total number of winners in the giveaway.
    :type winner_count: :obj:`int`
    :param winners: List of up to 100 winners of the giveaway.
    :type winners: :obj:`list` of :obj:`~apitele.types.User`
    :param additional_chat_count: The number of other chats the user had to join in order to be eligible for the giveaway.
    :type additional_chat_count: :obj:`int`, optional
    :param prize_star_count: The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only.
    :type prize_star_count: :obj:`int`, optional
    :param premium_subscription_month_count: The number of months the Telegram Premium subscription won from the giveaway will be active for.
    :type premium_subscription_month_count: :obj:`int`, optional
    :param unclaimed_prize_count: Number of undistributed prizes.
    :type unclaimed_prize_count: :obj:`int`, optional
    :param only_new_members: :obj:`True`, if only users who had joined the chats after the giveaway started were eligible to win.
    :type only_new_members: :obj:`True`, optional
    :param was_refunded: :obj:`True`, if the giveaway was canceled because the payment for it was refunded.
    :type was_refunded: :obj:`True`, optional
    :param prize_description: Description of additional giveaway prize.
    :type prize_description: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['giveaway_message_id'] = res.get('giveaway_message_id')
        obj['winners_selection_date'] = res.get('winners_selection_date')
        obj['winner_count'] = res.get('winner_count')
        obj['winners'] = [User._dese(kwargs) for kwargs in res.get('winners')]
        obj['additional_chat_count'] = res.get('additional_chat_count')
        obj['prize_star_count'] = res.get('prize_star_count')
        obj['premium_subscription_month_count'] = res.get('premium_subscription_month_count')
        obj['unclaimed_prize_count'] = res.get('unclaimed_prize_count')
        obj['only_new_members'] = res.get('only_new_members')
        obj['was_refunded'] = res.get('was_refunded')
        obj['prize_description'] = res.get('prize_description')
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        giveaway_message_id: int,
        winners_selection_date: int,
        winner_count: int,
        winners: list[User],
        additional_chat_count: Optional[int] = None,
        prize_star_count: Optional[int] = None,
        premium_subscription_month_count: Optional[int] = None,
        unclaimed_prize_count: Optional[int] = None,
        only_new_members: Optional[Literal[True]] = None,
        was_refunded: Optional[Literal[True]] = None,
        prize_description: Optional[str] = None
    ):
        self.chat = chat
        self.giveaway_message_id = giveaway_message_id
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.winners = winners
        self.additional_chat_count = additional_chat_count
        self.prize_star_count = prize_star_count
        self.premium_subscription_month_count = premium_subscription_month_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.only_new_members = only_new_members
        self.was_refunded = was_refunded
        self.prize_description = prize_description


class InaccessibleMessage(TelegramType):
    '''
    https://core.telegram.org/bots/api#inaccessiblemessage

    This object describes a message that was deleted or is otherwise inaccessible to the bot.

    :param chat: Chat the message belonged to.
    :type chat: :obj:`~apitele.types.Chat`
    :param message_id: Unique message identifier inside the chat.
    :type message_id: :obj:`int`
    :param date: Always 0. The field can be used to differentiate regular and inaccessible messages.
    :type date: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['message_id'] = res.get('message_id')
        obj['date'] = res.get('date')
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        message_id: int,
        date: int
    ):
        self.chat = chat
        self.message_id = message_id
        self.date = date


class InlineKeyboardButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinekeyboardbutton

    This object represents one button of an inline keyboard.
    You **must** use exactly one of the optional fields.

    :param text: Label text on the button.
    :type text: :obj:`str`
    :param url: HTTP or tg:// URL to be opened when the button is pressed. Links ``tg://user?id=<user_id>`` can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings.
    :type url: :obj:`str`, optional
    :param callback_data: Data to be sent in a :obj:`callback query <apitele.types.CallbackQuery>` to the bot when button is pressed, 1-64 bytes.
    :type callback_data: :obj:`str`, optional
    :param web_app: Description of the `Web App <https://core.telegram.org/bots/webapps>`_ that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method :meth:`~apitele.Client.answer_web_app_query`. Available only in private chats between a user and the bot.
    :type web_app: :obj:`~apitele.types.WebAppInfo`, optional
    :param login_url: An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the `Telegram Login Widget <https://core.telegram.org/widgets/login>`_.
    :type login_url: :obj:`~apitele.types.LoginUrl`, optional
    :param switch_inline_query: If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted.
    :type switch_inline_query: :obj:`str`, optional
    :param switch_inline_query_current_chat:
        If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted.

        This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options.
    :type switch_inline_query_current_chat: :obj:`str`, optional
    :param switch_inline_query_chosen_chat: If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field.
    :type switch_inline_query_chosen_chat: :obj:`~apitele.types.SwitchInlineQueryChosenChat`, optional
    :param copy_text: Description of the button that copies the specified text to the clipboard.
    :type copy_text: :obj:`~apitele.types.CopyTextButton`, optional
    :param callback_game:
        Description of the game that will be launched when the user presses the button.

        **NOTE**: This type of button **must** always be the first button in the first row.
    :type callback_game: :obj:`~apitele.types.CallbackGame`, optional
    :param pay:
        Specify :obj:`True`, to send a `Pay button <https://core.telegram.org/bots/api#payments>`_.

        **NOTE**: This type of button **must** always be the first button in the first row and can only be used in invoice messages.
    :type pay: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['text'] = res.get('text')
        obj['url'] = res.get('url')
        obj['callback_data'] = res.get('callback_data')
        obj['web_app'] = WebAppInfo._dese(res.get('web_app'))
        obj['login_url'] = LoginUrl._dese(res.get('login_url'))
        obj['switch_inline_query'] = res.get('switch_inline_query')
        obj['switch_inline_query_current_chat'] = res.get('switch_inline_query_current_chat')
        obj['switch_inline_query_chosen_chat'] = SwitchInlineQueryChosenChat._dese(res.get('switch_inline_query_chosen_chat'))
        obj['copy_text'] = CopyTextButton._dese(res.get('copy_text'))
        obj['callback_game'] = CallbackGame._dese(res.get('callback_game'))
        obj['pay'] = res.get('pay')
        return cls(**obj)

    def __init__(
        self,
        text: str,
        url: Optional[str] = None,
        callback_data: Optional[str] = None,
        web_app: Optional[WebAppInfo] = None, 
        login_url: Optional[LoginUrl] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None,
        copy_text: Optional[CopyTextButton] = None,
        callback_game: Optional[CallbackGame] = None,
        pay: Optional[bool] = None
    ):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.copy_text = copy_text
        self.callback_game = callback_game
        self.pay = pay


class InlineKeyboardMarkup(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinekeyboardmarkup

    This object represents an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ that appears right next to the message it belongs to.

    :param inline_keyboard: Array of button rows, each represented by an Array of :obj:`~apitele.types.InlineKeyboardButton` objects.
    :type inline_keyboard: :obj:`list` of :obj:`list` of :obj:`~apitele.types.InlineKeyboardButton`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['inline_keyboard'] = [[InlineKeyboardButton._dese(kwargs) for kwargs in lst] for lst in res.get('inline_keyboard')]
        return cls(**obj)

    def __init__(
        self,
        inline_keyboard: Optional[list[list[InlineKeyboardButton]]] = None
    ):
        self.inline_keyboard = inline_keyboard or []

    def add(self, *buttons: InlineKeyboardButton) -> Self:
        '''
        Usage:

        .. code-block:: python3

            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton('x', callback_data='x'),
                InlineKeyboardButton('y', callback_data='y'),
                InlineKeyboardButton('z', callback_data='z')
            )
            # All the buttons added with this method will be in
            # the same row, you can change the row width after the
            # object initialization using the property setter 'row_width'.

        :param buttons: :obj:`InlineKeyboardButtons <apitele.types.InlineKeyboardButton>` to add to a new row of the *inline_keyboard*.
        :type buttons: \*\ :obj:`~apitele.types.InlineKeyboardButton`
        :rtype: :obj:`~apitele.types.InlineKeyboardMarkup`
        '''
        self.inline_keyboard.append(buttons)
        return self

    @property
    def row_width(self) -> int:
        '''
        Usage:

        .. code-block:: python3

            markup.row_width = 2
            # The inline_keyboard will be rearranged with 2 buttons for each row.
        '''
        row_width = 0
        for nested in self.inline_keyboard:
            if len(nested) > row_width:
                row_width = len(nested)
        return row_width

    @row_width.setter
    def row_width(self, value: int) -> None:

        keyboard = []
        nested = []
        for row in self.inline_keyboard:
            for button in row:
                nested.append(button)
                if len(nested) == value:
                    keyboard.append(nested)
                    nested = []

        if nested:
            keyboard.append(nested)

        self.inline_keyboard = keyboard


class InlineQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequery

    This object represents an incoming inline query. When the user sends
    an empty query, your bot could return some default or trending results.

    :param id: Unique identifier for this query.
    :type id: :obj:`str`
    :param from_user: Sender.
    :type from_user: :obj:`~apitele.types.User`
    :param query: Text of the query (up to 256 characters).
    :type query: :obj:`str`
    :param offset: Offset of the results to be returned, can be controlled by the bot.
    :type offset: :obj:`str`
    :param chat_type: Type of the chat from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat.
    :type chat_type: :obj:`str`, optional
    :param location: Sender location, only for bots that request user location.
    :type location: :obj:`~apitele.types.Location`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['query'] = res.get('query')
        obj['offset'] = res.get('offset')
        obj['chat_type'] = res.get('chat_type')
        obj['location'] = Location._dese(res.get('location'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        query: str,
        offset: str,
        chat_type: Optional[str] = None,
        location: Optional[Location] = None
    ):
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location


class InlineQueryResultArticle(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultarticle

    Represents a link to an article or web page.

    :param id: Unique identifier for this result, 1-64 Bytes.
    :type id: :obj:`str`
    :param title: Title of the result.
    :type title: :obj:`str`
    :param input_message_content: Content of the message to be sent.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param url: URL of the result.
    :type url: :obj:`str`, optional
    :param description: Short description of the result.
    :type description: :obj:`str`, optional
    :param thumbnail_url: Url of the thumbnail for the result.
    :type thumbnail_url: :obj:`str`, optional
    :param thumbnail_width: Thumbnail width.
    :type thumbnail_width: :obj:`int`, optional
    :param thumbnail_height: Thumbnail height.
    :type thumbnail_height: :obj:`int`, optional
    '''
    def __init__(
        self,
        id: str,
        title: str,
        input_message_content: InputMessageContent,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        url: Optional[str] = None,
        description: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_ARTICLE
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultAudio(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultaudio

    Represents a link to an MP3 audio file.
    By default, this audio file will be sent by the user.
    Alternatively, you can use *input_message_content* to send
    a message with the specified content instead of the audio.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param audio_url: A valid URL for the audio file.
    :type audio_url: :obj:`str`
    :param title: Title.
    :type title: :obj:`str`
    :param caption: Caption, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the audio caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param performer: Performer.
    :type performer: :obj:`str`, optional
    :param audio_duration: Audio duration in seconds.
    :type audio_duration: :obj:`int`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the audio.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        audio_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        performer: Optional[str] = None,
        audio_duration: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_AUDIO
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedAudio(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio

    Represents a link to an MP3 audio file stored on the Telegram servers.
    By default, this audio file will be sent by the user. Alternatively, you can use
    *input_message_content* to send a message with the specified content instead of the audio.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param audio_file_id: A valid file identifier for the audio file.
    :type audio_file_id: :obj:`str`
    :param caption: Caption, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the audio caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the audio.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        audio_file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_AUDIO
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedDocument(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument

    Represents a link to a file stored on the Telegram servers.
    By default, this file will be sent by the user with an optional caption.
    Alternatively, you can use *input_message_content* to send a message with
    the specified content instead of the file.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param title: Title for the result.
    :type title: :obj:`str`
    :param document_file_id: A valid file identifier for the file.
    :type document_file_id: :obj:`str`
    :param description: Short description of the result.
    :type description: :obj:`str`, optional
    :param caption: Caption of the document to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the document caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the file.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        title: str,
        document_file_id: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_DOCUMENT
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedGif(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedgif

    Represents a link to an animated GIF file stored on the Telegram servers.
    By default, this animated GIF file will be sent by the user with an optional
    caption. Alternatively, you can use *input_message_content* to send a message
    with specified content instead of the animation.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param gif_file_id: A valid file identifier for the GIF file.
    :type gif_file_id: :obj:`str`
    :param title: Title for the result.
    :type title: :obj:`str`, optional
    :param caption: Caption of the GIF file to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the GIF animation.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        gif_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_GIF
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedMpeg4Gif(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif

    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored
    on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user
    with an optional caption. Alternatively, you can use *input_message_content* to send a
    message with the specified content instead of the animation.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param mpeg4_file_id: A valid file identifier for the MPEG4 file.
    :type mpeg4_file_id: :obj:`str`
    :param title: Title for the result.
    :type title: :obj:`str`, optional
    :param caption: Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the video animation.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        mpeg4_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_MPEG4_GIF
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto

    Represents a link to a photo stored on the Telegram servers.
    By default, this photo will be sent by the user with an optional caption.
    Alternatively, you can use *input_message_content* to send a message with
    the specified content instead of the photo.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param photo_file_id: A valid file identifier of the photo.
    :type photo_file_id: :obj:`str`
    :param title: Title for the result.
    :type title: :obj:`str`, optional
    :param description: Short description of the result.
    :type description: :obj:`str`, optional
    :param caption: Caption of the photo to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the photo caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the photo.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        photo_file_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_PHOTO
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedSticker(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker

    Represents a link to a sticker stored on the Telegram servers. By default, this sticker
    will be sent by the user. Alternatively, you can use *input_message_content* to send a
    message with the specified content instead of the sticker.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param sticker_file_id: A valid file identifier of the sticker.
    :type sticker_file_id: :obj:`str`
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the sticker.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        sticker_file_id: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_STICKER
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVideo(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo

    Represents a link to a video file stored on the Telegram servers.
    By default, this video file will be sent by the user with an optional
    caption. Alternatively, you can use *input_message_content* to send a
    message with the specified content instead of the video.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param video_file_id: A valid file identifier for the video file.
    :type video_file_id: :obj:`str`
    :param title: Title for the result.
    :type title: :obj:`str`
    :param description: Short description of the result.
    :type description: :obj:`str`, optional
    :param caption: Caption of the video to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the video caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the video.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        video_file_id: str,
        title: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_VIDEO
        self.id = id
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVoice(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice

    Represents a link to a voice message stored on the Telegram servers. By default,
    this voice message will be sent by the user. Alternatively, you can use *input_message_content*
    to send a message with the specified content instead of the voice message.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param voice_file_id: A valid file identifier for the voice message.
    :type voice_file_id: :obj:`str`
    :param title: Voice message title.
    :type title: :obj:`str`
    :param caption: Caption, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the voice message caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the voice message.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        voice_file_id: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CACHED_VOICE
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultContact(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcontact

    Represents a contact with a phone number. By default, this contact will be sent by the user.
    Alternatively, you can use *input_message_content* to send a message with the specified content
    instead of the contact.

    :param id: Unique identifier for this result, 1-64 Bytes.
    :type id: :obj:`str`
    :param phone_number: Contact's phone number.
    :type phone_number: :obj:`str`
    :param first_name: Contact's first name.
    :type first_name: :obj:`str`
    :param last_name: Contact's last name.
    :type last_name: :obj:`str`, optional
    :param vcard: Additional data about the contact in the form of a `vCard <https://en.wikipedia.org/wiki/VCard>`_, 0-2048 bytes.
    :type vcard: :obj:`str`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the contact.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    :param thumbnail_url: Url of the thumbnail for the result.
    :type thumbnail_url: :obj:`str`, optional
    :param thumbnail_width: Thumbnail width.
    :type thumbnail_width: :obj:`int`, optional
    :param thumbnail_height: Thumbnail height.
    :type thumbnail_height: :obj:`int`, optional
    '''
    def __init__(
        self,
        id: str,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_CONTACT
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultDocument(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultdocument

    Represents a link to a file. By default, this file will be sent by the user with an optional
    caption. Alternatively, you can use *input_message_content* to send a message with the specified
    content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param title: Title for the result.
    :type title: :obj:`str`
    :param document_url: A valid URL for the file.
    :type document_url: :obj:`str`
    :param mime_type: MIME type of the content of the file, either “application/pdf” or “application/zip”.
    :type mime_type: :obj:`str`
    :param caption: Caption of the document to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the document caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param description: Short description of the result.
    :type description: :obj:`str`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the file.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    :param thumbnail_url: URL of the thumbnail (JPEG only) for the file.
    :type thumbnail_url: :obj:`str`, optional
    :param thumbnail_width: Thumbnail width.
    :type thumbnail_width: :obj:`int`, optional
    :param thumbnail_height: Thumbnail height.
    :type thumbnail_height: :obj:`int`, optional
    '''
    def __init__(
        self,
        id: str,
        title: str,
        document_url: str,
        mime_type: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        description: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_DOCUMENT
        self.id = id
        self.title = title
        self.document_url = document_url
        self.mime_type = mime_type
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultGame(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultgame

    Represents a `Game <https://core.telegram.org/bots/api#games>`_.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param game_short_name: Short name of the game.
    :type game_short_name: :obj:`str`
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    '''
    def __init__(
        self,
        id: str,
        game_short_name: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_GAME
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup


class InlineQueryResultGif(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultgif

    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the
    user with optional caption. Alternatively, you can use *input_message_content* to send a message
    with the specified content instead of the animation.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param gif_url: A valid URL for the GIF file. File size must not exceed 1MB.
    :type gif_url: :obj:`str`
    :param thumbnail_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result.
    :type thumbnail_url: :obj:`str`
    :param gif_width: Width of the GIF.
    :type gif_width: :obj:`int`, optional
    :param gif_height: Height of the GIF.
    :type gif_height: :obj:`int`, optional
    :param gif_duration: Duration of the GIF in seconds.
    :type gif_duration: :obj:`int`, optional
    :param thumbnail_mime_type: MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”.
    :type thumbnail_mime_type: :obj:`str`, optional
    :param title: Title for the result.
    :type title: :obj:`str`, optional
    :param caption: Caption of the GIF file to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the GIF animation.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        gif_url: str,
        thumbnail_url: str,
        gif_width: Optional[int] = None,
        gif_height: Optional[int] = None,
        gif_duration: Optional[int] = None,
        thumbnail_mime_type: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_GIF
        self.id = id
        self.gif_url = gif_url
        self.thumbnail_url = thumbnail_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultLocation(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultlocation

    Represents a location on a map. By default, the location will be sent by the user.
    Alternatively, you can use *input_message_content* to send a message with the specified content instead of the location.

    :param id: Unique identifier for this result, 1-64 Bytes.
    :type id: :obj:`str`
    :param latitude: Location latitude in degrees.
    :type latitude: :obj:`float`
    :param longitude: Location longitude in degrees.
    :type longitude: :obj:`float`
    :param title: Location title.
    :type title: :obj:`str`
    :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500.
    :type horizontal_accuracy: :obj:`float`, optional
    :param live_period: Period in seconds for which the location can be updated, should be between 60 and 86400.
    :type live_period: :obj:`int`, optional
    :param heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :type heading: :obj:`int`, optional
    :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :type proximity_alert_radius: :obj:`int`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the location.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    :param thumbnail_url: Url of the thumbnail for the result.
    :type thumbnail_url: :obj:`str`, optional
    :param thumbnail_width: Thumbnail width.
    :type thumbnail_width: :obj:`int`, optional
    :param thumbnail_height: Thumbnail height.
    :type thumbnail_height: :obj:`int`, optional
    '''
    def __init__(
        self,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_LOCATION
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultMpeg4Gif(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif

    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound).
    By default, this animated MPEG-4 file will be sent by the user with optional caption.
    Alternatively, you can use *input_message_content* to send a message with the specified
    content instead of the animation.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param mpeg4_url: A valid URL for the MPEG4 file. File size must not exceed 1MB.
    :type mpeg4_url: :obj:`str`
    :param thumbnail_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result.
    :type thumbnail_url: :obj:`str`
    :param mpeg4_width: Video width.
    :type mpeg4_width: :obj:`int`, optional
    :param mpeg4_height: Video height.
    :type mpeg4_height: :obj:`int`, optional
    :param mpeg4_duration: Video duration in seconds.
    :type mpeg4_duration: :obj:`int`, optional
    :param thumbnail_mime_type: MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”.
    :type thumbnail_mime_type: :obj:`str`, optional
    :param title: Title for the result.
    :type title: :obj:`str`, optional
    :param caption: Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the video animation.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        mpeg4_url: str,
        thumbnail_url: str,
        mpeg4_width: Optional[int] = None,
        mpeg4_height: Optional[int] = None,
        mpeg4_duration: Optional[int] = None,
        thumbnail_mime_type: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_MPEG4_GIF
        self.id = id
        self.mpeg4_url = mpeg4_url
        self.thumbnail_url = thumbnail_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultphoto

    Represents a link to a photo. By default, this photo will be sent by the
    user with optional caption. Alternatively, you can use *input_message_content*
    to send a message with the specified content instead of the photo.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param photo_url: A valid URL of the photo. Photo must be in **JPEG** format. Photo size must not exceed 5MB.
    :type photo_url: :obj:`str`
    :param thumbnail_url: URL of the thumbnail for the photo.
    :type thumbnail_url: :obj:`str`
    :param photo_width: Width of the photo.
    :type photo_width: :obj:`int`, optional
    :param photo_height: Height of the photo.
    :type photo_height: :obj:`int`, optional
    :param title: Title for the result.
    :type title: :obj:`str`, optional
    :param description: Short description of the result.
    :type description: :obj:`str`, optional
    :param caption: Caption of the photo to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the photo caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the photo.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        photo_url: str,
        thumbnail_url: str,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_PHOTO
        self.id = id
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVenue(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultvenue

    Represents a venue. By default, the venue will be sent by the user.
    Alternatively, you can use *input_message_content* to send a message
    with the specified content instead of the venue.

    :param id: Unique identifier for this result, 1-64 Bytes.
    :type id: :obj:`str`
    :param latitude: Latitude of the venue location in degrees.
    :type latitude: :obj:`float`
    :param longitude: Longitude of the venue location in degrees.
    :type longitude: :obj:`float`
    :param title: Title of the venue.
    :type title: :obj:`str`
    :param address: Address of the venue.
    :type address: :obj:`str`
    :param foursquare_id: Foursquare identifier of the venue if known.
    :type foursquare_id: :obj:`str`, optional
    :param foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :type foursquare_type: :obj:`str`, optional
    :param google_place_id: Google Places identifier of the venue.
    :type google_place_id: :obj:`str`, optional
    :param google_place_type: Google Places type of the venue. (See `supported types <https://developers.google.com/places/web-service/supported_types>`_.)
    :type google_place_type: :obj:`str`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the venue.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    :param thumbnail_url: Url of the thumbnail for the result.
    :type thumbnail_url: :obj:`str`, optional
    :param thumbnail_width: Thumbnail width.
    :type thumbnail_width: :obj:`int`, optional
    :param thumbnail_height: Thumbnail height.
    :type thumbnail_height: :obj:`int`, optional
    '''
    def __init__(
        self,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_VENUE
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultVideo(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultvideo

    Represents a link to a page containing an embedded video player or a video file.
    By default, this video file will be sent by the user with an optional caption.
    Alternatively, you can use *input_message_content* to send a message with the
    specified content instead of the video.

        If an :obj:`~apitele.types.InlineQueryResultVideo` message contains an embedded
        video (e.g., YouTube), you **must** replace its content using *input_message_content*.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param video_url: A valid URL for the embedded video player or video file.
    :type video_url: :obj:`str`
    :param mime_type: MIME type of the content of the video URL, “text/html” or “video/mp4”.
    :type mime_type: :obj:`str`
    :param thumbnail_url: URL of the thumbnail (JPEG only) for the video.
    :type thumbnail_url: :obj:`str`
    :param title: Title for the result.
    :type title: :obj:`str`
    :param caption: Caption of the video to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the video caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param video_width: Video width.
    :type video_width: :obj:`int`, optional
    :param video_height: Video height.
    :type video_height: :obj:`int`, optional
    :param video_duration: Video duration in seconds.
    :type video_duration: :obj:`int`, optional
    :param description: Short description of the result.
    :type description: :obj:`str`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the video. This field is **required** if :obj:`~apitele.types.InlineQueryResultVideo` is used to send an HTML-page as a result (e.g., a YouTube video).
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        video_url: str,
        mime_type: str,
        thumbnail_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        video_width: Optional[int] = None,
        video_height: Optional[int] = None,
        video_duration: Optional[int] = None,
        description: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_VIDEO
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVoice(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultvoice

    Represents a link to a voice recording in an .OGG container encoded with OPUS.
    By default, this voice recording will be sent by the user.
    Alternatively, you can use *input_message_content* to send a message with the
    specified content instead of the the voice message.

    :param id: Unique identifier for this result, 1-64 bytes.
    :type id: :obj:`str`
    :param voice_url: A valid URL for the voice recording.
    :type voice_url: :obj:`str`
    :param title: Recording title.
    :type title: :obj:`str`
    :param caption: Caption, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the voice message caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param voice_duration: Recording duration in seconds.
    :type voice_duration: :obj:`int`, optional
    :param reply_markup: `Inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_ attached to the message.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    :param input_message_content: Content of the message to be sent instead of the voice recording.
    :type input_message_content: :obj:`~apitele.types.InputMessageContent`, optional
    '''
    def __init__(
        self,
        id: str,
        voice_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        voice_duration: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None
    ):
        self.type = DEFAULT_INLINE_QUERY_RESULT_VOICE
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultsButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultsbutton

    This object represents a button to be shown above inline query results.
    You **must** use exactly one of the optional fields.

    :param text: Label text on the button.
    :type text: :obj:`str`
    :param web_app: Description of the `Web App <https://core.telegram.org/bots/webapps>`_ that will be launched when the user presses the button. The Web App will be able to switch back to the inline mode using the method `switchInlineQuery <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_ inside the Web App.
    :type web_app: :obj:`~apitele.types.WebAppInfo`, optional
    :param start_parameter:
        `Deep-linking <https://core.telegram.org/bots/features#deep-linking>`_ parameter for the /start message sent to the bot when a user presses the button. 1-64 characters, only ``A-Z``, ``a-z``, ``0-9``, ``_`` and ``-`` are allowed.

        *Example*: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the
        results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer
        a :obj:`switch_inline <apitele.types.InlineKeyboardMarkup>` button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.
    :type start_parameter: :obj:`str`, optional
    '''
    def __init__(
        self,
        text: str,
        web_app: Optional[WebAppInfo] = None,
        start_parameter: Optional[str] = None
    ):
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter


class InputContactMessageContent(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputcontactmessagecontent

    Represents the :obj:`content <apitele.types.InputMessageContent>`
    of a contact message to be sent as the result of an inline query.

    :param phone_number: Contact's phone number.
    :type phone_number: :obj:`str`
    :param first_name: Contact's first name.
    :type first_name: :obj:`str`
    :param last_name: Contact's last name.
    :type last_name: :obj:`str`, optional
    :param vcard: Additional data about the contact in the form of a `vCard <https://en.wikipedia.org/wiki/VCard>`_, 0-2048 bytes.
    :type vcard: :obj:`str`, optional
    '''
    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard


class InputFile(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputfile

    This object represents the contents of a file to be uploaded. Must be posted
    using multipart/form-data in the usual way that files are uploaded via the browser.

        **Note**: If *file_name* or *hide_name* are not set, then the filename will be taken from the *path*.

    :param path: Directory of the file.
    :type path: :obj:`str`
    :param file_name: Select a different filename.
    :type file_name: :obj:`str`, optional
    :param hide_name: Hide the filename.
    :type hide_name: :obj:`bool`, optional
    '''
    def __init__(
        self,
        path: str,
        file_name: Optional[str] = None,
        hide_name: Optional[bool] = None
    ):
        self.path = path

        if not file_name and not hide_name:
            self.file_name = os.path.basename(path)

        elif file_name and not hide_name:
            self.file_name = file_name
        else:
            self.file_name = None


class InputInvoiceMessageContent(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputinvoicemessagecontent

    Represents the :obj:`content <apitele.types.InputMessageContent>` of an invoice message to be sent as the result of an inline query.

    :param title: Product name, 1-32 characters.
    :type title: :obj:`str`
    :param description: Product description, 1-255 characters.
    :type description: :obj:`str`
    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    :type payload: :obj:`str`
    :param currency: Three-letter ISO 4217 currency code, see `more on currencies <https://core.telegram.org/bots/payments#supported-currencies>`_. Pass “XTR” for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type currency: :obj:`str`
    :param prices: Price breakdown, a JSON-serialized list of components. (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type prices: :obj:`list` of :obj:`~apitele.types.LabeledPrice`
    :param provider_token: Payment provider token, obtained via `@BotFather <https://t.me/botfather>`_. Pass an empty string for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type provider_token: :obj:`str`, optional
    :param max_tip_amount: The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of ``US$ 1.45`` pass ``max_tip_amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to :obj:`0`. Not supported for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type max_tip_amount: :obj:`int`, optional
    :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tip in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*.
    :type suggested_tip_amounts: :obj:`list` of :obj:`int`, optional
    :param provider_data: A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
    :type provider_data: :obj:`str`, optional
    :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
    :type photo_url: :obj:`str`, optional
    :param photo_size: Photo size in bytes.
    :type photo_size: :obj:`int`, optional
    :param photo_width: Photo width.
    :type photo_width: :obj:`int`, optional
    :param photo_height: Photo height.
    :type photo_height: :obj:`int`, optional
    :param need_name: Pass :obj:`True` if you require the user's full name to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type need_name: :obj:`bool`, optional
    :param need_phone_number: Pass :obj:`True` if you require the user's phone number to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type need_phone_number: :obj:`bool`, optional
    :param need_email: Pass :obj:`True` if you require the user's email address to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type need_email: :obj:`bool`, optional
    :param need_shipping_address: Pass :obj:`True` if you require the user's shipping address to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type need_shipping_address: :obj:`bool`, optional
    :param send_phone_number_to_provider: Pass :obj:`True` if the user's phone number should be sent to provider. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type send_phone_number_to_provider: :obj:`bool`, optional
    :param send_email_to_provider: Pass :obj:`True` if the user's email address should be sent to provider. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type send_email_to_provider: :obj:`bool`, optional
    :param is_flexible: Pass :obj:`True` if the final price depends on the shipping method. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
    :type is_flexible: :obj:`bool`, optional
    '''
    def __init__(
        self,
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: list[LabeledPrice],
        provider_token: Optional[str] = None,
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[list[int]] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None
    ):
        self.title = title
        self.description = description
        self.payload = payload
        self.currency = currency
        self.prices = prices
        self.provider_token = provider_token
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible


class InputLocationMessageContent(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputlocationmessagecontent

    Represents the :obj:`content <apitele.types.InputMessageContent>`
    of a location message to be sent as the result of an inline query.

    :param latitude: Latitude of the location in degrees.
    :type latitude: :obj:`float`
    :param longitude: Longitude of the location in degrees.
    :type longitude: :obj:`float`
    :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500.
    :type horizontal_accuracy: :obj:`float`, optional
    :param live_period: Period in seconds for which the location can be updated, should be between 60 and 86400.
    :type live_period: :obj:`int`, optional
    :param heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :type heading: :obj:`int`, optional
    :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :type proximity_alert_radius: :obj:`int`, optional
    '''
    def __init__(
        self,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class InputMediaAnimation(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputmediaanimation

    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type media: :obj:`str`
    :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
    :param caption: Caption of the animation to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the animation caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param width: Animation width.
    :type width: :obj:`int`, optional
    :param height: Animation height.
    :type height: :obj:`int`, optional
    :param duration: Animation duration in seconds.
    :type duration: :obj:`int`, optional
    :param has_spoiler: Pass :obj:`True` if the animation needs to be covered with a spoiler animation.
    :type has_spoiler: :obj:`bool`, optional
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        has_spoiler: Optional[bool] = None
    ):
        self.type = DEFAULT_INPUT_MEDIA_ANIMATION
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.has_spoiler = has_spoiler


class InputMediaAudio(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputmediaaudio

    Represents an audio file to be treated as music to be sent.

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type media: :obj:`str`
    :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
    :param caption: Caption of the audio to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the audio caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param duration: Duration of the audio in seconds.
    :type duration: :obj:`int`, optional
    :param performer: Performer of the audio.
    :type performer: :obj:`str`, optional
    :param title: Title of the audio.
    :type title: :obj:`str`, optional
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None
    ):
        self.type = DEFAULT_INPUT_MEDIA_AUDIO
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title


class InputMediaDocument(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputmediadocument

    Represents a general file to be sent.

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type media: :obj:`str`
    :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
    :param caption: Caption of the document to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the document caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param disable_content_type_detection: Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always :obj:`True`, if the document is sent as part of an album.
    :type disable_content_type_detection: :obj:`bool`, optional
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None
    ):
        self.type = DEFAULT_INPUT_MEDIA_DOCUMENT
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection


class InputMediaPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputmediaphoto

    Represents a photo to be sent.

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type media: :obj:`str`
    :param caption: Caption of the photo to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the photo caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param has_spoiler: Pass :obj:`True` if the photo needs to be covered with a spoiler animation.
    :type has_spoiler: :obj:`bool`, optional
    '''
    def __init__(
        self,
        media: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None
    ):
        self.type = DEFAULT_INPUT_MEDIA_PHOTO
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler


class InputMediaVideo(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputmediavideo

    Represents a video to be sent.

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type media: :obj:`str`
    :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
    :param cover: Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type cover: :obj:`str`, optional
    :param start_timestamp: Start timestamp for the video in the message.
    :type start_timestamp: :obj:`int`, optional
    :param caption: Caption of the video to be sent, 0-1024 characters after entities parsing.
    :type caption: :obj:`str`, optional
    :param parse_mode: Mode for parsing entities in the video caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`bool`, optional
    :param width: Video width.
    :type width: :obj:`int`, optional
    :param height: Video height.
    :type height: :obj:`int`, optional
    :param duration: Video duration in seconds.
    :type duration: :obj:`int`, optional
    :param supports_streaming: Pass :obj:`True` if the uploaded video is suitable for streaming.
    :type supports_streaming: :obj:`bool`, optional
    :param has_spoiler: Pass :obj:`True` if the video needs to be covered with a spoiler animation.
    :type has_spoiler: :obj:`bool`, optional
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        cover: Optional[str] = None,
        start_timestamp: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        supports_streaming: Optional[bool] = None,
        has_spoiler: Optional[bool] = None
    ):
        self.type = DEFAULT_INPUT_MEDIA_VIDEO
        self.media = media
        self.thumbnail = thumbnail
        self.cover = cover
        self.start_timestamp = start_timestamp
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler


class InputPaidMediaPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputpaidmediaphoto

    The paid media to send is a photo.

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type media: :obj:`str`
    '''
    def __init__(
        self,
        media: str
    ):
        self.type = DEFAULT_INPUT_PAID_MEDIA_PHOTO
        self.media = media


class InputPaidMediaVideo(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputpaidmediavideo

    The paid media to send is a video.

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type media: :obj:`str`
    :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
    :param cover: Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type cover: :obj:`str`, optional
    :param start_timestamp: Start timestamp for the video in the message.
    :type start_timestamp: :obj:`int`, optional
    :param width: Video width.
    :type width: :obj:`int`, optional
    :param height: Video height.
    :type height: :obj:`int`, optional
    :param duration: Video duration in seconds.
    :type duration: :obj:`int`, optional
    :param supports_streaming: Pass :obj:`True` if the uploaded video is suitable for streaming.
    :type supports_streaming: :obj:`bool`, optional
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        cover: Optional[str] = None,
        start_timestamp: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        supports_streaming: Optional[bool] = None
    ):
        self.type = DEFAULT_INPUT_PAID_MEDIA_VIDEO
        self.media = media
        self.thumbnail = thumbnail
        self.cover = cover
        self.start_timestamp = start_timestamp
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming


class InputPollOption(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputpolloption

    This object contains information about one answer option in a poll to send.

    :param text: Option text, 1-100 characters.
    :type text: :obj:`str`
    :param text_parse_mode: Mode for parsing entities in the text. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details. Currently, only custom emoji entities are allowed.
    :type text_parse_mode: :obj:`str`, optional
    :param text_entities: A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of *text_parse_mode*.
    :type text_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    '''
    def __init__(
        self,
        text: str,
        text_parse_mode: Optional[str] = None,
        text_entities: Optional[list[MessageEntity]] = None
    ):
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities


class InputProfilePhotoStatic(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputprofilephotostatic

    A static profile photo in the .JPG format.

    :param photo: The static profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type photo: :obj:`str`
    '''
    def __init__(
        self,
        photo: str
    ):
        self.type = DEFAULT_INPUT_PROFILE_PHOTO_STATIC
        self.photo = photo


class InputProfilePhotoAnimated(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputprofilephotoanimated

    An animated profile photo in the MPEG4 format.

    :param animation: The animated profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type animation: :obj:`str`
    :param main_frame_timestamp: Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0.
    :type main_frame_timestamp: :obj:`float`, optional
    '''
    def __init__(
        self,
        animation: str,
        main_frame_timestamp: Optional[float] = None
    ):
        self.type = DEFAULT_INPUT_PROFILE_PHOTO_ANIMATED
        self.animation = animation
        self.main_frame_timestamp = main_frame_timestamp


class InputSticker(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputsticker

    This object describes a sticker to be added to a sticker set.

    :param sticker: The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, upload a new one using multipart/form-data, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type sticker: :obj:`~apitele.types.InputFile` or :obj:`str`
    :param format: Format of the added sticker, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, “video” for a **WEBM** video.
    :type format: :obj:`str`
    :param emoji_list: List of 1-20 emoji associated with the sticker.
    :type emoji_list: :obj:`list` of :obj:`str`
    :param mask_position: Position where the mask should be placed on faces. For “mask” stickers only.
    :type mask_position: :obj:`~apitele.types.MaskPosition`, optional
    :param keywords: List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom_emoji” stickers only.
    :type keywords: :obj:`list` of :obj:`str`, optional
    '''
    def __init__(
        self,
        sticker: Union[InputFile, str],
        format: str,
        emoji_list: list[str],
        mask_position: Optional[MaskPosition] = None,
        keywords: Optional[list[str]] = None
    ):
        self.sticker = sticker
        self.format = format
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords


class InputStoryContentPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputstorycontentphoto

    Describes a photo to post as a story.

    :param photo: The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB. The photo can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type photo: :obj:`str`
    '''
    def __init__(
        self,
        photo: str
    ):
        self.type = DEFAULT_INPUT_STORY_CONTENT_PHOTO
        self.photo = photo


class InputStoryContentVideo(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputstorycontentvideo

    Describes a video to post as a story.

    :param video: The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB. The video can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the video was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
    :type video: :obj:`str`
    :param duration: Precise duration of the video in seconds; 0-60.
    :type duration: :obj:`float`, optional
    :param cover_frame_timestamp: Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0.
    :type cover_frame_timestamp: :obj:`float`, optional
    :param is_animation: Pass :obj:`True` if the video has no sound.
    :type is_animation: :obj:`bool`, optional
    '''
    def __init__(
        self,
        video: str,
        duration: Optional[float] = None,
        cover_frame_timestamp: Optional[float] = None,
        is_animation: Optional[bool] = None
    ):
        self.type = DEFAULT_INPUT_STORY_CONTENT_VIDEO
        self.video = video
        self.duration = duration
        self.cover_frame_timestamp = cover_frame_timestamp
        self.is_animation = is_animation


class InputTextMessageContent(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputtextmessagecontent

    Represents the :obj:`content <apitele.types.InputMessageContent>`
    of a text message to be sent as the result of an inline query.

    :param message_text: Text of the message to be sent, 1-4096 characters.
    :type message_text: :obj:`str`
    :param parse_mode: Mode for parsing entities in the message text. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type parse_mode: :obj:`str`, optional
    :param entities: List of special entities that appear in message text, which can be specified instead of *parse_mode*.
    :type entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param link_preview_options: Link preview generation options for the message.
    :type link_preview_options: :obj:`~apitele.types.LinkPreviewOptions`, optional
    '''
    def __init__(
        self,
        message_text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None
    ):
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options


class InputVenueMessageContent(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputvenuemessagecontent

    Represents the :obj:`content <apitele.types.InputMessageContent>`
    of a venue message to be sent as the result of an inline query.

    :param latitude: Latitude of the venue in degrees.
    :type latitude: :obj:`float`
    :param longitude: Longitude of the venue in degrees.
    :type longitude: :obj:`float`
    :param title: Name of the venue.
    :type title: :obj:`str`
    :param address: Address of the venue.
    :type address: :obj:`str`
    :param foursquare_id: Foursquare identifier of the venue, if known.
    :type foursquare_id: :obj:`str`, optional
    :param foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :type foursquare_type: :obj:`str`, optional
    :param google_place_id: Google Places identifier of the venue.
    :type google_place_id: :obj:`str`, optional
    :param google_place_type: Google Places type of the venue. (See `supported types <https://developers.google.com/places/web-service/supported_types>`_.)
    :type google_place_type: :obj:`str`, optional
    '''
    def __init__(
        self,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class Invoice(TelegramType):
    '''
    https://core.telegram.org/bots/api#invoice

    This object contains basic information about an invoice.

    :param title: Product name.
    :type title: :obj:`str`
    :param description: Product description.
    :type description: :obj:`str`
    :param start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice.
    :type start_parameter: :obj:`str`
    :param currency: Three-letter ISO 4217 `currency <https://core.telegram.org/bots/payments#supported-currencies>`_ code.
    :type currency: :obj:`str`
    :param total_amount: Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of ``US$ 1.45`` pass ``amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['title'] = res.get('title')
        obj['description'] = res.get('description')
        obj['start_parameter'] = res.get('start_parameter')
        obj['currency'] = res.get('currency')
        obj['total_amount'] = res.get('total_amount')
        return cls(**obj)

    def __init__(
        self,
        title: str,
        description: str,
        start_parameter: str,
        currency: str,
        total_amount: int
    ):
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount


class KeyboardButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbutton

    This object represents one button of the reply keyboard. For simple text buttons, :obj:`String` can be
    used instead of this object to specify the button text. The optional fields *web_app*, *request_users*,
    *request_chat*, *request_contact*, *request_location*, and *request_poll* are mutually exclusive.

    :param text: Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed.
    :type text: :obj:`str`
    :param request_users: If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a “users_shared” service message. Available in private chats only.
    :type request_users: :obj:`~apitele.types.KeyboardButtonRequestUsers`, optional
    :param request_chat: If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a “chat_shared” service message. Available in private chats only.
    :type request_chat: :obj:`~apitele.types.KeyboardButtonRequestChat`, optional
    :param request_contact: If :obj:`True`, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.
    :type request_contact: :obj:`bool`, optional
    :param request_location: If :obj:`True`, the user's current location will be sent when the button is pressed. Available in private chats only.
    :type request_location: :obj:`bool`, optional
    :param request_poll: If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.
    :type request_poll: :obj:`~apitele.types.KeyboardButtonPollType`, optional
    :param web_app: If specified, the described `Web App <https://core.telegram.org/bots/webapps>`_ will be launched when the button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private chats only.
    :type web_app: :obj:`~apitele.types.WebAppInfo`, optional
    '''
    def __init__(
        self,
        text: str,
        request_users: Optional[KeyboardButtonRequestUsers] = None,
        request_chat: Optional[KeyboardButtonRequestChat] = None,
        request_contact: Optional[bool] = None,
        request_location: Optional[bool] = None,
        request_poll: Optional[KeyboardButtonPollType] = None,
        web_app: Optional[WebAppInfo] = None
    ):
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app


class KeyboardButtonPollType(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbuttonpolltype

    This object represents type of a poll, which is allowed to
    be created and sent when the corresponding button is pressed.

    :param type: If *quiz* is passed, the user will be allowed to create only polls in the quiz mode. If *regular* is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    :type type: :obj:`str`, optional
    '''
    def __init__(
        self,
        type: Optional[str] = None
    ):
        self.type = type


class KeyboardButtonRequestChat(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbuttonrequestchat

    This object defines the criteria used to request a suitable chat. Information about the
    selected chat will be shared with the bot when the corresponding button is pressed. The bot
    will be granted requested rights in the chat if appropriate `More about requesting chats » <https://core.telegram.org/bots/features#chat-and-user-selection>`_.

    :param request_id: Signed 32-bit identifier of the request, which will be received back in the :obj:`~apitele.types.ChatShared` object. Must be unique within the message.
    :type request_id: :obj:`int`
    :param chat_is_channel: Pass :obj:`True` to request a channel chat, pass :obj:`False` to request a group or a supergroup chat.
    :type chat_is_channel: :obj:`bool`
    :param chat_is_forum: Pass :obj:`True` to request a forum supergroup, pass :obj:`False` to request a non-forum chat. If not specified, no additional restrictions are applied.
    :type chat_is_forum: :obj:`bool`, optional
    :param chat_has_username: Pass :obj:`True` to request a supergroup or a channel with a username, pass :obj:`False` to request a chat without a username. If not specified, no additional restrictions are applied.
    :type chat_has_username: :obj:`bool`, optional
    :param chat_is_created: Pass :obj:`True` to request a chat owned by the user. Otherwise, no additional restrictions are applied.
    :type chat_is_created: :obj:`bool`, optional
    :param user_administrator_rights: A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of *bot_administrator_rights*. If not specified, no additional restrictions are applied.
    :type user_administrator_rights: :obj:`~apitele.types.ChatAdministratorRights`, optional
    :param bot_administrator_rights: A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of *user_administrator_rights*. If not specified, no additional restrictions are applied.
    :type bot_administrator_rights: :obj:`~apitele.types.ChatAdministratorRights`, optional
    :param bot_is_member: Pass :obj:`True` to request a chat with the bot as a member. Otherwise, no additional restrictions are applied.
    :type bot_is_member: :obj:`bool`, optional
    :param request_title: Pass :obj:`True` to request the chat's title.
    :type request_title: :obj:`bool`, optional
    :param request_username: Pass :obj:`True` to request the chat's username.
    :type request_username: :obj:`bool`, optional
    :param request_photo: Pass :obj:`True` to request the chat's photo.
    :type request_photo: :obj:`bool`, optional
    '''
    def __init__(
        self,
        request_id: int,
        chat_is_channel: bool,
        chat_is_forum: Optional[bool] = None,
        chat_has_username: Optional[bool] = None,
        chat_is_created: Optional[bool] = None,
        user_administrator_rights: Optional[ChatAdministratorRights] = None,
        bot_administrator_rights: Optional[ChatAdministratorRights] = None,
        bot_is_member: Optional[bool] = None,
        request_title: Optional[bool] = None,
        request_username: Optional[bool] = None,
        request_photo: Optional[bool] = None
    ):
        self.request_id = request_id
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member
        self.request_title = request_title
        self.request_username = request_username
        self.request_photo = request_photo


class KeyboardButtonRequestUsers(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbuttonrequestusers

    This object defines the criteria used to request suitable users. Information about the
    selected users will be shared with the bot when the corresponding button is pressed.
    `More about requesting users » <https://core.telegram.org/bots/features#chat-and-user-selection>`_.

    :param request_id: Signed 32-bit identifier of the request that will be received back in the :obj:`~apitele.types.UsersShared` object. Must be unique within the message.
    :type request_id: :obj:`int`
    :param user_is_bot: Pass :obj:`True` to request bots, pass :obj:`False` to request regular users. If not specified, no additional restrictions are applied.
    :type user_is_bot: :obj:`bool`, optional
    :param user_is_premium: Pass :obj:`True` to request premium users, pass :obj:`False` to request non-premium users. If not specified, no additional restrictions are applied.
    :type user_is_premium: :obj:`bool`, optional
    :param max_quantity: The maximum number of users to be selected; 1-10. Defaults to :obj:`1`.
    :type max_quantity: :obj:`int`, optional
    :param request_name: Pass :obj:`True` to request the users' first and last name.
    :type request_name: :obj:`bool`, optional
    :param request_username: Pass :obj:`True` to request the users' username.
    :type request_username: :obj:`bool`, optional
    :param request_photo: Pass :obj:`True` to request the users' photo.
    :type request_photo: :obj:`bool`, optional
    '''
    def __init__(
        self,
        request_id: int,
        user_is_bot: Optional[bool] = None,
        user_is_premium: Optional[bool] = None,
        max_quantity: Optional[int] = None,
        request_name: Optional[bool] = None,
        request_username: Optional[bool] = None,
        request_photo: Optional[bool] = None
    ):
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity
        self.request_name = request_name
        self.request_username = request_username
        self.request_photo = request_photo


class LabeledPrice(TelegramType):
    '''
    https://core.telegram.org/bots/api#labeledprice

    This object represents a portion of the price for goods or services.

    :param label: Portion label.
    :type label: :obj:`str`
    :param amount: Price of the product in the *smallest units* of the `currency <https://core.telegram.org/bots/payments#supported-currencies>`_ (integer, **not** float/double). For example, for a price of ``US$ 1.45`` pass ``amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type amount: :obj:`int`
    '''
    def __init__(
        self,
        label: str,
        amount: int
    ):
        self.label = label
        self.amount = amount


class LinkPreviewOptions(TelegramType):
    '''
    https://core.telegram.org/bots/api#linkpreviewoptions

    Describes the options used for link preview generation.

    :param is_disabled: :obj:`True`, if the link preview is disabled.
    :type is_disabled: :obj:`bool`, optional
    :param url: URL to use for the link preview. If empty, then the first URL found in the message text will be used.
    :type url: :obj:`str`, optional
    :param prefer_small_media: :obj:`True`, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.
    :type prefer_small_media: :obj:`bool`, optional
    :param prefer_large_media: :obj:`True`, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.
    :type prefer_large_media: :obj:`bool`, optional
    :param show_above_text: :obj:`True`, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text.
    :type show_above_text: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['is_disabled'] = res.get('is_disabled')
        obj['url'] = res.get('url')
        obj['prefer_small_media'] = res.get('prefer_small_media')
        obj['prefer_large_media'] = res.get('prefer_large_media')
        obj['show_above_text'] = res.get('show_above_text')
        return cls(**obj)

    def __init__(
        self,
        is_disabled: Optional[bool] = None,
        url: Optional[str] = None,
        prefer_small_media: Optional[bool] = None,
        prefer_large_media: Optional[bool] = None,
        show_above_text: Optional[bool] = None
    ):
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text


class Location(TelegramType):
    '''
    https://core.telegram.org/bots/api#location

    This object represents a point on the map.

    :param latitude: Latitude as defined by sender.
    :type latitude: :obj:`float`
    :param longitude: Longitude as defined by sender.
    :type longitude: :obj:`float`
    :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500.
    :type horizontal_accuracy: :obj:`float`, optional
    :param live_period: Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
    :type live_period: :obj:`int`, optional
    :param heading: The direction in which user is moving, in degrees; 1-360. For active live locations only.
    :type heading: :obj:`int`, optional
    :param proximity_alert_radius: The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    :type proximity_alert_radius: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['latitude'] = res.get('latitude')
        obj['longitude'] = res.get('longitude')
        obj['horizontal_accuracy'] = res.get('horizontal_accuracy')
        obj['live_period'] = res.get('live_period')
        obj['heading'] = res.get('heading')
        obj['proximity_alert_radius'] = res.get('proximity_alert_radius')
        return cls(**obj)

    def __init__(
        self,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class LocationAddress(TelegramType):
    '''
    https://core.telegram.org/bots/api#locationaddress

    Describes the physical address of a location.

    :param country_code: The two-letter ISO 3166-1 alpha-2 country code of the country where the location is located.
    :type country_code: :obj:`str`
    :param state: State of the location.
    :type state: :obj:`str`, optional
    :param city: City of the location.
    :type city: :obj:`str`, optional
    :param street: Street address of the location.
    :type street: :obj:`str`, optional
    '''
    def __init__(
        self,
        country_code: str,
        state: Optional[str] = None,
        city: Optional[str] = None,
        street: Optional[str] = None
    ):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street = street


class LoginUrl(TelegramType):
    '''
    https://core.telegram.org/bots/api#loginurl

    This object represents a parameter of the inline keyboard button used to automatically authorize
    a user. Serves as a great replacement for the `Telegram Login Widget <https://core.telegram.org/widgets/login>`_
    when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in.

    Telegram apps support these buttons as of `version 5.7 <https://telegram.org/blog/privacy-discussions-web-bots#meet-seamless-web-bots>`_.

        Sample bot: `@discussbot <https://t.me/discussbot>`_

    :param url:
        An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in `Receiving authorization data <https://core.telegram.org/widgets/login#receiving-authorization-data>`_.

        **NOTE**: You **must** always check the hash of the received data to verify the authentication and the integrity of the data as described in `Checking authorization <https://core.telegram.org/widgets/login#checking-authorization>`_.
    :type url: :obj:`str`
    :param forward_text: New text of the button in forwarded messages.
    :type forward_text: :obj:`str`, optional
    :param bot_username: Username of a bot, which will be used for user authorization. See `Setting up a bot <https://core.telegram.org/widgets/login#setting-up-a-bot>`_ for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See `Linking your domain to the bot <https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot>`_ for more details.
    :type bot_username: :obj:`str`, optional
    :param request_write_access: Pass :obj:`True` to request the permission for your bot to send messages to the user.
    :type request_write_access: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['url'] = res.get('url')
        obj['forward_text'] = res.get('forward_text')
        obj['bot_username'] = res.get('bot_username')
        obj['request_write_access'] = res.get('request_write_access')
        return cls(**obj)

    def __init__(
        self,
        url: str,
        forward_text: Optional[str] = None,
        bot_username: Optional[str] = None,
        request_write_access: Optional[bool] = None
    ):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access


class MaskPosition(TelegramType):
    '''
    https://core.telegram.org/bots/api#maskposition

    This object describes the position on faces where a mask should be placed by default.

    :param point: The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
    :type point: :obj:`str`
    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    :type x_shift: :obj:`float`
    :param y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    :type y_shift: :obj:`float`
    :param scale: Mask scaling coefficient. For example, 2.0 means double size.
    :type scale: :obj:`float`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['point'] = res.get('point')
        obj['x_shift'] = res.get('x_shift')
        obj['y_shift'] = res.get('y_shift')
        obj['scale'] = res.get('scale')
        return cls(**obj)

    def __init__(
        self,
        point: str,
        x_shift: float,
        y_shift: float,
        scale: float
    ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale


class MenuButtonCommands(TelegramType):
    '''
    https://core.telegram.org/bots/api#menubuttoncommands

    Represents a menu button, which opens the bot's list of commands.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        self.type = DEFAULT_MENU_BUTTON_COMMANDS


class MenuButtonDefault(TelegramType):
    '''
    https://core.telegram.org/bots/api#menubuttondefault

    Describes that no specific value for the menu button was set.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        self.type = DEFAULT_MENU_BUTTON_DEFAULT


class MenuButtonWebApp(TelegramType):
    '''
    https://core.telegram.org/bots/api#menubuttonwebapp

    Represents a menu button, which launches a `Web App <https://core.telegram.org/bots/webapps>`_.

    :param text: Text on the button.
    :type text: :obj:`str`
    :param web_app: Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method :meth:`~apitele.Client.answer_web_app_query`. Alternatively, a ``t.me`` link to a Web App of the bot can be specified in the object instead of the Web App's URL, in which case the Web App will be opened as if the user pressed the link.
    :type web_app: :obj:`~apitele.types.WebAppInfo`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['text'] = res.get('text')
        obj['web_app'] = WebAppInfo._dese(res.get('web_app'))
        return cls(**obj)

    def __init__(
        self,
        text: str,
        web_app: WebAppInfo
    ):
        self.type = DEFAULT_MENU_BUTTON_WEB_APP
        self.text = text
        self.web_app = web_app


class Message(TelegramType):
    '''
    https://core.telegram.org/bots/api#message

    This object represents a message.

    :param message_id: Unique message identifier inside this chat.
    :type message_id: :obj:`int`
    :param date: Date the message was sent in Unix time. It is always a positive number, representing a valid date.
    :type date: :obj:`int`
    :param chat: Chat the message belongs to.
    :type chat: :obj:`~apitele.types.Chat`
    :param message_thread_id: Unique identifier of a message thread to which the message belongs; for supergroups only.
    :type message_thread_id: :obj:`int`, optional
    :param from_user: Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    :type from_user: :obj:`~apitele.types.User`, optional
    :param sender_chat: Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    :type sender_chat: :obj:`~apitele.types.Chat`, optional
    :param sender_boost_count: If the sender of the message boosted the chat, the number of boosts added by the user.
    :type sender_boost_count: :obj:`int`, optional
    :param sender_business_bot: The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account.
    :type sender_business_bot: :obj:`~apitele.types.User`, optional
    :param business_connection_id: Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.
    :type business_connection_id: :obj:`str`, optional
    :param forward_origin: Information about the original message for forwarded messages.
    :type forward_origin: :obj:`~apitele.types.MessageOrigin`, optional
    :param is_topic_message: :obj:`True`, if the message is sent to a forum topic.
    :type is_topic_message: :obj:`True`, optional
    :param is_automatic_forward: :obj:`True`, if the message is a channel post that was automatically forwarded to the connected discussion group.
    :type is_automatic_forward: :obj:`True`, optional
    :param reply_to_message: For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further *reply_to_message* fields even if it itself is a reply.
    :type reply_to_message: :obj:`~apitele.types.Message`, optional
    :param external_reply: Information about the message that is being replied to, which may come from another chat or forum topic.
    :type external_reply: :obj:`~apitele.types.ExternalReplyInfo`, optional
    :param quote: For replies that quote part of the original message, the quoted part of the message.
    :type quote: :obj:`~apitele.types.TextQuote`, optional
    :param reply_to_story: For replies to a story, the original story.
    :type reply_to_story: :obj:`~apitele.types.Story`, optional
    :param via_bot: Bot through which the message was sent.
    :type via_bot: :obj:`~apitele.types.User`, optional
    :param edit_date: Date the message was last edited in Unix time.
    :type edit_date: :obj:`int`, optional
    :param has_protected_content: :obj:`True`, if the message can't be forwarded.
    :type has_protected_content: :obj:`True`, optional
    :param is_from_offline: :obj:`True`, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message.
    :type is_from_offline: :obj:`True`, optional
    :param media_group_id: The unique identifier of a media message group this message belongs to.
    :type media_group_id: :obj:`str`, optional
    :param author_signature: Signature of the post author for messages in channels, or the custom title of an anonymous group administrator.
    :type author_signature: :obj:`str`, optional
    :param paid_star_count: The number of Telegram Stars that were paid by the sender of the message to send it.
    :type paid_star_count: :obj:`int`, optional
    :param text: For text messages, the actual UTF-8 text of the message.
    :type text: :obj:`str`, optional
    :param entities: For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.
    :type entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param link_preview_options: Options used for link preview generation for the message, if it is a text message and link preview options were changed.
    :type link_preview_options: :obj:`~apitele.types.LinkPreviewOptions`, optional
    :param effect_id: Unique identifier of the message effect added to the message.
    :type effect_id: :obj:`str`, optional
    :param animation: Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set.
    :type animation: :obj:`~apitele.types.Animation`, optional
    :param audio: Message is an audio file, information about the file.
    :type audio: :obj:`~apitele.types.Audio`, optional
    :param document: Message is a general file, information about the file.
    :type document: :obj:`~apitele.types.Document`, optional
    :param paid_media: Message contains paid media; information about the paid media.
    :type paid_media: :obj:`~apitele.types.PaidMediaInfo`, optional
    :param photo: Message is a photo, available sizes of the photo.
    :type photo: :obj:`list` of :obj:`~apitele.types.PhotoSize`, optional
    :param sticker: Message is a sticker, information about the sticker.
    :type sticker: :obj:`~apitele.types.Sticker`, optional
    :param story: Message is a forwarded story.
    :type story: :obj:`~apitele.types.Story`, optional
    :param video: Message is a video, information about the video.
    :type video: :obj:`~apitele.types.Video`, optional
    :param video_note: Message is a `video note <https://telegram.org/blog/video-messages-and-telescope>`_, information about the video message.
    :type video_note: :obj:`~apitele.types.VideoNote`, optional
    :param voice: Message is a voice message, information about the file.
    :type voice: :obj:`~apitele.types.Voice`, optional
    :param caption: Caption for the animation, audio, document, photo, video or voice.
    :type caption: :obj:`str`, optional
    :param caption_entities: For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption.
    :type caption_entities: :obj:`list` of :obj:`MessageEntity`, optional
    :param show_caption_above_media: :obj:`True`, if the caption must be shown above the message media.
    :type show_caption_above_media: :obj:`True`, optional
    :param has_media_spoiler: :obj:`True`, if the message media is covered by a spoiler animation.
    :type has_media_spoiler: :obj:`True`, optional
    :param contact: Message is a shared contact, information about the contact.
    :type contact: :obj:`~apitele.types.Contact`, optional
    :param dice: Message is a dice with random value.
    :type dice: :obj:`~apitele.types.Dice`, optional
    :param game: Message is a game, information about the game. `More about games » <https://core.telegram.org/bots/api#games>`_.
    :type game: :obj:`~apitele.types.Game`, optional
    :param poll: Message is a native poll, information about the poll.
    :type poll: :obj:`~apitele.types.Poll`, optional
    :param venue: Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set.
    :type venue: :obj:`~apitele.types.Venue`, optional
    :param location: Message is a shared location, information about the location.
    :type location: :obj:`~apitele.types.Location`, optional
    :param new_chat_members: New members that were added to the group or supergroup and information about them (the bot itself may be one of these members).
    :type new_chat_members: :obj:`list` of :obj:`~apitele.types.User`, optional
    :param left_chat_member: A member was removed from the group, information about them (this member may be the bot itself).
    :type left_chat_member: :obj:`~apitele.types.User`, optional
    :param new_chat_title: A chat title was changed to this value.
    :type new_chat_title: :obj:`str`, optional
    :param new_chat_photo: A chat photo was change to this value.
    :type new_chat_photo: :obj:`list` of :obj:`~apitele.types.PhotoSize`, optional
    :param delete_chat_photo: Service message: the chat photo was deleted.
    :type delete_chat_photo: :obj:`True`, optional
    :param group_chat_created: Service message: the group has been created.
    :type group_chat_created: :obj:`True`, optional
    :param supergroup_chat_created: Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    :type supergroup_chat_created: :obj:`True`, optional
    :param channel_chat_created: Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    :type channel_chat_created: :obj:`True`, optional
    :param message_auto_delete_timer_changed: Service message: auto-delete timer settings changed in the chat.
    :type message_auto_delete_timer_changed: :obj:`~apitele.types.MessageAutoDeleteTimerChanged`, optional
    :param migrate_to_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :type migrate_to_chat_id: :obj:`int`, optional
    :param migrate_from_chat_id: The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :type migrate_from_chat_id: :obj:`int`, optional
    :param pinned_message: Specified message was pinned. Note that the Message object in this field will not contain further *reply_to_message* fields even if it itself is a reply.
    :type pinned_message: :obj:`~apitele.types.MaybeInaccessibleMessage`, optional
    :param invoice: Message is an invoice for a `payment <https://core.telegram.org/bots/api#payments>`_, information about the invoice. `More about payments » <https://core.telegram.org/bots/api#payments>`_.
    :type invoice: :obj:`~apitele.types.Invoice`, optional
    :param successful_payment: Message is a service message about a successful payment, information about the payment. `More about payments » <https://core.telegram.org/bots/api#payments>`_.
    :type successful_payment: :obj:`~apitele.types.SuccessfulPayment`, optional
    :param refunded_payment: Message is a service message about a refunded payment, information about the payment. `More about payments » <https://core.telegram.org/bots/api#payments>`_.
    :type refunded_payment: :obj:`~apitele.types.RefundedPayment`, optional
    :param users_shared: Service message: users were shared with the bot.
    :type users_shared: :obj:`~apitele.types.UsersShared`, optional
    :param chat_shared: Service message: a chat was shared with the bot.
    :type chat_shared: :obj:`~apitele.types.ChatShared`, optional
    :param gift: Service message: a regular gift was sent or received.
    :type gift: :obj:`~apitele.types.GiftInfo`, optional
    :param unique_gift: Service message: a unique gift was sent or received.
    :type unique_gift: :obj:`~apitele.types.UniqueGiftInfo`, optional
    :param connected_website: The domain name of the website on which the user has logged in. `More about Telegram Login » <https://core.telegram.org/widgets/login>`_.
    :type connected_website: :obj:`str`, optional
    :param write_access_allowed: Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method `requestWriteAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_.
    :type write_access_allowed: :obj:`~apitele.types.WriteAccessAllowed`, optional
    :param passport_data: Telegram Passport data.
    :type passport_data: :obj:`~apitele.types.PassportData`, optional
    :param proximity_alert_triggered: Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    :type proximity_alert_triggered: :obj:`~apitele.types.ProximityAlertTriggered`, optional
    :param boost_added: Service message: user boosted the chat.
    :type boost_added: :obj:`~apitele.types.ChatBoostAdded`, optional
    :param chat_background_set: Service message: chat background set.
    :type chat_background_set: :obj:`~apitele.types.ChatBackground`, optional
    :param forum_topic_created: Service message: forum topic created.
    :type forum_topic_created: :obj:`~apitele.types.ForumTopicCreated`, optional
    :param forum_topic_edited: Service message: forum topic edited.
    :type forum_topic_edited: :obj:`~apitele.types.ForumTopicEdited`, optional
    :param forum_topic_closed: Service message: forum topic closed.
    :type forum_topic_closed: :obj:`~apitele.types.ForumTopicClosed`, optional
    :param forum_topic_reopened: Service message: forum topic reopened.
    :type forum_topic_reopened: :obj:`~apitele.types.ForumTopicReopened`, optional
    :param general_forum_topic_hidden: Service message: the 'General' forum topic hidden.
    :type general_forum_topic_hidden: :obj:`~apitele.types.GeneralForumTopicHidden`, optional
    :param general_forum_topic_unhidden: Service message: the 'General' forum topic unhidden.
    :type general_forum_topic_unhidden: :obj:`~apitele.types.GeneralForumTopicUnhidden`, optional
    :param giveaway_created: Service message: a scheduled giveaway was created.
    :type giveaway_created: :obj:`~apitele.types.GiveawayCreated`, optional
    :param giveaway: The message is a scheduled giveaway message.
    :type giveaway: :obj:`~apitele.types.Giveaway`, optional
    :param giveaway_winners: A giveaway with public winners was completed.
    :type giveaway_winners: :obj:`~apitele.types.GiveawayWinners`, optional
    :param giveaway_completed: Service message: a giveaway without public winners was completed.
    :type giveaway_completed: :obj:`~apitele.types.GiveawayCompleted`, optional
    :param paid_message_price_changed: Service message: the price for paid messages has changed in the chat.
    :type paid_message_price_changed: :obj:`~apitele.types.PaidMessagePriceChanged`, optional
    :param video_chat_scheduled: Service message: video chat scheduled.
    :type video_chat_scheduled: :obj:`~apitele.types.VideoChatScheduled`, optional
    :param video_chat_started: Service message: video chat started.
    :type video_chat_started: :obj:`~apitele.types.VideoChatStarted`, optional
    :param video_chat_ended: Service message: video chat ended.
    :type video_chat_ended: :obj:`~apitele.types.VideoChatEnded`, optional
    :param video_chat_participants_invited: Service message: new participants invited to a video chat.
    :type video_chat_participants_invited: :obj:`~apitele.types.VideoChatParticipantsInvited`, optional
    :param web_app_data: Service message: data sent by a Web App.
    :type web_app_data: :obj:`~apitele.types.WebAppData`, optional
    :param reply_markup: Inline keyboard attached to the message. ``login_url`` buttons are represented as ordinary ``url`` buttons.
    :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['message_id'] = res.get('message_id')
        obj['date'] = res.get('date')
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['message_thread_id'] = res.get('message_thread_id')
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['sender_chat'] = Chat._dese(res.get('sender_chat'))
        obj['sender_boost_count'] = res.get('sender_boost_count')
        obj['sender_business_bot'] = User._dese(res.get('sender_business_bot'))
        obj['business_connection_id'] = res.get('business_connection_id')
        obj['forward_origin'] = _dese_message_origin(res.get('forward_origin'))
        obj['is_topic_message'] = res.get('is_topic_message')
        obj['is_automatic_forward'] = res.get('is_automatic_forward')
        obj['reply_to_message'] = Message._dese(res.get('reply_to_message'))
        obj['external_reply'] = ExternalReplyInfo._dese(res.get('external_reply'))
        obj['quote'] = TextQuote._dese(res.get('quote'))
        obj['reply_to_story'] = Story._dese(res.get('reply_to_story'))
        obj['via_bot'] = User._dese(res.get('via_bot'))
        obj['edit_date'] = res.get('edit_date')
        obj['has_protected_content'] = res.get('has_protected_content')
        obj['is_from_offline'] = res.get('is_from_offline')
        obj['media_group_id'] = res.get('media_group_id')
        obj['author_signature'] = res.get('author_signature')
        obj['paid_star_count'] = res.get('paid_star_count')
        obj['text'] = res.get('text')
        obj['entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('entities')] if 'entities' in res else None
        obj['link_preview_options'] = LinkPreviewOptions._dese(res.get('link_preview_options'))
        obj['effect_id'] = res.get('effect_id')
        obj['animation'] = Animation._dese(res.get('animation'))
        obj['audio'] = Audio._dese(res.get('audio'))
        obj['document'] = Document._dese(res.get('document'))
        obj['paid_media'] = PaidMediaInfo._dese(res.get('paid_media'))
        obj['photo'] = [PhotoSize._dese(kwargs) for kwargs in res.get('photo')] if 'photo' in res else None
        obj['sticker'] = Sticker._dese(res.get('sticker'))
        obj['story'] = Story._dese(res.get('story'))
        obj['video'] = Video._dese(res.get('video'))
        obj['video_note'] = VideoNote._dese(res.get('video_note'))
        obj['voice'] = Voice._dese(res.get('voice'))
        obj['caption'] = res.get('caption')
        obj['caption_entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('caption_entities')] if 'caption_entities' in res else None
        obj['show_caption_above_media'] = res.get('show_caption_above_media')
        obj['has_media_spoiler'] = res.get('has_media_spoiler')
        obj['contact'] = Contact._dese(res.get('contact'))
        obj['dice'] = Dice._dese(res.get('dice'))
        obj['game'] = Game._dese(res.get('game'))
        obj['poll'] = Poll._dese(res.get('poll'))
        obj['venue'] = Venue._dese(res.get('venue'))
        obj['location'] = Location._dese(res.get('location'))
        obj['new_chat_members'] = [User._dese(kwargs) for kwargs in res.get('new_chat_members')] if 'new_chat_members' in res else None
        obj['left_chat_member'] = User._dese(res.get('left_chat_member'))
        obj['new_chat_title'] = res.get('new_chat_title')
        obj['new_chat_photo'] = [PhotoSize._dese(kwargs) for kwargs in res.get('new_chat_photo')] if 'new_chat_photo' in res else None
        obj['delete_chat_photo'] = res.get('delete_chat_photo')
        obj['group_chat_created'] = res.get('group_chat_created')
        obj['supergroup_chat_created'] = res.get('supergroup_chat_created')
        obj['channel_chat_created'] = res.get('channel_chat_created')
        obj['message_auto_delete_timer_changed'] = MessageAutoDeleteTimerChanged._dese(res.get('message_auto_delete_timer_changed'))
        obj['migrate_to_chat_id'] = res.get('migrate_to_chat_id')
        obj['migrate_from_chat_id'] = res.get('migrate_from_chat_id')
        obj['pinned_message'] = _dese_maybe_inaccessible_message(res.get('pinned_message'))
        obj['invoice'] = Invoice._dese(res.get('invoice'))
        obj['successful_payment'] = SuccessfulPayment._dese(res.get('successful_payment'))
        obj['refunded_payment'] = RefundedPayment._dese(res.get('refunded_payment'))
        obj['users_shared'] = UsersShared._dese(res.get('users_shared'))
        obj['chat_shared'] = ChatShared._dese(res.get('chat_shared'))
        obj['gift'] = GiftInfo._dese(res.get('gift'))
        obj['unique_gift'] = UniqueGiftInfo._dese(res.get('unique_gift'))
        obj['connected_website'] = res.get('connected_website')
        obj['write_access_allowed'] = WriteAccessAllowed._dese(res.get('write_access_allowed'))
        obj['passport_data'] = PassportData._dese(res.get('passport_data'))
        obj['proximity_alert_triggered'] = ProximityAlertTriggered._dese(res.get('proximity_alert_triggered'))
        obj['boost_added'] = ChatBoostAdded._dese(res.get('boost_added'))
        obj['chat_background_set'] = ChatBackground._dese(res.get('chat_background_set'))
        obj['forum_topic_created'] = ForumTopicCreated._dese(res.get('forum_topic_created'))
        obj['forum_topic_edited'] = ForumTopicEdited._dese(res.get('forum_topic_edited'))
        obj['forum_topic_closed'] = ForumTopicClosed._dese(res.get('forum_topic_closed'))
        obj['forum_topic_reopened'] = ForumTopicReopened._dese(res.get('forum_topic_reopened'))
        obj['general_forum_topic_hidden'] = GeneralForumTopicHidden._dese(res.get('general_forum_topic_hidden'))
        obj['general_forum_topic_unhidden'] = GeneralForumTopicUnhidden._dese(res.get('general_forum_topic_unhidden'))
        obj['giveaway_created'] = GiveawayCreated._dese(res.get('giveaway_created'))
        obj['giveaway'] = Giveaway._dese(res.get('giveaway'))
        obj['giveaway_winners'] = GiveawayWinners._dese(res.get('giveaway_winners'))
        obj['giveaway_completed'] = GiveawayCompleted._dese(res.get('giveaway_completed'))
        obj['paid_message_price_changed'] = PaidMessagePriceChanged._dese(res.get('paid_message_price_changed'))
        obj['video_chat_scheduled'] = VideoChatScheduled._dese(res.get('video_chat_scheduled'))
        obj['video_chat_started'] = VideoChatStarted._dese(res.get('video_chat_started'))
        obj['video_chat_ended'] = VideoChatEnded._dese(res.get('video_chat_ended'))
        obj['video_chat_participants_invited'] = VideoChatParticipantsInvited._dese(res.get('video_chat_participants_invited'))
        obj['web_app_data'] = WebAppData._dese(res.get('web_app_data'))
        obj['reply_markup'] = InlineKeyboardMarkup._dese(res.get('reply_markup'))
        return cls(**obj)

    def __init__(
        self,
        message_id: int,
        date: int,
        chat: Chat,
        message_thread_id: Optional[int] = None,
        from_user: Optional[User] = None,
        sender_chat: Optional[Chat] = None,
        sender_boost_count: Optional[int] = None,
        sender_business_bot: Optional[User] = None,
        business_connection_id: Optional[str] = None,
        forward_origin: Optional[MessageOrigin] = None,
        is_topic_message: Optional[Literal[True]] = None,
        is_automatic_forward: Optional[Literal[True]] = None,
        reply_to_message: Optional[Message] = None,
        external_reply: Optional[ExternalReplyInfo] = None,
        quote: Optional[TextQuote] = None,
        reply_to_story: Optional[Story] = None,
        via_bot: Optional[User] = None,
        edit_date: Optional[int] = None,
        has_protected_content: Optional[Literal[True]] = None,
        is_from_offline: Optional[Literal[True]] = None,
        media_group_id: Optional[str] = None,
        author_signature: Optional[str] = None,
        paid_star_count: Optional[int] = None,
        text: str = None,
        entities: Optional[list[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        effect_id: Optional[str] = None,
        animation: Optional[Animation] = None,
        audio: Optional[Audio] = None,
        document: Optional[Document] = None,
        paid_media: Optional[PaidMediaInfo] = None,
        photo: Optional[list[PhotoSize]] = None,
        sticker: Optional[Sticker] = None,
        story: Optional[Story] = None,
        video: Optional[Video] = None,
        video_note: Optional[VideoNote] = None,
        voice: Optional[Voice] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[Literal[True]] = None,
        has_media_spoiler: Optional[Literal[True]] = None,
        contact: Optional[Contact] = None,
        dice: Optional[Dice] = None,
        game: Optional[Game] = None,
        poll: Optional[Poll] = None,
        venue: Optional[Venue] = None,
        location: Optional[Location] = None,
        new_chat_members: Optional[list[User]] = None,
        left_chat_member: Optional[User] = None,
        new_chat_title: Optional[str] = None,
        new_chat_photo: Optional[list[PhotoSize]] = None,
        delete_chat_photo: Optional[Literal[True]] = None,
        group_chat_created: Optional[Literal[True]] = None,
        supergroup_chat_created: Optional[Literal[True]] = None,
        channel_chat_created: Optional[Literal[True]] = None,
        message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None,
        migrate_to_chat_id: Optional[int] = None,
        migrate_from_chat_id: Optional[int] = None,
        pinned_message: Optional[MaybeInaccessibleMessage] = None,
        invoice: Optional[Invoice] = None,
        successful_payment: Optional[SuccessfulPayment] = None,
        refunded_payment: Optional[RefundedPayment] = None,
        users_shared: Optional[UsersShared] = None,
        chat_shared: Optional[ChatShared] = None,
        gift: Optional[GiftInfo] = None,
        unique_gift: Optional[UniqueGiftInfo] = None,
        connected_website: Optional[str] = None,
        write_access_allowed: Optional[WriteAccessAllowed] = None,
        passport_data: Optional[PassportData] = None,
        proximity_alert_triggered: Optional[ProximityAlertTriggered] = None,
        boost_added: Optional[ChatBoostAdded] = None,
        chat_background_set: Optional[ChatBackground] = None,
        forum_topic_created: Optional[ForumTopicCreated] = None,
        forum_topic_edited: Optional[ForumTopicEdited] = None,
        forum_topic_closed: Optional[ForumTopicClosed] = None,
        forum_topic_reopened: Optional[ForumTopicReopened] = None,
        general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = None,
        general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = None,
        giveaway_created: Optional[GiveawayCreated] = None,
        giveaway: Optional[Giveaway] = None,
        giveaway_winners: Optional[GiveawayWinners] = None,
        giveaway_completed: Optional[GiveawayCompleted] = None,
        paid_message_price_changed: Optional[PaidMessagePriceChanged] = None,
        video_chat_scheduled: Optional[VideoChatScheduled] = None,
        video_chat_started: Optional[VideoChatStarted] = None,
        video_chat_ended: Optional[VideoChatEnded] = None,
        video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = None,
        web_app_data: Optional[WebAppData] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ):
        self.message_id = message_id
        self.date = date
        self.chat = chat
        self.message_thread_id = message_thread_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.sender_boost_count = sender_boost_count
        self.sender_business_bot = sender_business_bot
        self.business_connection_id = business_connection_id
        self.forward_origin = forward_origin
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.external_reply = external_reply
        self.quote = quote
        self.reply_to_story = reply_to_story
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.is_from_offline = is_from_offline
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.paid_star_count = paid_star_count
        self.text = text or str() # If not text, it's str() instead of None
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.effect_id = effect_id
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.refunded_payment = refunded_payment
        self.users_shared = users_shared
        self.chat_shared = chat_shared
        self.gift = gift
        self.unique_gift = unique_gift
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.boost_added = boost_added
        self.chat_background_set = chat_background_set
        self.forum_topic_created = forum_topic_created
        self.forum_topic_edited = forum_topic_edited
        self.forum_topic_closed = forum_topic_closed
        self.forum_topic_reopened = forum_topic_reopened
        self.general_forum_topic_hidden = general_forum_topic_hidden
        self.general_forum_topic_unhidden = general_forum_topic_unhidden
        self.giveaway_created = giveaway_created
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.giveaway_completed = giveaway_completed
        self.paid_message_price_changed = paid_message_price_changed
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup


class MessageAutoDeleteTimerChanged(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageautodeletetimerchanged

    This object represents a service message about a change in auto-delete timer settings.

    :param message_auto_delete_time: New auto-delete time for messages in the chat; in seconds.
    :type message_auto_delete_time: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['message_auto_delete_time'] = res.get('message_auto_delete_time')
        return cls(**obj)

    def __init__(
        self,
        message_auto_delete_time: int
    ):
        self.message_auto_delete_time = message_auto_delete_time


class MessageEntity(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageentity

    This object represents one special entity in a text message.
    For example, hashtags, usernames, URLs, etc.

    :param type: Type of the entity. Currently, can be “mention” (``@username``), “hashtag” (``#hashtag``), “cashtag” (``$USD``), “bot_command” (``/start@jobs_bot``), “url” (``https://telegram.org``), “email” (``do-not-reply@telegram.org``), “phone_number” (``+1-212-555-0123``), “bold” (**bold text**), “italic” (*italic text*), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “blockquote” (block quotation), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users `without usernames <https://telegram.org/blog/edit#new-mentions>`_), “custom_emoji” (for inline custom emoji stickers).
    :type type: :obj:`str`
    :param offset: Offset in `UTF-16 code units <https://core.telegram.org/api/entities#entity-length>`_ to the start of the entity.
    :type offset: :obj:`int`
    :param length: Length of the entity in `UTF-16 code units <https://core.telegram.org/api/entities#entity-length>`_.
    :type length: :obj:`int`
    :param url: For “text_link” only, URL that will be opened after user taps on the text.
    :type url: :obj:`str`, optional
    :param user: For “text_mention” only, the mentioned user.
    :type user: :obj:`~apitele.types.User`, optional
    :param language: For “pre” only, the programming language of the entity text.
    :type language: :obj:`str`, optional
    :param custom_emoji_id: For “custom_emoji” only, unique identifier of the custom emoji. Use :meth:`~apitele.Client.get_custom_emoji_stickers` to get full information about the sticker.
    :type custom_emoji_id: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['type'] = res.get('type')
        obj['offset'] = res.get('offset')
        obj['length'] = res.get('length')
        obj['url'] = res.get('url')
        obj['user'] = User._dese(res.get('user'))
        obj['language'] = res.get('language')
        obj['custom_emoji_id'] = res.get('custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        type: str,
        offset: int,
        length: int,
        url: Optional[str] = None,
        user: Optional[User] = None,
        language: Optional[str] = None,
        custom_emoji_id: Optional[str] = None
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id


class MessageId(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageid

    This object represents a unique message identifier.

    :param message_id: Unique message identifier.
    :type message_id: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['message_id'] = res.get('message_id')
        return cls(**obj)

    def __init__(
        self,
        message_id: int
    ):
        self.message_id = message_id


class MessageOriginChannel(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageoriginchannel

    The message was originally sent to a channel chat.

    :param date: Date the message was sent originally in Unix time.
    :type date: :obj:`int`
    :param chat: Channel chat to which the message was originally sent.
    :type chat: :obj:`~apitele.types.Chat`
    :param message_id: Unique message identifier inside the chat.
    :type message_id: :obj:`int`
    :param author_signature: Signature of the original post author.
    :type author_signature: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['date'] = res.get('date')
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['message_id'] = res.get('message_id')
        obj['author_signature'] = res.get('author_signature')
        return cls(**obj)

    def __init__(
        self,
        date: int,
        chat: Chat,
        message_id: int,
        author_signature: Optional[str] = None
    ):
        self.type = DEFAULT_MESSAGE_ORIGIN_CHANNEL
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature


class MessageOriginChat(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageoriginchat

    The message was originally sent on behalf of a chat to a group chat.

    :param date: Date the message was sent originally in Unix time.
    :type date: :obj:`int`
    :param sender_chat: Chat that sent the message originally.
    :type sender_chat: :obj:`~apitele.types.Chat`
    :param author_signature: For messages originally sent by an anonymous chat administrator, original message author signature.
    :type author_signature: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['date'] = res.get('date')
        obj['sender_chat'] = Chat._dese(res.get('sender_chat'))
        obj['author_signature'] = res.get('author_signature')
        return cls(**obj)

    def __init__(
        self,
        date: int,
        sender_chat: Chat,
        author_signature: Optional[str] = None
    ):
        self.type = DEFAULT_MESSAGE_ORIGIN_CHAT
        self.date = date
        self.sender_chat = sender_chat
        self.author_signature = author_signature


class MessageOriginHiddenUser(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageoriginhiddenuser

    The message was originally sent by an unknown user.

    :param date: Date the message was sent originally in Unix time.
    :type date: :obj:`int`
    :param sender_user_name: Name of the user that sent the message originally.
    :type sender_user_name: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['date'] = res.get('date')
        obj['sender_user_name'] = res.get('sender_user_name')
        return cls(**obj)

    def __init__(
        self,
        date: int,
        sender_user_name: str
    ):
        self.type = DEFAULT_MESSAGE_ORIGIN_HIDDEN_USER
        self.date = date
        self.sender_user_name = sender_user_name


class MessageOriginUser(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageoriginuser

    The message was originally sent by a known user.

    :param date: Date the message was sent originally in Unix time.
    :type date: :obj:`int`
    :param sender_user: User that sent the message originally.
    :type sender_user: :obj:`~apitele.types.User`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['date'] = res.get('date')
        obj['sender_user'] = User._dese(res.get('sender_user'))
        return cls(**obj)

    def __init__(
        self,
        date: int,
        sender_user: User
    ):
        self.type = DEFAULT_MESSAGE_ORIGIN_USER
        self.date = date
        self.sender_user = sender_user


class MessageReactionCountUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#messagereactioncountupdated

    This object represents reaction changes on a message with anonymous reactions.

    :param chat: The chat containing the message.
    :type chat: :obj:`~apitele.types.Chat`
    :param message_id: Unique message identifier inside the chat.
    :type message_id: :obj:`int`
    :param date: Date of the change in Unix time.
    :type date: :obj:`int`
    :param reactions: List of reactions that are present on the message.
    :type reactions: :obj:`list` of :obj:`~apitele.types.ReactionCount`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['message_id'] = res.get('message_id')
        obj['date'] = res.get('date')
        obj['reactions'] = [ReactionCount._dese(kwargs) for kwargs in res.get('reactions')]
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        message_id: int,
        date: int,
        reactions: list[ReactionCount]
    ):
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions


class MessageReactionUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#messagereactionupdated

    This object represents a change of a reaction on a message performed by a user.

    :param chat: The chat containing the message the user reacted to.
    :type chat: :obj:`~apitele.types.Chat`
    :param message_id: Unique identifier of the message inside the chat.
    :type message_id: :obj:`int`
    :param date: Date of the change in Unix time.
    :type date: :obj:`int`
    :param old_reaction: Previous list of reaction types that were set by the user.
    :type old_reaction: :obj:`list` of :obj:`~apitele.types.ReactionType`
    :param new_reaction: New list of reaction types that have been set by the user.
    :type new_reaction: :obj:`list` of :obj:`~apitele.types.ReactionType`
    :param user: The user that changed the reaction, if the user isn't anonymous.
    :type user: :obj:`~apitele.types.User`, optional
    :param actor_chat: The chat on behalf of which the reaction was changed, if the user is anonymous.
    :type actor_chat: :obj:`~apitele.types.Chat`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['message_id'] = res.get('message_id')
        obj['date'] = res.get('date')
        obj['old_reaction'] = [_dese_reaction_type(kwargs) for kwargs in res.get('old_reaction')]
        obj['new_reaction'] = [_dese_reaction_type(kwargs) for kwargs in res.get('new_reaction')]
        obj['user'] = User._dese(res.get('user'))
        obj['actor_chat'] = Chat._dese(res.get('actor_chat'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        message_id: int,
        date: int,
        old_reaction: list[ReactionType],
        new_reaction: list[ReactionType],
        user: Optional[User] = None,
        actor_chat: Optional[Chat] = None
    ):
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction
        self.user = user
        self.actor_chat = actor_chat


class OrderInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#orderinfo

    This object represents information about an order.

    :param name: User name.
    :type name: :obj:`str`, optional
    :param phone_number: User's phone number.
    :type phone_number: :obj:`str`, optional
    :param email: User email.
    :type email: :obj:`str`, optional
    :param shipping_address: User shipping address.
    :type shipping_address: :obj:`~apitele.types.ShippingAddress`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        obj['phone_number'] = res.get('phone_number')
        obj['email'] = res.get('email')
        obj['shipping_address'] = ShippingAddress._dese(res.get('shipping_address'))
        return cls(**obj)

    def __init__(
        self,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        shipping_address: Optional[ShippingAddress] = None
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address


class OwnedGiftRegular(TelegramType):
    '''
    https://core.telegram.org/bots/api#ownedgiftregular

    Describes a regular gift owned by a user or a chat.

    :param gift: Information about the regular gift.
    :type gift: :obj:`~apitele.types.Gift`
    :param send_date: Date the gift was sent in Unix time.
    :type send_date: :obj:`int`
    :param owned_gift_id: Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only.
    :type owned_gift_id: :obj:`str`, optional
    :param sender_user: Sender of the gift if it is a known user.
    :type sender_user: :obj:`~apitele.types.User`, optional
    :param text: Text of the message that was added to the gift.
    :type text: :obj:`str`, optional
    :param entities: Special entities that appear in the text.
    :type entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param is_private: :obj:`True`, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them.
    :type is_private: :obj:`True`, optional
    :param is_saved: :obj:`True`, if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only.
    :type is_saved: :obj:`True`, optional
    :param can_be_upgraded: :obj:`True`, if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only.
    :type can_be_upgraded: :obj:`True`, optional
    :param was_refunded: :obj:`True`, if the gift was refunded and isn't available anymore.
    :type was_refunded: :obj:`True`, optional
    :param convert_star_count: Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars.
    :type convert_star_count: :obj:`int`, optional
    :param prepaid_upgrade_star_count: Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift.
    :type prepaid_upgrade_star_count: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['gift'] = Gift._dese(res.get('gift'))
        obj['send_date'] = res.get('send_date')
        obj['owned_gift_id'] = res.get('owned_gift_id')
        obj['sender_user'] = User._dese(res.get('sender_user'))
        obj['text'] = res.get('text')
        obj['entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('entities')] if 'entities' in res else None
        obj['is_private'] = res.get('is_private')
        obj['is_saved'] = res.get('is_saved')
        obj['can_be_upgraded'] = res.get('can_be_upgraded')
        obj['was_refunded'] = res.get('was_refunded')
        obj['convert_star_count'] = res.get('convert_star_count')
        obj['prepaid_upgrade_star_count'] = res.get('prepaid_upgrade_star_count')
        return cls(**obj)

    def __init__(
        self,
        gift: Gift,
        send_date: int,
        owned_gift_id: Optional[str] = None,
        sender_user: Optional[User] = None,
        text: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        is_private: Optional[Literal[True]] = None,
        is_saved: Optional[Literal[True]] = None,
        can_be_upgraded: Optional[Literal[True]] = None,
        was_refunded: Optional[Literal[True]] = None,
        convert_star_count: Optional[int] = None,
        prepaid_upgrade_star_count: Optional[int] = None
    ):
        self.type = DEFAULT_OWNED_GIFT_REGULAR
        self.gift = gift
        self.send_date = send_date
        self.owned_gift_id = owned_gift_id
        self.sender_user = sender_user
        self.text = text
        self.entities = entities
        self.is_private = is_private
        self.is_saved = is_saved
        self.can_be_upgraded = can_be_upgraded
        self.was_refunded = was_refunded
        self.convert_star_count = convert_star_count
        self.prepaid_upgrade_star_count = prepaid_upgrade_star_count


class OwnedGiftUnique(TelegramType):
    '''
    https://core.telegram.org/bots/api#ownedgiftunique

    Describes a unique gift received and owned by a user or a chat.

    :param gift: Information about the unique gift.
    :type gift: :obj:`~apitele.types.UniqueGift`
    :param send_date: Date the gift was sent in Unix time.
    :type send_date: :obj:`int`
    :param owned_gift_id: Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only.
    :type owned_gift_id: :obj:`str`, optional
    :param sender_user: Sender of the gift if it is a known user.
    :type sender_user: :obj:`~apitele.types.User`, optional
    :param is_saved: :obj:`True`, if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only.
    :type is_saved: :obj:`True`, optional
    :param can_be_transferred: :obj:`True`, if the gift can be transferred to another owner; for gifts received on behalf of business accounts only.
    :type can_be_transferred: :obj:`True`, optional
    :param transfer_star_count: Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift.
    :type transfer_star_count: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['gift'] = UniqueGift._dese(res.get('gift'))
        obj['send_date'] = res.get('send_date')
        obj['owned_gift_id'] = res.get('owned_gift_id')
        obj['sender_user'] = User._dese(res.get('sender_user'))
        obj['is_saved'] = res.get('is_saved')
        obj['can_be_transferred'] = res.get('can_be_transferred')
        obj['transfer_star_count'] = res.get('transfer_star_count')
        return cls(**obj)

    def __init__(
        self,
        gift: UniqueGift,
        send_date: int,
        owned_gift_id: Optional[str] = None,
        sender_user: Optional[User] = None,
        is_saved: Optional[Literal[True]] = None,
        can_be_transferred: Optional[Literal[True]] = None,
        transfer_star_count: Optional[int] = None
    ):
        self.type = DEFAULT_OWNED_GIFT_UNIQUE
        self.gift = gift
        self.send_date = send_date
        self.owned_gift_id = owned_gift_id
        self.sender_user = sender_user
        self.is_saved = is_saved
        self.can_be_transferred = can_be_transferred
        self.transfer_star_count = transfer_star_count


class OwnedGifts(TelegramType):
    '''
    https://core.telegram.org/bots/api#ownedgifts

    Contains the list of gifts received and owned by a user or a chat.

    :param total_count: The total number of gifts owned by the user or the chat.
    :type total_count: :obj:`int`
    :param gifts: The list of gifts.
    :type gifts: :obj:`list` of :obj:`~apitele.types.OwnedGift`
    :param next_offset: Offset for the next request. If empty, then there are no more results.
    :type next_offset: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['total_count'] = res.get('total_count')
        obj['gifts'] = [_dese_owned_gift(kwargs) for kwargs in res.get('gifts')]
        obj['next_offset'] = res.get('next_offset')
        return cls(**obj)

    def __init__(
        self,
        total_count: int,
        gifts: list[OwnedGift],
        next_offset: Optional[str] = None
    ):
        self.total_count = total_count
        self.gifts = gifts
        self.next_offset = next_offset


class PaidMediaInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#paidmediainfo

    Describes the paid media added to a message.

    :param star_count: The number of Telegram Stars that must be paid to buy access to the media.
    :type star_count: :obj:`int`
    :param paid_media: Information about the paid media.
    :type paid_media: :obj:`list` of :obj:`~apitele.types.PaidMedia`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['star_count'] = res.get('star_count')
        obj['paid_media'] = [_dese_paid_media(kwargs) for kwargs in res.get('paid_media')]
        return cls(**obj)

    def __init__(
        self,
        star_count: int,
        paid_media: list[PaidMedia]
    ):
        self.star_count = star_count
        self.paid_media = paid_media


class PaidMediaPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#paidmediaphoto

    The paid media is a photo.

    :param photo: The photo.
    :type photo: :obj:`list` of :obj:`~apitele.types.PhotoSize`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['photo'] = [PhotoSize._dese(kwargs) for kwargs in res.get('photo')]
        return cls(**obj)

    def __init__(
        self,
        photo: list[PhotoSize]
    ):
        self.photo = photo


class PaidMediaPreview(TelegramType):
    '''
    https://core.telegram.org/bots/api#paidmediapreview

    The paid media isn't available before the payment.

    :param width: Media width as defined by the sender.
    :type width: :obj:`int`, optional
    :param height: Media height as defined by the sender.
    :type height: :obj:`int`, optional
    :param duration: Duration of the media in seconds as defined by the sender.
    :type duration: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['width'] = res.get('width')
        obj['height'] = res.get('height')
        obj['duration'] = res.get('duration')
        return cls(**obj)

    def __init__(
        self,
        width: Optional[int],
        height: Optional[int],
        duration: Optional[int]
    ):
        self.width = width
        self.height = height
        self.duration = duration


class PaidMediaPurchased(TelegramType):
    '''
    https://core.telegram.org/bots/api#paidmediapurchased

    This object contains information about a paid media purchase.

    :param from_user: User who purchased the media.
    :type from_user: :obj:`~apitele.types.User`
    :param paid_media_payload: Bot-specified paid media payload.
    :type paid_media_payload: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['paid_media_payload'] = res.get('paid_media_payload')
        return cls(**obj)

    def __init__(
        self,
        from_user: User,
        paid_media_payload: str
    ):
        self.from_user = from_user
        self.paid_media_payload = paid_media_payload


class PaidMediaVideo(TelegramType):
    '''
    https://core.telegram.org/bots/api#paidmediavideo

    The paid media is a video.

    :param video: The video.
    :type video: :obj:`~apitele.types.Video`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['video'] = Video._dese(res.get('video'))
        return cls(**obj)

    def __init__(
        self,
        video: Video
    ):
        self.video = video


class PaidMessagePriceChanged(TelegramType):
    '''
    https://core.telegram.org/bots/api#paidmessagepricechanged

    Describes a service message about a change in the price of paid messages within a chat.

    :param paid_message_star_count: The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message.
    :type paid_message_star_count: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['paid_message_star_count'] = res.get('paid_message_star_count')
        return cls(**obj)

    def __init__(
        self,
        paid_message_star_count: int
    ):
        self.paid_message_star_count = paid_message_star_count


class PassportData(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportdata

    Describes Telegram Passport data shared with the bot by the user.

    :param data: Array with information about documents and other Telegram Passport elements that was shared with the bot.
    :type data: :obj:`list` of :obj:`~apitele.types.EncryptedPassportElement`
    :param credentials: Encrypted credentials required to decrypt the data.
    :type credentials: :obj:`~apitele.types.EncryptedCredentials`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['data'] = [EncryptedPassportElement._dese(kwargs) for kwargs in res.get('data')]
        obj['credentials'] = EncryptedCredentials._dese(res.get('credentials'))
        return cls(**obj)

    def __init__(
        self,
        data: list[EncryptedPassportElement],
        credentials: EncryptedCredentials
    ):
        self.data = data
        self.credentials = credentials


class PassportElementErrorDataField(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrordatafield

    Represents an issue in one of the data fields that was provided by the user.
    The error is considered resolved when the field's value changes.

    :param type: The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”.
    :type type: :obj:`str`
    :param field_name: Name of the data field which has the error.
    :type field_name: :obj:`str`
    :param data_hash: Base64-encoded data hash.
    :type data_hash: :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        field_name: str,
        data_hash: str,
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_DATA_FIELD
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message


class PassportElementErrorFile(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrorfile

    Represents an issue with a document scan.
    The error is considered resolved when the file with the document scan changes.

    :param type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
    :type type: :obj:`str`
    :param file_hash: Base64-encoded file hash.
    :type file_hash: :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        file_hash: str,
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_FILE
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorFiles(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrorfiles

    Represents an issue with a list of scans.
    The error is considered resolved when the list of files containing the scans changes.

    :param type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
    :type type: :obj:`str`
    :param file_hashes: List of base64-encoded file hashes.
    :type file_hashes: :obj:`list` of :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        file_hashes: list[str],
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_FILES
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorFrontSide(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrorfrontside

    Represents an issue with the front side of a document.
    The error is considered resolved when the file with the front side of the document changes.

    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”.
    :type type: :obj:`str`
    :param file_hash: Base64-encoded hash of the file with the front side of the document.
    :type file_hash: :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        file_hash: str,
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_FRONT_SIDE
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorReverseSide(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrorreverseside

    Represents an issue with the reverse side of a document.
    The error is considered resolved when the file with reverse side of the document changes.

    :param type: The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”.
    :type type: :obj:`str`
    :param file_hash: Base64-encoded hash of the file with the reverse side of the document.
    :type file_hash: :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        file_hash: str,
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_REVERSE_SIDE
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorSelfie(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrorselfie

    Represents an issue with the selfie with a document.
    The error is considered resolved when the file with the selfie changes.

    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”.
    :type type: :obj:`str`
    :param file_hash: Base64-encoded hash of the file with the selfie.
    :type file_hash: :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        file_hash: str,
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_SELFIE
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorTranslationFile(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrortranslationfile

    Represents an issue with one of the files that constitute the translation of a document.
    The error is considered resolved when the file changes.

    :param type: Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
    :type type: :obj:`str`
    :param file_hash: Base64-encoded file hash.
    :type file_hash: :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        file_hash: str,
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILE
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorTranslationFiles(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrortranslationfiles

    Represents an issue with the translated version of a document.
    The error is considered resolved when a file with the document translation change.

    :param type: Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
    :type type: :obj:`str`
    :param file_hashes: List of base64-encoded file hashes.
    :type file_hashes: :obj:`list` of :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        file_hashes: list[str],
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILES
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorUnspecified(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerrorunspecified

    Represents an issue in an unspecified place.
    The error is considered resolved when new data is added.

    :param type: Type of element of the user's Telegram Passport which has the issue.
    :type type: :obj:`str`
    :param element_hash: Base64-encoded element hash.
    :type element_hash: :obj:`str`
    :param message: Error message.
    :type message: :obj:`str`
    '''
    def __init__(
        self,
        type: str,
        element_hash: str,
        message: str
    ):
        self.source = DEFAULT_PASSPORT_ELEMENT_ERROR_UNSPECIFIED
        self.type = type
        self.element_hash = element_hash
        self.message = message


class PassportFile(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportfile

    This object represents a file uploaded to Telegram Passport.
    Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param file_size: File size in bytes.
    :type file_size: :obj:`int`
    :param file_date: Unix time when the file was uploaded.
    :type file_date: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['file_size'] = res.get('file_size')
        obj['file_date'] = res.get('file_date')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_size: int,
        file_date: int
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date


class PhotoSize(TelegramType):
    '''
    https://core.telegram.org/bots/api#photosize

    This object represents one size of a photo or a
    :obj:`file <apitele.types.Document>` / :obj:`sticker <apitele.types.Sticker>` thumbnail.

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param width: Photo width.
    :type width: :obj:`int`
    :param height: Photo height.
    :type height: :obj:`int`
    :param file_size: File size in bytes.
    :type file_size: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['width'] = res.get('width')
        obj['height'] = res.get('height')
        obj['file_size'] = res.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        file_size: Optional[int] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size


class Poll(TelegramType):
    '''
    https://core.telegram.org/bots/api#poll

    This object contains information about a poll.

    :param id: Unique poll identifier.
    :type id: :obj:`str`
    :param question: Poll question, 1-300 characters.
    :type question: :obj:`str`
    :param options: List of poll options.
    :type options: :obj:`list` of :obj:`~apitele.types.PollOption`
    :param total_voter_count: Total number of users that voted in the poll.
    :type total_voter_count: :obj:`int`
    :param is_closed: :obj:`True`, if the poll is closed.
    :type is_closed: :obj:`bool`
    :param is_anonymous: :obj:`True`, if the poll is anonymous.
    :type is_anonymous: :obj:`bool`
    :param type: Poll type, currently can be “regular” or “quiz”.
    :type type: :obj:`str`
    :param allows_multiple_answers: :obj:`True`, if the poll allows multiple answers.
    :type allows_multiple_answers: :obj:`bool`
    :param question_entities: Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions.
    :type question_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param correct_option_id: 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    :type correct_option_id: :obj:`int`, optional
    :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters.
    :type explanation: :obj:`str`, optional
    :param explanation_entities: Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation*.
    :type explanation_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param open_period: Amount of time in seconds the poll will be active after creation.
    :type open_period: :obj:`int`, optional
    :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed.
    :type close_date: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['question'] = res.get('question')
        obj['options'] = [PollOption._dese(kwargs) for kwargs in res.get('options')]
        obj['total_voter_count'] = res.get('total_voter_count')
        obj['is_closed'] = res.get('is_closed')
        obj['is_anonymous'] = res.get('is_anonymous')
        obj['type'] = res.get('type')
        obj['allows_multiple_answers'] = res.get('allows_multiple_answers')
        obj['question_entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('question_entities')] if 'question_entities' in res else None
        obj['correct_option_id'] = res.get('correct_option_id')
        obj['explanation'] = res.get('explanation')
        obj['explanation_entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('explanation_entities')] if 'explanation_entities' in res else None
        obj['open_period'] = res.get('open_period')
        obj['close_date'] = res.get('close_date')
        return cls(**obj)

    def __init__(
        self,
        id: str,
        question: str,
        options: list[PollOption],
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool,
        type: str,
        allows_multiple_answers: bool,
        question_entities: Optional[list[MessageEntity]] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_entities: Optional[list[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None
    ):
        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.question_entities = question_entities
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date


class PollAnswer(TelegramType):
    '''
    https://core.telegram.org/bots/api#pollanswer

    This object represents an answer of a user in a non-anonymous poll.

    :param poll_id: Unique poll identifier.
    :type poll_id: :obj:`str`
    :param option_ids: 0-based identifiers of chosen answer options. May be empty if the vote was retracted.
    :type option_ids: :obj:`list` of :obj:`int`
    :param voter_chat: The chat that changed the answer to the poll, if the voter is anonymous.
    :type voter_chat: :obj:`~apitele.types.Chat`, optional
    :param user: The user that changed the answer to the poll, if the voter isn't anonymous.
    :type user: :obj:`~apitele.types.User`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['poll_id'] = res.get('poll_id')
        obj['option_ids'] = res.get('option_ids')
        obj['voter_chat'] = Chat._dese(res.get('voter_chat'))
        obj['user'] = User._dese(res.get('user'))
        return cls(**obj)

    def __init__(
        self,
        poll_id: str,
        option_ids: list[int],
        voter_chat: Optional[Chat] = None,
        user: Optional[User] = None
    ):
        self.poll_id = poll_id
        self.option_ids = option_ids
        self.voter_chat = voter_chat
        self.user = user


class PollOption(TelegramType):
    '''
    https://core.telegram.org/bots/api#polloption

    This object contains information about one answer option in a poll.

    :param text: Option text, 1-100 characters.
    :type text: :obj:`str`
    :param voter_count: Number of users that voted for this option.
    :type voter_count: :obj:`int`
    :param text_entities: Special entities that appear in the option *text*. Currently, only custom emoji entities are allowed in poll option texts.
    :type text_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['text'] = res.get('text')
        obj['voter_count'] = res.get('voter_count')
        obj['text_entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('text_entities')] if 'text_entities' in res else None
        return cls(**obj)

    def __init__(
        self,
        text: str,
        voter_count: int,
        text_entities: Optional[list[MessageEntity]] = None
    ):
        self.text = text
        self.voter_count = voter_count
        self.text_entities = text_entities


class PreCheckoutQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#precheckoutquery

    This object contains information about an incoming pre-checkout query.

    :param id: Unique query identifier.
    :type id: :obj:`str`
    :param from_user: User who sent the query.
    :type from_user: :obj:`~apitele.types.User`
    :param currency: Three-letter ISO 4217 `currency <https://core.telegram.org/bots/payments#supported-currencies>`_ code.
    :type currency: :obj:`str`
    :param total_amount: Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of ``US$ 1.45`` pass ``amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`
    :param invoice_payload: Bot specified invoice payload.
    :type invoice_payload: :obj:`str`
    :param shipping_option_id: Identifier of the shipping option chosen by the user.
    :type shipping_option_id: :obj:`str`, optional
    :param order_info: Order information provided by the user.
    :type order_info: :obj:`~apitele.types.OrderInfo`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['currency'] = res.get('currency')
        obj['total_amount'] = res.get('total_amount')
        obj['invoice_payload'] = res.get('invoice_payload')
        obj['shipping_option_id'] = res.get('shipping_option_id')
        obj['order_info'] = OrderInfo._dese(res.get('order_info'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        shipping_option_id: Optional[str] = None,
        order_info: Optional[OrderInfo] = None
    ):
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info


class PreparedInlineMessage(TelegramType):
    '''
    https://core.telegram.org/bots/api#preparedinlinemessage

    Describes an inline message to be sent by a user of a Mini App.

    :param id: Unique identifier of the prepared message.
    :type id: :obj:`str`
    :param expiration_date: Expiration date of the prepared message, in Unix time. Expired prepared messages can no longer be used.
    :type expiration_date: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res:dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['expiration_date'] = res.get('expiration_date')
        return cls(**obj)

    def __init__(
        self,
        id: str,
        expiration_date: int
    ):
        self.id = id
        self.expiration_date  = expiration_date


class ProximityAlertTriggered(TelegramType):
    '''
    https://core.telegram.org/bots/api#proximityalerttriggered

    This object represents the content of a service message, sent whenever
    a user in the chat triggers a proximity alert set by another user.

    :param traveler: User that triggered the alert.
    :type traveler: :obj:`~apitele.types.User`
    :param watcher: User that set the alert.
    :type watcher: :obj:`~apitele.types.User`
    :param distance: The distance between the users.
    :type distance: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['traveler'] = User._dese(res.get('traveler'))
        obj['watcher'] = User._dese(res.get('watcher'))
        obj['distance'] = res.get('distance')
        return cls(**obj)

    def __init__(
        self,
        traveler: User,
        watcher: User,
        distance: int
    ):
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance


class ReactionCount(TelegramType):
    '''
    https://core.telegram.org/bots/api#reactioncount

    Represents a reaction added to a message along with the number of times it was added.

    :param type: Type of the reaction.
    :type type: :obj:`~apitele.types.ReactionType`
    :param total_count: Number of times the reaction was added.
    :type total_count: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['type'] = _dese_reaction_type(res.get('type'))
        obj['total_count'] = res.get('total_count')
        return cls(**obj)

    def __init__(
        self,
        type: ReactionType,
        total_count: int
    ):
        self.type = type
        self.total_count = total_count


class ReactionTypeCustomEmoji(TelegramType):
    '''
    https://core.telegram.org/bots/api#reactiontypecustomemoji

    The reaction is based on a custom emoji.

    :param custom_emoji_id: Custom emoji identifier.
    :type custom_emoji_id: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['custom_emoji_id'] = res.get('custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        custom_emoji_id: str
    ):
        self.type = DEFAULT_REACTION_TYPE_CUSTOM_EMOJI
        self.custom_emoji_id = custom_emoji_id


class ReactionTypeEmoji(TelegramType):
    '''
    https://core.telegram.org/bots/api#reactiontypeemoji

    The reaction is based on an emoji.

    :param emoji: Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡".
    :type emoji: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['emoji'] = res.get('emoji')
        return cls(**obj)

    def __init__(
        self,
        emoji: str
    ):
        self.type = DEFAULT_REACTION_TYPE_EMOJI
        self.emoji = emoji


class ReactionTypePaid(TelegramType):
    '''
    https://core.telegram.org/bots/api#reactiontypepaid

    The reaction is paid.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        self.type = DEFAULT_REACTION_TYPE_PAID


class RefundedPayment(TelegramType):
    '''
    https://core.telegram.org/bots/api#refundedpayment

    This object contains basic information about a refunded payment.

    :param currency: Three-letter ISO 4217 `currency <https://core.telegram.org/bots/payments#supported-currencies>`_ code, or “XTR” for payments in `Telegram Stars <https://t.me/BotNews/90>`_. Currently, always “XTR”.
    :type currency: :obj:`str`
    :param total_amount: Total refunded price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of ``US$ 1.45``, ``total_amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`
    :param invoice_payload: Bot-specified invoice payload.
    :type invoice_payload: :obj:`str`
    :param telegram_payment_charge_id: Telegram payment identifier.
    :type telegram_payment_charge_id: :obj:`str`
    :param provider_payment_charge_id: Provider payment identifier.
    :type provider_payment_charge_id: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['currency'] = res.get('currency')
        obj['total_amount'] = res.get('total_amount')
        obj['invoice_payload'] = res.get('invoice_payload')
        obj['telegram_payment_charge_id'] = res.get('telegram_payment_charge_id')
        obj['provider_payment_charge_id'] = res.get('provider_payment_charge_id')
        return cls(**obj)

    def __init__(
        self,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        telegram_payment_charge_id: str,
        provider_payment_charge_id: Optional[str] = None
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id


class ReplyKeyboardMarkup(TelegramType):
    '''
    https://core.telegram.org/bots/api#replykeyboardmarkup

    This object represents a `custom keyboard <https://core.telegram.org/bots/features#keyboards>`_ with reply
    options (see `Introduction to bots <https://core.telegram.org/bots/features#keyboards>`_ for details and examples).

    :param keyboard: Array of button rows, each represented by an Array of :obj:`~apitele.types.KeyboardButton` objects.
    :type keyboard: :obj:`list` of :obj:`list` of :obj:`~apitele.types.KeyboardButton`, optional
    :param is_persistent: Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to :obj:`False`, in which case the custom keyboard can be hidden and opened with a keyboard icon.
    :type is_persistent: :obj:`bool`, optional
    :param resize_keyboard: Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to :obj:`False`, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    :type resize_keyboard: :obj:`bool`, optional
    :param one_time_keyboard: Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to :obj:`False`.
    :type one_time_keyboard: :obj:`bool`, optional
    :param input_field_placeholder: The placeholder to be shown in the input field when the keyboard is active; 1-64 characters.
    :type input_field_placeholder: :obj:`str`, optional
    :param selective:
        Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the *text* of the :obj:`~apitele.types.Message` object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.

        *Example*: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
    :type selective: :obj:`bool`, optional
    '''
    def __init__(
        self,
        keyboard: Optional[list[list[KeyboardButton]]] = None,
        is_persistent: Optional[bool] = None,
        resize_keyboard: Optional[bool] = None,
        one_time_keyboard: Optional[bool] = None,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None
    ):
        self.keyboard = keyboard or []
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    def add(self, *buttons: Union[KeyboardButton, str]) -> Self:
        '''
        Usage:

        .. code-block:: python3

            markup = ReplyKeyboardMarkup()
            markup.add(
                KeyboardButton('x'),
                KeyboardButton('y'),
                KeyboardButton('z')
            )
            # All the buttons added with this method will be in
            # the same row, you can change the row width after the
            # object initialization using the property setter 'row_width'.

        :param buttons: :obj:`KeyboardButtons <apitele.types.KeyboardButton>` to add to a new row of the *keyboard*. For simple text buttons, you can pass a :obj:`String` instead of a :obj:`~apitele.types.KeyboardButton` object to specify the button text.
        :type buttons: \*\ :obj:`~apitele.types.KeyboardButton` or \*\ :obj:`str`
        :rtype: :obj:`~apitele.types.ReplyKeyboardMarkup`
        '''
        self.keyboard.append(buttons)
        return self

    @property
    def row_width(self) -> int:
        '''
        Usage:

        .. code-block:: python3

            markup.row_width = 2
            # The keyboard will be rearranged with 2 buttons for each row.
        '''
        row_width = 0
        for nested in self.keyboard:
            if len(nested) > row_width:
                row_width = len(nested)
        return row_width

    @row_width.setter
    def row_width(self, value: int) -> None:

        keyboard = []
        nested = []
        for row in self.keyboard:
            for button in row:
                nested.append(button)
                if len(nested) == value:
                    keyboard.append(nested)
                    nested = []

        if nested:
            keyboard.append(nested)

        self.keyboard = keyboard


class ReplyKeyboardRemove(TelegramType):
    '''
    https://core.telegram.org/bots/api#replykeyboardremove

    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard
    and display the default letter-keyboard. By default, custom keyboards are displayed until a new
    keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately
    after the user presses a button (see :obj:`~apitele.types.ReplyKeyboardMarkup`).

    :param selective:
        Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the *text* of the :obj:`~apitele.types.Message` object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.

        *Example*: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    :type selective: :obj:`bool`, optional
    '''
    def __init__(
        self,
        selective: Optional[bool] = None
    ):
        self.remove_keyboard: Literal[True] = True
        self.selective = selective


class ReplyParameters(TelegramType):
    '''
    https://core.telegram.org/bots/api#replyparameters

    Describes reply parameters for the message that is being sent.

    :param message_id: Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified.
    :type message_id: :obj:`int`
    :param chat_id: If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format ``@channelusername``). Not supported for messages sent on behalf of a business account.
    :type chat_id: :obj:`int` or :obj:`str`, optional
    :param allow_sending_without_reply: Pass :obj:`True` if the message should be sent even if the specified message to be replied to is not found. Always :obj:`False` for replies in another chat or forum topic. Always :obj:`True` for messages sent on behalf of a business account.
    :type allow_sending_without_reply: :obj:`bool`, optional
    :param quote: Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom_emoji entities*. The message will fail to send if the quote isn't found in the original message.
    :type quote: :obj:`str`, optional
    :param quote_parse_mode: Mode for parsing entities in the quote. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    :type quote_parse_mode: :obj:`str`, optional
    :param quote_entities: A JSON-serialized list of special entities that appear in the quote. It can be specified instead of *quote_parse_mode*.
    :type quote_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param quote_position: Position of the quote in the original message in UTF-16 code units.
    :type quote_position: :obj:`int`, optional
    '''
    def __init__(
        self,
        message_id: int,
        chat_id: Optional[Union[int, str]] = None,
        allow_sending_without_reply: Optional[bool] = None,
        quote: Optional[str] = None,
        quote_parse_mode: Optional[str] = None,
        quote_entities: Optional[list[MessageEntity]] = None,
        quote_position: Optional[int] = None
    ):
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position


class ResponseParameters(TelegramType):
    '''
    https://core.telegram.org/bots/api#responseparameters

    Describes why a request was unsuccessful.

    :param migrate_to_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :type migrate_to_chat_id: :obj:`int`, optional
    :param retry_after: In case of exceeding flood control, the number of seconds left to wait before the request can be repeated.
    :type retry_after: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['migrate_to_chat_id'] = res.get('migrate_to_chat_id')
        obj['retry_after'] = res.get('retry_after')
        return cls(**obj)

    def __init__(
        self,
        migrate_to_chat_id: Optional[int] = None,
        retry_after: Optional[int] = None
    ):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after


class RevenueWithdrawalStateFailed(TelegramType):
    '''
    https://core.telegram.org/bots/api#revenuewithdrawalstatefailed

    The withdrawal failed and the transaction was refunded.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        self.type = DEFAULT_REVENUE_WITHDRAWAL_STATE_FAILED


class RevenueWithdrawalStatePending(TelegramType):
    '''
    https://core.telegram.org/bots/api#revenuewithdrawalstatepending

    The withdrawal is in progress.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        self.type = DEFAULT_REVENUE_WITHDRAWAL_STATE_PENDING


class RevenueWithdrawalStateSucceeded(TelegramType):
    '''
    https://core.telegram.org/bots/api#revenuewithdrawalstatesucceeded

    The withdrawal succeeded.

    :param date: Date the withdrawal was completed in Unix time.
    :type date: :obj:`int`
    :param url: An HTTPS URL that can be used to see transaction details.
    :type url: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['date'] = res.get('date')
        obj['url'] = res.get('url')
        return cls(**obj)

    def __init__(
        self,
        date: int,
        url: str
    ):
        self.type = DEFAULT_REVENUE_WITHDRAWAL_STATE_SUCCEEDED
        self.date = date
        self.url = url


class SentWebAppMessage(TelegramType):
    '''
    https://core.telegram.org/bots/api#sentwebappmessage

    Describes an inline message sent by a `Web App <https://core.telegram.org/bots/webapps>`_ on behalf of a user.

    :param inline_message_id: Identifier of the sent inline message. Available only if there is an :obj:`inline keyboard <apitele.types.InlineKeyboardMarkup>` attached to the message.
    :type inline_message_id: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['inline_message_id'] = res.get('inline_message_id')
        return cls(**obj)

    def __init__(
        self,
        inline_message_id: Optional[str] = None
    ):
        self.inline_message_id = inline_message_id


class SharedUser(TelegramType):
    '''
    https://core.telegram.org/bots/api#shareduser

    This object contains information about a user that was shared with
    the bot using a :obj:`~apitele.types.KeyboardButtonRequestUsers` button.

    :param user_id: Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.
    :type user_id: :obj:`int`
    :param first_name: First name of the user, if the name was requested by the bot.
    :type first_name: :obj:`str`, optional
    :param last_name: Last name of the user, if the name was requested by the bot.
    :type last_name: :obj:`str`, optional
    :param username: Username of the user, if the username was requested by the bot.
    :type username: :obj:`str`, optional
    :param photo: Available sizes of the chat photo, if the photo was requested by the bot.
    :type photo: :obj:`list` of :obj:`~apitele.types.PhotoSize`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['user_id'] = res.get('user_id')
        obj['first_name'] = res.get('first_name')
        obj['last_name'] = res.get('last_name')
        obj['username'] = res.get('username')
        obj['photo'] = [PhotoSize._dese(kwargs) for kwargs in res.get('photo')] if 'photo' in res else None
        return cls(**obj)

    def __init__(
        self,
        user_id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        photo: Optional[list[PhotoSize]] = None
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo


class ShippingAddress(TelegramType):
    '''
    https://core.telegram.org/bots/api#shippingaddress

    This object represents a shipping address.

    :param country_code: Two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ country code.
    :type country_code: :obj:`str`
    :param state: State, if applicable.
    :type state: :obj:`str`
    :param city: City.
    :type city: :obj:`str`
    :param street_line1: First line for the address.
    :type street_line1: :obj:`str`
    :param street_line2: Second line for the address.
    :type street_line2: :obj:`str`
    :param post_code: Address post code.
    :type post_code: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['country_code'] = res.get('country_code')
        obj['state'] = res.get('state')
        obj['city'] = res.get('city')
        obj['street_line1'] = res.get('street_line1')
        obj['street_line2'] = res.get('street_line2')
        obj['post_code'] = res.get('post_code')
        return cls(**obj)

    def __init__(
        self,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str
    ):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code


class ShippingOption(TelegramType):
    '''
    https://core.telegram.org/bots/api#shippingoption

    This object represents one shipping option.

    :param id: Shipping option identifier.
    :type id: :obj:`str`
    :param title: Option title.
    :type title: :obj:`str`
    :param prices: List of price portions.
    :type prices: :obj:`list` of :obj:`~apitele.types.LabeledPrice`
    '''
    def __init__(
        self,
        id: str,
        title: str,
        prices: list[LabeledPrice]
    ):
        self.id = id
        self.title = title
        self.prices = prices


class ShippingQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#shippingquery

    This object contains information about an incoming shipping query.

    :param id: Unique query identifier.
    :type id: :obj:`str`
    :param from_user: User who sent the query.
    :type from_user: :obj:`~apitele.types.User`
    :param invoice_payload: Bot specified invoice payload.
    :type invoice_payload: :obj:`str`
    :param shipping_address: User specified shipping address.
    :type shipping_address: :obj:`~apitele.types.ShippingAddress`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['from_user'] = User._dese(res.get('from_user'))
        obj['invoice_payload'] = res.get('invoice_payload')
        obj['shipping_address'] = ShippingAddress._dese(res.get('shipping_address'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        invoice_payload: str,
        shipping_address: ShippingAddress
    ):
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address


class StarAmount(TelegramType):
    '''
    https://core.telegram.org/bots/api#staramount

    Describes an amount of Telegram Stars.

    :param amount: Integer amount of Telegram Stars, rounded to 0; can be negative.
    :type amount: :obj:`int`
    :param nanostar_amount: The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if amount is non-positive.
    :type nanostar_amount: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['amount'] = res.get('amount')
        obj['nanostar_amount'] = res.get('nanostar_amount')
        return cls(**obj)

    def __init__(
        self,
        amount: int,
        nanostar_amount: Optional[int] = None
    ):
        self.amount = amount
        self.nanostar_amount = nanostar_amount


class StarTransaction(TelegramType):
    '''
    https://core.telegram.org/bots/api#startransaction

    Describes a Telegram Star transaction.

    :param id: Unique identifier of the transaction. Coincides with the identifer of the original transaction for refund transactions. Coincides with :obj:`~apitele.types.SuccessfulPayment`.telegram_payment_charge_id for successful incoming payments from users.
    :type id: :obj:`str`
    :param amount: Number of Telegram Stars transferred by the transaction.
    :type amount: :obj:`int`
    :param date: Date the transaction was created in Unix time.
    :type date: :obj:`int`
    :param nanostar_amount: The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999.
    :type nanostar_amount: :obj:`int`, optional
    :param source: Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions.
    :type source: :obj:`~apitele.types.TransactionPartner`, optional
    :param receiver: Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions.
    :type receiver: :obj:`~apitele.types.TransactionPartner`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['amount'] = res.get('amount')
        obj['date'] = res.get('date')
        obj['nanostar_amount'] = res.get('nanostar_amount')
        obj['source'] = _dese_transaction_partner(res.get('source'))
        obj['receiver'] = _dese_transaction_partner(res.get('receiver'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        amount: int,
        date: int,
        nanostar_amount: Optional[int] = None,
        source: Optional[TransactionPartner] = None,
        receiver: Optional[TransactionPartner] = None
    ):
        self.id = id
        self.amount = amount
        self.date = date
        self.nanostar_amount = nanostar_amount
        self.source = source
        self.receiver = receiver


class StarTransactions(TelegramType):
    '''
    https://core.telegram.org/bots/api#startransactions

    Contains a list of Telegram Star transactions.

    :param transactions: The list of transactions.
    :type transactions: :obj:`list` of :obj:`~apitele.types.StarTransaction`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['transactions'] = [StarTransaction._dese(kwargs) for kwargs in res.get('transactions')]
        return cls(**obj)

    def __init__(
        self,
        transactions: list[StarTransaction]
    ):
        self.transactions = transactions


class Sticker(TelegramType):
    '''
    https://core.telegram.org/bots/api#sticker

    This object represents a sticker.

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param type: Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is independent from its format, which is determined by the fields *is_animated* and *is_video*.
    :type type: :obj:`str`
    :param width: Sticker width.
    :type width: :obj:`int`
    :param height: Sticker height.
    :type height: :obj:`int`
    :param is_animated: :obj:`True`, if the sticker is `animated <https://telegram.org/blog/animated-stickers>`_.
    :type is_animated: :obj:`bool`
    :param is_video: :obj:`True`, if the sticker is a `video sticker <https://telegram.org/blog/video-stickers-better-reactions>`_.
    :type is_video: :obj:`bool`
    :param thumbnail: Sticker thumbnail in the .WEBP or .JPG format.
    :type thumbnail: :obj:`~apitele.types.PhotoSize`, optional
    :param emoji: Emoji associated with the sticker.
    :type emoji: :obj:`str`, optional
    :param set_name: Name of the sticker set to which the sticker belongs.
    :type set_name: :obj:`str`, optional
    :param premium_animation: For premium regular stickers, premium animation for the sticker.
    :type premium_animation: :obj:`~apitele.types.File`, optional
    :param mask_position: For mask stickers, the position where the mask should be placed.
    :type mask_position: :obj:`~apitele.types.MaskPosition`, optional
    :param custom_emoji_id: For custom emoji stickers, unique identifier of the custom emoji.
    :type custom_emoji_id: :obj:`str`, optional
    :param needs_repainting: :obj:`True`, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places.
    :type needs_repainting: :obj:`True`, optional
    :param file_size: File size in bytes.
    :type file_size: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['type'] = res.get('type')
        obj['width'] = res.get('width')
        obj['height'] = res.get('height')
        obj['is_animated'] = res.get('is_animated')
        obj['is_video'] = res.get('is_video')
        obj['thumbnail'] = PhotoSize._dese(res.get('thumbnail'))
        obj['emoji'] = res.get('emoji')
        obj['set_name'] = res.get('set_name')
        obj['premium_animation'] = File._dese(res.get('premium_animation'))
        obj['mask_position'] = MaskPosition._dese(res.get('mask_position'))
        obj['custom_emoji_id'] = res.get('custom_emoji_id')
        obj['needs_repainting'] = res.get('needs_repainting')
        obj['file_size'] = res.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        type: str,
        width: int,
        height: int,
        is_animated: bool,
        is_video: bool,
        thumbnail: Optional[PhotoSize] = None,
        emoji: Optional[str] = None,
        set_name: Optional[str] = None,
        premium_animation: Optional[File] = None,
        mask_position: Optional[MaskPosition] = None,
        custom_emoji_id: Optional[str] = None,
        needs_repainting: Optional[Literal[True]] = None,
        file_size: Optional[int] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size


class StickerSet(TelegramType):
    '''
    https://core.telegram.org/bots/api#stickerset

    This object represents a sticker set.

    :param name: Sticker set name.
    :type name: :obj:`str`
    :param title: Sticker set title.
    :type title: :obj:`str`
    :param sticker_type: Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”.
    :type sticker_type: :obj:`str`
    :param stickers: List of all set stickers.
    :type stickers: :obj:`list` of :obj:`~apitele.types.Sticker`
    :param thumbnail: Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format.
    :type thumbnail: :obj:`~apitele.types.PhotoSize`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        obj['title'] = res.get('title')
        obj['sticker_type'] = res.get('sticker_type')
        obj['stickers'] = [Sticker._dese(kwargs) for kwargs in res.get('stickers')]
        obj['thumbnail'] = PhotoSize._dese(res.get('thumbnail'))
        return cls(**obj)

    def __init__(
        self,
        name: str,
        title: str,
        sticker_type: str,
        stickers: list[Sticker],
        thumbnail: Optional[PhotoSize] = None
    ):
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.stickers = stickers
        self.thumbnail = thumbnail


class Story(TelegramType):
    '''
    https://core.telegram.org/bots/api#story

    This object represents a story.

    :param chat: Chat that posted the story.
    :type chat: :obj:`~apitele.types.Chat`
    :param id: Unique identifier for the story in the chat.
    :type id: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['id'] = res.get('id')
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        id: int
    ):
        self.chat = chat
        self.id = id


class StoryArea(TelegramType):
    '''
    https://core.telegram.org/bots/api#storyarea

    Describes a clickable area on a story media.

    :param position: Position of the area.
    :type position: :obj:`~apitele.types.StoryAreaPosition`
    :param type: Type of the area.
    :type type: :obj:`~apitele.types.StoryAreaType`
    '''
    def __init__(
        self,
        position: StoryAreaPosition,
        type: StoryAreaType
    ):
        self.position = position
        self.type = type


class StoryAreaPosition(TelegramType):
    '''
    https://core.telegram.org/bots/api#storyareaposition

    Describes the position of a clickable area within a story.

    :param x_percentage: The abscissa of the area's center, as a percentage of the media width.
    :type x_percentage: :obj:`float`
    :param y_percentage: The ordinate of the area's center, as a percentage of the media height.
    :type y_percentage: :obj:`float`
    :param width_percentage: The width of the area's rectangle, as a percentage of the media width.
    :type width_percentage: :obj:`float`
    :param height_percentage: The height of the area's rectangle, as a percentage of the media height.
    :type height_percentage: :obj:`float`
    :param rotation_angle: The clockwise rotation angle of the rectangle, in degrees; 0-360.
    :type rotation_angle: :obj:`float`
    :param corner_radius_percentage: The radius of the rectangle corner rounding, as a percentage of the media width.
    :type corner_radius_percentage: :obj:`float`
    '''
    def __init__(
        self,
        x_percentage: float,
        y_percentage: float,
        width_percentage: float,
        height_percentage: float,
        rotation_angle: float,
        corner_radius_percentage: float
    ):
        self.x_percentage = x_percentage
        self.y_percentage = y_percentage
        self.width_percentage = width_percentage
        self.height_percentage = height_percentage
        self.rotation_angle = rotation_angle
        self.corner_radius_percentage = corner_radius_percentage


class StoryAreaTypeLink(TelegramType):
    '''
    https://core.telegram.org/bots/api#storyareatypelink

    Describes a story area pointing to an HTTP or tg:// link. Currently, a story can have up to 3 link areas.

    :param url: HTTP or tg:// URL to be opened when the area is clicked.
    :type url: :obj:`str`
    '''
    def __init__(
        self,
        url: str
    ):
        self.type = DEFAULT_STORY_AREA_TYPE_LINK
        self.url = url


class StoryAreaTypeLocation(TelegramType):
    '''
    https://core.telegram.org/bots/api#storyareatypelocation

    Describes a story area pointing to a location. Currently, a story can have up to 10 location areas.

    :param latitude: Location latitude in degrees.
    :type latitude: :obj:`float`
    :param longitude: Location longitude in degrees.
    :type longitude: :obj:`float`
    :param address: Address of the location.
    :type address: :obj:`~apitele.types.LocationAddress`, optional
    '''
    def __init__(
        self,
        latitude: float,
        longitude: float,
        address: Optional[LocationAddress] = None
    ):
        self.type = DEFAULT_STORY_AREA_TYPE_LOCATION
        self.latitude = latitude
        self.longitude = longitude
        self.address = address


class StoryAreaTypeSuggestedReaction(TelegramType):
    '''
    https://core.telegram.org/bots/api#storyareatypesuggestedreaction

    Describes a story area pointing to a suggested reaction. Currently, a story can have up to 5 suggested reaction areas.

    :param reaction_type: Type of the reaction.
    :type reaction_type: :obj:`~apitele.types.ReactionType`
    :param is_dark: Pass :obj:`True` if the reaction area has a dark background.
    :type is_dark: :obj:`bool`, optional
    :param is_flipped: Pass :obj:`True` if reaction area corner is flipped.
    :type is_flipped: :obj:`bool`, optional
    '''
    def __init__(
        self,
        reaction_type: ReactionType,
        is_dark: Optional[bool] = None,
        is_flipped: Optional[bool] = None
    ):
        self.type = DEFAULT_STORY_AREA_TYPE_SUGGESTED_REACTION
        self.reaction_type = reaction_type
        self.is_dark = is_dark
        self.is_flipped = is_flipped


class StoryAreaTypeUniqueGift(TelegramType):
    '''
    https://core.telegram.org/bots/api#storyareatypeuniquegift

    Describes a story area pointing to a unique gift. Currently, a story can have at most 1 unique gift area.

    :param name: Unique name of the gift.
    :type name: :obj:`str`
    '''
    def __init__(
        self,
        name: str
    ):
        self.type = DEFAULT_STORY_AREA_TYPE_UNIQUE_GIFT
        self.name = name


class StoryAreaTypeWeather(TelegramType):
    '''
    https://core.telegram.org/bots/api#storyareatypeweather

    Describes a story area containing weather information. Currently, a story can have up to 3 weather areas.

    :param temperature: Temperature, in degree Celsius.
    :type temperature: :obj:`float`
    :param emoji: Emoji representing the weather.
    :type emoji: :obj:`str`
    :param background_color: A color of the area background in the ARGB format.
    :type background_color: :obj:`int`
    '''
    def __init__(
        self,
        temperature: float,
        emoji: str,
        background_color: int
    ):
        self.type = DEFAULT_STORY_AREA_TYPE_WEATHER
        self.temperature = temperature
        self.emoji = emoji
        self.background_color = background_color


class SuccessfulPayment(TelegramType):
    '''
    https://core.telegram.org/bots/api#successfulpayment

    This object contains basic information about a successful payment.

    :param currency: Three-letter ISO 4217 `currency <https://core.telegram.org/bots/payments#supported-currencies>`_ code.
    :type currency: :obj:`str`
    :param total_amount: Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of ``US$ 1.45`` pass ``amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type total_amount: :obj:`int`
    :param invoice_payload: Bot specified invoice payload.
    :type invoice_payload: :obj:`str`
    :param telegram_payment_charge_id: Telegram payment identifier.
    :type telegram_payment_charge_id: :obj:`str`
    :param provider_payment_charge_id: Provider payment identifier.
    :type provider_payment_charge_id: :obj:`str`
    :param subscription_expiration_date: Expiration date of the subscription, in Unix time; for recurring payments only.
    :type subscription_expiration_date: :obj:`int`, optional
    :param is_recurring: :obj:`True`, if the payment is a recurring payment for a subscription.
    :type is_recurring: :obj:`True`, optional
    :param is_first_recurring: :obj:`True`, if the payment is the first payment for a subscription.
    :type is_first_recurring: :obj:`True`, optional
    :param shipping_option_id: Identifier of the shipping option chosen by the user.
    :type shipping_option_id: :obj:`str`, optional
    :param order_info: Order information provided by the user.
    :type order_info: :obj:`~apitele.types.OrderInfo`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['currency'] = res.get('currency')
        obj['total_amount'] = res.get('total_amount')
        obj['invoice_payload'] = res.get('invoice_payload')
        obj['telegram_payment_charge_id'] = res.get('telegram_payment_charge_id')
        obj['provider_payment_charge_id'] = res.get('provider_payment_charge_id')
        obj['subscription_expiration_date'] = res.get('subscription_expiration_date')
        obj['is_recurring'] = res.get('is_recurring')
        obj['is_first_recurring'] = res.get('is_first_recurring')
        obj['shipping_option_id'] = res.get('shipping_option_id')
        obj['order_info'] = OrderInfo._dese(res.get('order_info'))
        return cls(**obj)

    def __init__(
        self,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        telegram_payment_charge_id: str,
        provider_payment_charge_id: str,
        subscription_expiration_date: Optional[int] = None,
        is_recurring: Optional[Literal[True]] = None,
        is_first_recurring: Optional[Literal[True]] = None,
        shipping_option_id: Optional[str] = None,
        order_info: Optional[OrderInfo] = None
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        self.subscription_expiration_date = subscription_expiration_date
        self.is_recurring = is_recurring
        self.is_first_recurring = is_first_recurring
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info


class SwitchInlineQueryChosenChat(TelegramType):
    '''
    https://core.telegram.org/bots/api#switchinlinequerychosenchat

    This object represents an inline button that switches the current user
    to inline mode in a chosen chat, with an optional default inline query.

    :param query: The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted.
    :type query: :obj:`str`, optional
    :param allow_user_chats: :obj:`True`, if private chats with users can be chosen.
    :type allow_user_chats: :obj:`bool`, optional
    :param allow_bot_chats: :obj:`True`, if private chats with bots can be chosen.
    :type allow_bot_chats: :obj:`bool`, optional
    :param allow_group_chats: :obj:`True`, if group and supergroup chats can be chosen.
    :type allow_group_chats: :obj:`bool`, optional
    :param allow_channel_chats: :obj:`True`, if channel chats can be chosen.
    :type allow_channel_chats: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['query'] = res.get('query')
        obj['allow_user_chats'] = res.get('allow_user_chats')
        obj['allow_bot_chats'] = res.get('allow_bot_chats')
        obj['allow_group_chats'] = res.get('allow_group_chats')
        obj['allow_channel_chats'] = res.get('allow_channel_chats')
        return cls(**obj)

    def __init__(
        self,
        query: Optional[str] = None,
        allow_user_chats: Optional[bool] = None,
        allow_bot_chats: Optional[bool] = None,
        allow_group_chats: Optional[bool] = None,
        allow_channel_chats: Optional[bool] = None
    ):
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats


class TextQuote(TelegramType):
    '''
    https://core.telegram.org/bots/api#textquote

    This object contains information about the quoted part
    of a message that is replied to by the given message.

    :param text: Text of the quoted part of a message that is replied to by the given message.
    :type text: :obj:`str`
    :param position: Approximate quote position in the original message in UTF-16 code units as specified by the sender.
    :type position: :obj:`int`
    :param entities: Special entities that appear in the quote. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom_emoji entities* are kept in quotes.
    :type entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
    :param is_manual: :obj:`True`, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server.
    :type is_manual: :obj:`True`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['text'] = res.get('text')
        obj['position'] = res.get('position')
        obj['entities'] = [MessageEntity._dese(kwargs) for kwargs in res.get('entities')] if 'entities' in res else None
        obj['is_manual'] = res.get('is_manual')
        return cls(**obj)

    def __init__(
        self,
        text: str,
        position: int,
        entities: Optional[list[MessageEntity]] = None,
        is_manual: Optional[Literal[True]] = None
    ):
        self.text = text
        self.position = position
        self.entities = entities
        self.is_manual = is_manual


class TransactionPartnerAffiliateProgram(TelegramType):
    '''
    https://core.telegram.org/bots/api#transactionpartneraffiliateprogram

    Describes the affiliate program that issued the affiliate commission received via this transaction.

    :param commission_per_mille: The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users.
    :type commission_per_mille: :obj:`int`
    :param sponsor_user: Information about the bot that sponsored the affiliate program.
    :type sponsor_user: :obj:`~apitele.types.User`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res:dict):
        obj = {}
        obj['commission_per_mille'] = res.get('commission_per_mille')
        obj['sponsor_user'] = User._dese(res.get('sponsor_user'))
        return cls(**obj)

    def __init__(
        self,
        commission_per_mille: int,
        sponsor_user: Optional[User] = None
    ):
        self.type = DEFAULT_TRANSACTION_PARTNER_AFFILIATE_PROGRAM
        self.commission_per_mille = commission_per_mille
        self.sponsor_user = sponsor_user


class TransactionPartnerChat(TelegramType):
    '''
    https://core.telegram.org/bots/api#transactionpartnerchat

    Describes a transaction with a chat.

    :param chat: Information about the chat.
    :type chat: :obj:`~apitele.types.Chat`
    :param gift: The gift sent to the chat by the bot.
    :type gift: :obj:`~apitele.types.Gift`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res:dict):
        obj = {}
        obj['chat'] = Chat._dese(res.get('chat'))
        obj['gift'] = Gift._dese(res.get('gift'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        gift: Optional[Gift] = None
    ):
        self.type = DEFAULT_TRANSACTION_PARTNER_CHAT
        self.chat = chat
        self.gift = gift


class TransactionPartnerFragment(TelegramType):
    '''
    https://core.telegram.org/bots/api#transactionpartnerfragment

    Describes a withdrawal transaction with Fragment.

    :param withdrawal_state: State of the transaction if the transaction is outgoing.
    :type withdrawal_state: :obj:`~apitele.types.RevenueWithdrawalState`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['withdrawal_state'] = _dese_revenue_withdrawal_state(res.get('withdrawal_state'))
        return cls(**obj)

    def __init__(
        self,
        withdrawal_state: Optional[RevenueWithdrawalState] = None
    ):
        self.type = DEFAULT_TRANSACTION_PARTNER_FRAGMENT
        self.withdrawal_state = withdrawal_state


class TransactionPartnerOther(TelegramType):
    '''
    https://core.telegram.org/bots/api#transactionpartnerother

    Describes a transaction with an unknown source or recipient.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        self.type = DEFAULT_TRANSACTION_PARTNER_OTHER


class TransactionPartnerTelegramAds(TelegramType):
    '''
    https://core.telegram.org/bots/api#transactionpartnertelegramads

    Describes a withdrawal transaction to the Telegram Ads platform.

    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        self.type = DEFAULT_TRANSACTION_PARTNER_TELEGRAM_ADS


class TransactionPartnerTelegramApi(TelegramType):
    '''
    https://core.telegram.org/bots/api#transactionpartnertelegramapi

    Describes a transaction with payment for `paid broadcasting <https://core.telegram.org/bots/api#paid-broadcasts>`_.

    :param request_count: The number of successful requests that exceeded regular limits and were therefore billed.
    :type request_count: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['request_count'] = res.get('request_count')
        return cls(**obj)

    def __init__(
        self,
        request_count: int
    ):
        self.type = DEFAULT_TRANSACTION_PARTNER_TELEGRAM_API
        self.request_count = request_count


class TransactionPartnerUser(TelegramType):
    '''
    https://core.telegram.org/bots/api#transactionpartneruser

    Describes a transaction with a user.

    :param transaction_type: Type of the transaction, currently one of “invoice_payment” for payments via invoices, “paid_media_payment” for payments for paid media, “gift_purchase” for gifts sent by the bot, “premium_purchase” for Telegram Premium subscriptions gifted by the bot, “business_account_transfer” for direct transfers from managed business accounts.
    :type transaction_type: :obj:`str`
    :param user: Information about the user.
    :type user: :obj:`~apitele.types.User`
    :param affiliate: Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions.
    :type affiliate: :obj:`~apitele.types.AffiliateInfo`, optional
    :param invoice_payload: Bot-specified invoice payload.
    :type invoice_payload: :obj:`str`, optional
    :param subscription_period: The duration of the paid subscription. Can be available only for “invoice_payment” transactions.
    :type subscription_period: :obj:`int`, optional
    :param paid_media: Information about the paid media bought by the user.
    :type paid_media: :obj:`list` of :obj:`~apitele.types.PaidMedia`, optional
    :param paid_media_payload: Bot-specified paid media payload.
    :type paid_media_payload: :obj:`str`, optional
    :param gift: The gift sent to the user by the bot; for “gift_purchase” transactions only
    :type gift: :obj:`~apitele.types.Gift`, optional
    :param premium_subscription_duration: Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only.
    :type premium_subscription_duration: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['transaction_type'] = res.get('transaction_type')
        obj['user'] = User._dese(res.get('user'))
        obj['affiliate'] = AffiliateInfo._dese(res.get('affiliate'))
        obj['invoice_payload'] = res.get('invoice_payload')
        obj['subscription_period'] = res.get('subscription_period')
        obj['paid_media'] = [_dese_paid_media(kwargs) for kwargs in res.get('paid_media')] if 'paid_media' in res else None
        obj['paid_media_payload'] = res.get('paid_media_payload')
        obj['gift'] = Gift._dese(res.get('gift'))
        obj['premium_subscription_duration'] = res.get('premium_subscription_duration')
        return cls(**obj)

    def __init__(
        self,
        transaction_type: str,
        user: User,
        affiliate: Optional[AffiliateInfo] = None,
        invoice_payload: Optional[str] = None,
        subscription_period: Optional[int] = None,
        paid_media: Optional[list[PaidMedia]] = None,
        paid_media_payload: Optional[str] = None,
        gift: Optional[Gift] = None,
        premium_subscription_duration: Optional[int] = None
    ):
        self.type = DEFAULT_TRANSACTION_PARTNER_USER
        self.transaction_type = transaction_type
        self.user = user
        self.affiliate = affiliate
        self.invoice_payload = invoice_payload
        self.subscription_period = subscription_period
        self.paid_media = paid_media
        self.paid_media_payload = paid_media_payload
        self.gift = gift
        self.premium_subscription_duration = premium_subscription_duration


class UniqueGift(TelegramType):
    '''
    https://core.telegram.org/bots/api#uniquegift

    This object describes a unique gift that was upgraded from a regular gift.

    :param base_name: Human-readable name of the regular gift from which this unique gift was upgraded.
    :type base_name: :obj:`str`
    :param name: Unique name of the gift. This name can be used in ``https://t.me/nft/...`` links and story areas.
    :type name: :obj:`str`
    :param number: Unique number of the upgraded gift among gifts upgraded from the same regular gift.
    :type number: :obj:`int`
    :param model: Model of the gift.
    :type model: :obj:`~apitele.types.UniqueGiftModel`
    :param symbol: Symbol of the gift.
    :type symbol: :obj:`~apitele.types.UniqueGiftSymbol`
    :param backdrop: Backdrop of the gift.
    :type backdrop: :obj:`~apitele.types.UniqueGiftBackdrop`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['base_name'] = res.get('base_name')
        obj['name'] = res.get('name')
        obj['number'] = res.get('number')
        obj['model'] = UniqueGiftModel._dese(res.get('model'))
        obj['symbol'] = UniqueGiftSymbol._dese(res.get('symbol'))
        obj['backdrop'] = UniqueGiftBackdrop._dese(res.get('backdrop'))
        return cls(**obj)

    def __init__(
        self,
        base_name: str,
        name: str,
        number: int,
        model: UniqueGiftModel,
        symbol: UniqueGiftSymbol,
        backdrop: UniqueGiftBackdrop
    ):
        self.base_name = base_name
        self.name = name
        self.number = number
        self.model = model
        self.symbol = symbol
        self.backdrop = backdrop


class UniqueGiftBackdrop(TelegramType):
    '''
    https://core.telegram.org/bots/api#uniquegiftbackdrop

    This object describes the backdrop of a unique gift.

    :param name: Name of the backdrop.
    :type name: :obj:`str`
    :param colors: Colors of the backdrop.
    :type colors: :obj:`~apitele.types.UniqueGiftBackdropColors`
    :param rarity_per_mille: The number of unique gifts that receive this backdrop for every 1000 gifts upgraded.
    :type rarity_per_mille: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        obj['colors'] = UniqueGiftBackdropColors._dese(res.get('colors'))
        obj['rarity_per_mille'] = res.get('rarity_per_mille')
        return cls(**obj)

    def __init__(
        self,
        name: str,
        colors: UniqueGiftBackdropColors,
        rarity_per_mille: int
    ):
        self.name = name
        self.colors = colors
        self.rarity_per_mille = rarity_per_mille


class UniqueGiftBackdropColors(TelegramType):
    '''
    https://core.telegram.org/bots/api#uniquegiftbackdropcolors

    This object describes the colors of the backdrop of a unique gift.

    :param center_color: The color in the center of the backdrop in RGB format.
    :type center_color: :obj:`int`
    :param edge_color: The color on the edges of the backdrop in RGB format.
    :type edge_color: :obj:`int`
    :param symbol_color: The color to be applied to the symbol in RGB format.
    :type symbol_color: :obj:`int`
    :param text_color: The color for the text on the backdrop in RGB format.
    :type text_color: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['center_color'] = res.get('center_color')
        obj['edge_color'] = res.get('edge_color')
        obj['symbol_color'] = res.get('symbol_color')
        obj['text_color'] = res.get('text_color')
        return cls(**obj)

    def __init__(
        self,
        center_color: int,
        edge_color: int,
        symbol_color: int,
        text_color: int
    ):
        self.center_color = center_color
        self.edge_color = edge_color
        self.symbol_color = symbol_color
        self.text_color = text_color


class UniqueGiftInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#uniquegiftinfo

    Describes a service message about a unique gift that was sent or received.

    :param gift: Information about the gift.
    :type gift: :obj:`~apitele.types.UniqueGift`
    :param origin: Origin of the gift. Currently, either “upgrade” or “transfer”.
    :type origin: :obj:`str`
    :param owned_gift_id: Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts.
    :type owned_gift_id: :obj:`str`, optional
    :param transfer_star_count: Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift.
    :type transfer_star_count: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['gift'] = UniqueGift._dese(res.get('gift'))
        obj['origin'] = res.get('origin')
        obj['owned_gift_id'] = res.get('owned_gift_id')
        obj['transfer_star_count'] = res.get('transfer_star_count')
        return cls(**obj)

    def __init__(
        self,
        gift: UniqueGift,
        origin: str,
        owned_gift_id: Optional[str] = None,
        transfer_star_count: Optional[int] = None
    ):
        self.gift = gift
        self.origin = origin
        self.owned_gift_id = owned_gift_id
        self.transfer_star_count = transfer_star_count


class UniqueGiftModel(TelegramType):
    '''
    https://core.telegram.org/bots/api#uniquegiftmodel

    This object describes the model of a unique gift.

    :param name: Name of the model.
    :type name: :obj:`str`
    :param sticker: The sticker that represents the unique gift.
    :type sticker: :obj:`~apitele.types.Sticker`
    :param rarity_per_mille: The number of unique gifts that receive this model for every 1000 gifts upgraded.
    :type rarity_per_mille: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        obj['sticker'] = Sticker._dese(res.get('sticker'))
        obj['rarity_per_mille'] = res.get('rarity_per_mille')
        return cls(**obj)

    def __init__(
        self,
        name: str,
        sticker: Sticker,
        rarity_per_mille: int
    ):
        self.name = name
        self.sticker = sticker
        self.rarity_per_mille = rarity_per_mille


class UniqueGiftSymbol(TelegramType):
    '''
    https://core.telegram.org/bots/api#uniquegiftsymbol

    This object describes the symbol shown on the pattern of a unique gift.

    :param name: Name of the symbol.
    :type name: :obj:`str`
    :param sticker: The sticker that represents the unique gift.
    :type sticker: :obj:`~apitele.types.Sticker`
    :param rarity_per_mille: The number of unique gifts that receive this model for every 1000 gifts upgraded.
    :type rarity_per_mille: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['name'] = res.get('name')
        obj['sticker'] = Sticker._dese(res.get('sticker'))
        obj['rarity_per_mille'] = res.get('rarity_per_mille')
        return cls(**obj)

    def __init__(
        self,
        name: str,
        sticker: Sticker,
        rarity_per_mille: int
    ):
        self.name = name
        self.sticker = sticker
        self.rarity_per_mille = rarity_per_mille


class Update(TelegramType):
    '''
    https://core.telegram.org/bots/api#update

    This `object <https://core.telegram.org/bots/api#available-types>`_ represents an
    incoming update. At most one of the optional parameters can be present in any given update.

    :param update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using `webhooks <https://core.telegram.org/bots/api#setwebhook>`_, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    :type update_id: :obj:`int`
    :param message: New incoming message of any kind - text, photo, sticker, etc.
    :type message: :obj:`~apitele.types.Message`, optional
    :param edited_message: New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.
    :type edited_message: :obj:`~apitele.types.Message`, optional
    :param channel_post: New incoming channel post of any kind - text, photo, sticker, etc.
    :type channel_post: :obj:`~apitele.types.Message`, optional
    :param edited_channel_post: New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.
    :type edited_channel_post: :obj:`~apitele.types.Message`, optional
    :param business_connection: The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot.
    :type business_connection: :obj:`~apitele.types.BusinessConnection`, optional
    :param business_message: New non-service message from a connected business account.
    :type business_message: :obj:`~apitele.types.Message`, optional
    :param edited_business_message: New version of a message from a connected business account.
    :type edited_business_message: :obj:`~apitele.types.Message`, optional
    :param deleted_business_messages: Messages were deleted from a connected business account.
    :type deleted_business_messages: :obj:`~apitele.types.BusinessMessagesDeleted`, optional
    :param message_reaction: A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify ``"message_reaction"`` in the list of *allowed_updates* to receive these updates. The update isn't received for reactions set by bots.
    :type message_reaction: :obj:`~apitele.types.MessageReactionUpdated`, optional
    :param message_reaction_count: Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify ``"message_reaction_count"`` in the list of *allowed_updates* to receive these updates. The updates are grouped and can be sent with delay up to a few minutes.
    :type message_reaction_count: :obj:`~apitele.types.MessageReactionCountUpdated`, optional
    :param inline_query: New incoming `inline <https://core.telegram.org/bots/api#inline-mode>`_ query.
    :type inline_query: :obj:`~apitele.types.InlineQuery`, optional
    :param chosen_inline_result: The result of an `inline <https://core.telegram.org/bots/api#inline-mode>`_ query that was chosen by a user and sent to their chat partner. Please see our documentation on the `feedback collecting <https://core.telegram.org/bots/inline#collecting-feedback>`_ for details on how to enable these updates for your bot.
    :type chosen_inline_result: :obj:`~apitele.types.ChosenInlineResult`, optional
    :param callback_query: New incoming callback query.
    :type callback_query: :obj:`~apitele.types.CallbackQuery`, optional
    :param shipping_query: New incoming shipping query. Only for invoices with flexible price.
    :type shipping_query: :obj:`~apitele.types.ShippingQuery`, optional
    :param pre_checkout_query: New incoming pre-checkout query. Contains full information about checkout.
    :type pre_checkout_query: :obj:`~apitele.types.PreCheckoutQuery`, optional
    :param purchased_paid_media: A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat.
    :type purchased_paid_media: :obj:`~apitele.types.PaidMediaPurchased`, optional
    :param poll: New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot.
    :type poll: :obj:`~apitele.types.Poll`, optional
    :param poll_answer: A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    :type poll_answer: :obj:`~apitele.types.PollAnswer`, optional
    :param my_chat_member: The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
    :type my_chat_member: :obj:`~apitele.types.ChatMemberUpdated`, optional
    :param chat_member: A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify ``"chat_member"`` in the list of *allowed_updates* to receive these updates.
    :type chat_member: :obj:`~apitele.types.ChatMemberUpdated`, optional
    :param chat_join_request: A request to join the chat has been sent. The bot must have the *can_invite_users* administrator right in the chat to receive these updates.
    :type chat_join_request: :obj:`~apitele.types.ChatJoinRequest`, optional
    :param chat_boost: A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates.
    :type chat_boost: :obj:`~apitele.types.ChatBoostUpdated`, optional
    :param removed_chat_boost: A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates.
    :type removed_chat_boost: :obj:`~apitele.types.ChatBoostRemoved`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['update_id'] = res.get('update_id')
        obj['message'] = Message._dese(res.get('message'))
        obj['edited_message'] = Message._dese(res.get('edited_message'))
        obj['channel_post'] = Message._dese(res.get('channel_post'))
        obj['edited_channel_post'] = Message._dese(res.get('edited_channel_post'))
        obj['business_connection'] = BusinessConnection._dese(res.get('business_connection'))
        obj['business_message'] = Message._dese(res.get('business_message'))
        obj['edited_business_message'] = Message._dese(res.get('edited_business_message'))
        obj['deleted_business_messages'] = BusinessMessagesDeleted._dese(res.get('deleted_business_messages'))
        obj['message_reaction'] = MessageReactionUpdated._dese(res.get('message_reaction'))
        obj['message_reaction_count'] = MessageReactionCountUpdated._dese(res.get('message_reaction_count'))
        obj['inline_query'] = InlineQuery._dese(res.get('inline_query'))
        obj['chosen_inline_result'] = ChosenInlineResult._dese(res.get('chosen_inline_result'))
        obj['callback_query'] = CallbackQuery._dese(res.get('callback_query'))
        obj['shipping_query'] = ShippingQuery._dese(res.get('shipping_query'))
        obj['pre_checkout_query'] = PreCheckoutQuery._dese(res.get('pre_checkout_query'))
        obj['purchased_paid_media'] = PaidMediaPurchased._dese(res.get('purchased_paid_media'))
        obj['poll'] = Poll._dese(res.get('poll'))
        obj['poll_answer'] = PollAnswer._dese(res.get('poll_answer'))
        obj['my_chat_member'] = ChatMemberUpdated._dese(res.get('my_chat_member'))
        obj['chat_member'] = ChatMemberUpdated._dese(res.get('chat_member'))
        obj['chat_join_request'] = ChatJoinRequest._dese(res.get('chat_join_request'))
        obj['chat_boost'] = ChatBoostUpdated._dese(res.get('chat_boost'))
        obj['removed_chat_boost'] = ChatBoostRemoved._dese(res.get('removed_chat_boost'))
        return cls(**obj)

    def __init__(
        self,
        update_id: int,
        message: Optional[Message] = None,
        edited_message: Optional[Message] = None,
        channel_post: Optional[Message] = None,
        edited_channel_post: Optional[Message] = None,
        business_connection: Optional[BusinessConnection] = None,
        business_message: Optional[Message] = None,
        edited_business_message: Optional[Message] = None,
        deleted_business_messages: Optional[BusinessMessagesDeleted] = None,
        message_reaction: Optional[MessageReactionUpdated] = None,
        message_reaction_count: Optional[MessageReactionCountUpdated] = None,
        inline_query: Optional[InlineQuery] = None,
        chosen_inline_result: Optional[ChosenInlineResult] = None,
        callback_query: Optional[CallbackQuery] = None,
        shipping_query: Optional[ShippingQuery] = None,
        pre_checkout_query: Optional[PreCheckoutQuery] = None,
        purchased_paid_media: Optional[PaidMediaPurchased] = None,
        poll: Optional[Poll] = None,
        poll_answer: Optional[PollAnswer] = None,
        my_chat_member: Optional[ChatMemberUpdated] = None,
        chat_member: Optional[ChatMemberUpdated] = None,
        chat_join_request: Optional[ChatJoinRequest] = None,
        chat_boost: Optional[ChatBoostUpdated] = None,
        removed_chat_boost: Optional[ChatBoostRemoved] = None
    ):
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.business_connection = business_connection
        self.business_message = business_message
        self.edited_business_message = edited_business_message
        self.deleted_business_messages = deleted_business_messages
        self.message_reaction = message_reaction
        self.message_reaction_count = message_reaction_count
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.purchased_paid_media = purchased_paid_media
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request
        self.chat_boost = chat_boost
        self.removed_chat_boost = removed_chat_boost


class User(TelegramType):
    '''
    https://core.telegram.org/bots/api#user

    This object represents a Telegram user or bot.

    :param id: Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type id: :obj:`int`
    :param is_bot: :obj:`True`, if this user is a bot.
    :type is_bot: :obj:`bool`
    :param first_name: User's or bot's first name.
    :type first_name: :obj:`str`
    :param last_name: User's or bot's last name.
    :type last_name: :obj:`str`, optional
    :param username: User's or bot's username.
    :type username: :obj:`str`, optional
    :param language_code: `IETF language tag <https://en.wikipedia.org/wiki/IETF_language_tag>`_ of the user's language.
    :type language_code: :obj:`str`, optional
    :param is_premium: :obj:`True`, if this user is a Telegram Premium user.
    :type is_premium: :obj:`True`, optional
    :param added_to_attachment_menu: :obj:`True`, if this user added the bot to the attachment menu.
    :type added_to_attachment_menu: :obj:`True`, optional
    :param can_join_groups: :obj:`True`, if the bot can be invited to groups. Returned only in :meth:`~apitele.Client.get_me`.
    :type can_join_groups: :obj:`bool`, optional
    :param can_read_all_group_messages: :obj:`True`, if privacy mode is disabled for the bot. Returned only in :meth:`~apitele.Client.get_me`.
    :type can_read_all_group_messages: :obj:`bool`, optional
    :param supports_inline_queries: :obj:`True`, if the bot supports inline queries. Returned only in :meth:`~apitele.Client.get_me`.
    :type supports_inline_queries: :obj:`bool`, optional
    :param can_connect_to_business: :obj:`True`, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in :meth:`~apitele.Client.get_me`.
    :type can_connect_to_business: :obj:`bool`, optional
    :param has_main_web_app: :obj:`True`, if the bot has a main Web App. Returned only in :meth:`~apitele.Client.get_me`.
    :type has_main_web_app: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['id'] = res.get('id')
        obj['is_bot'] = res.get('is_bot')
        obj['first_name'] = res.get('first_name')
        obj['last_name'] = res.get('last_name')
        obj['username'] = res.get('username')
        obj['language_code'] = res.get('language_code')
        obj['is_premium'] = res.get('is_premium')
        obj['added_to_attachment_menu'] = res.get('added_to_attachment_menu')
        obj['can_join_groups'] = res.get('can_join_groups')
        obj['can_read_all_group_messages'] = res.get('can_read_all_group_messages')
        obj['supports_inline_queries'] = res.get('supports_inline_queries')
        obj['can_connect_to_business'] = res.get('can_connect_to_business')
        obj['has_main_web_app'] = res.get('has_main_web_app')
        return cls(**obj)

    def __init__(
        self,
        id: int,
        is_bot: bool,
        first_name: str,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        language_code: Optional[str] = None,
        is_premium: Optional[Literal[True]] = None,
        added_to_attachment_menu: Optional[Literal[True]] = None,
        can_join_groups: Optional[bool] = None,
        can_read_all_group_messages: Optional[bool] = None,
        supports_inline_queries: Optional[bool] = None,
        can_connect_to_business: Optional[bool] = None,
        has_main_web_app: Optional[bool] = None
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.can_connect_to_business = can_connect_to_business
        self.has_main_web_app = has_main_web_app


class UserChatBoosts(TelegramType):
    '''
    https://core.telegram.org/bots/api#userchatboosts

    This object represents a list of boosts added to a chat by a user.

    :param boosts: The list of boosts added to the chat by the user.
    :type boosts: :obj:`list` of :obj:`~apitele.types.ChatBoost`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['boosts'] = [ChatBoost._dese(kwargs) for kwargs in res.get('boosts')]
        return cls(**obj)

    def __init__(
        self,
        boosts: list[ChatBoost]
    ):
        self.boosts = boosts


class UserProfilePhotos(TelegramType):
    '''
    https://core.telegram.org/bots/api#userprofilephotos

    This object represent a user's profile pictures.

    :param total_count: Total number of profile pictures the target user has.
    :type total_count: :obj:`int`
    :param photos: Requested profile pictures (in up to 4 sizes each).
    :type photos: :obj:`list` of :obj:`list` of :obj:`~apitele.types.PhotoSize`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['total_count'] = res.get('total_count')
        obj['photos'] = [[PhotoSize._dese(kwargs) for kwargs in lst] for lst in res.get('photos')]
        return cls(**obj)

    def __init__(
        self,
        total_count: int,
        photos: list[list[PhotoSize]]
    ):
        self.total_count = total_count
        self.photos = photos


class UsersShared(TelegramType):
    '''
    https://core.telegram.org/bots/api#usersshared

    This object contains information about the users whose identifiers
    were shared with the bot using a :obj:`~apitele.types.KeyboardButtonRequestUsers` button.

    :param request_id: Identifier of the request.
    :type request_id: :obj:`int`
    :param users: Information about users shared with the bot.
    :type users: :obj:`list` of :obj:`~apitele.types.SharedUser`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['request_id'] = res.get('request_id')
        obj['users'] = [SharedUser._dese(kwargs) for kwargs in res.get('users')]
        return cls(**obj)

    def __init__(
        self,
        request_id: int,
        users: list[SharedUser]
    ):
        self.request_id = request_id
        self.users = users


class Venue(TelegramType):
    '''
    https://core.telegram.org/bots/api#venue

    This object represents a venue.

    :param location: Venue location. Can't be a live location.
    :type location: :obj:`~apitele.types.Location`
    :param title: Name of the venue.
    :type title: :obj:`str`
    :param address: Address of the venue.
    :type address: :obj:`str`
    :param foursquare_id: Foursquare identifier of the venue.
    :type foursquare_id: :obj:`str`, optional
    :param foursquare_type: Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :type foursquare_type: :obj:`str`, optional
    :param google_place_id: Google Places identifier of the venue.
    :type google_place_id: :obj:`str`, optional
    :param google_place_type: Google Places type of the venue. (See `supported types <https://developers.google.com/places/web-service/supported_types>`_.)
    :type google_place_type: :obj:`str`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['location'] = Location._dese(res.get('location'))
        obj['title'] = res.get('title')
        obj['address'] = res.get('address')
        obj['foursquare_id'] = res.get('foursquare_id')
        obj['foursquare_type'] = res.get('foursquare_type')
        obj['google_place_id'] = res.get('google_place_id')
        obj['google_place_type'] = res.get('google_place_type')
        return cls(**obj)

    def __init__(
        self,
        location: Location,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None
    ):
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class Video(TelegramType):
    '''
    https://core.telegram.org/bots/api#video

    This object represents a video file.

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param width: Video width as defined by sender.
    :type width: :obj:`int`
    :param height: Video height as defined by sender.
    :type height: :obj:`int`
    :param duration: Duration of the video in seconds as defined by sender.
    :type duration: :obj:`int`
    :param thumbnail: Video thumbnail.
    :type thumbnail: :obj:`~apitele.types.PhotoSize`, optional
    :param cover: Available sizes of the cover of the video in the message.
    :type cover: :obj:`list` of :obj:`~apitele.types.PhotoSize`, optional
    :param start_timestamp: Timestamp in seconds from which the video will play in the message.
    :type start_timestamp: :obj:`int`, optional
    :param file_name: Original filename as defined by sender.
    :type file_name: :obj:`str`, optional
    :param mime_type: MIME type of the file as defined by sender.
    :type mime_type: :obj:`str`, optional
    :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['width'] = res.get('width')
        obj['height'] = res.get('height')
        obj['duration'] = res.get('duration')
        obj['thumbnail'] = PhotoSize._dese(res.get('thumbnail'))
        obj['cover'] = [PhotoSize._dese(kwargs) for kwargs in res.get('cover')] if 'cover' in res else None
        obj['start_timestamp'] = res.get('start_timestamp')
        obj['file_name'] = res.get('file_name')
        obj['mime_type'] = res.get('mime_type')
        obj['file_size'] = res.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        cover: Optional[list[PhotoSize]] = None,
        start_timestamp: Optional[int] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.cover = cover
        self.start_timestamp = start_timestamp
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class VideoChatEnded(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatended

    This object represents a service message about a video chat ended in the chat.

    :param duration: Video chat duration in seconds.
    :type duration: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['duration'] = res.get('duration')
        return cls(**obj)

    def __init__(
        self,
        duration: int
    ):
        self.duration = duration


class VideoChatParticipantsInvited(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatparticipantsinvited

    This object represents a service message about new members invited to a video chat.

    :param users: New members that were invited to the video chat.
    :type users: :obj:`list` of :obj:`~apitele.types.User`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['users'] = [User._dese(kwargs) for kwargs in res.get('users')]
        return cls(**obj)

    def __init__(
        self,
        users: list[User]
    ):
        self.users = users


class VideoChatScheduled(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatscheduled

    This object represents a service message about a video chat scheduled in the chat.

    :param start_date: Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator.
    :type start_date: :obj:`int`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['start_date'] = res.get('start_date')
        return cls(**obj)

    def __init__(
        self,
        start_date: int
    ):
        self.start_date = start_date


class VideoChatStarted(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatstarted

    This object represents a service message about a video
    chat started in the chat. Currently holds no information.
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        return cls(**obj)

    def __init__(self):
        ...


class VideoNote(TelegramType):
    '''
    https://core.telegram.org/bots/api#videonote

    This object represents a `video message <https://telegram.org/blog/video-messages-and-telescope>`_
    (available in Telegram apps as of `v.4.0 <https://telegram.org/blog/video-messages-and-telescope>`_).

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param length: Video width and height (diameter of the video message) as defined by sender.
    :type length: :obj:`int`
    :param duration: Duration of the video in seconds as defined by sender.
    :type duration: :obj:`int`
    :param thumbnail: Video thumbnail.
    :type thumbnail: :obj:`~apitele.types.PhotoSize`, optional
    :param file_size: File size in bytes.
    :type file_size: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['length'] = res.get('length')
        obj['duration'] = res.get('duration')
        obj['thumbnail'] = PhotoSize._dese(res.get('thumbnail'))
        obj['file_size'] = res.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        file_size: Optional[int] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size


class Voice(TelegramType):
    '''
    https://core.telegram.org/bots/api#voice

    This object represents a voice note.

    :param file_id: Identifier for this file, which can be used to download or reuse the file.
    :type file_id: :obj:`str`
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type file_unique_id: :obj:`str`
    :param duration: Duration of the audio in seconds as defined by sender.
    :type duration: :obj:`int`
    :param mime_type: MIME type of the file as defined by sender.
    :type mime_type: :obj:`str`, optional
    :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    :type file_size: :obj:`int`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['file_id'] = res.get('file_id')
        obj['file_unique_id'] = res.get('file_unique_id')
        obj['duration'] = res.get('duration')
        obj['mime_type'] = res.get('mime_type')
        obj['file_size'] = res.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


class WebAppData(TelegramType):
    '''
    https://core.telegram.org/bots/api#webappdata

    Describes data sent from a `Web App <https://core.telegram.org/bots/webapps>`_ to the bot.

    :param data: The data. Be aware that a bad client can send arbitrary data in this field.
    :type data: :obj:`str`
    :param button_text: Text of the *web_app* keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.
    :type button_text: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['data'] = res.get('data')
        obj['button_text'] = res.get('button_text')
        return cls(**obj)

    def __init__(
        self,
        data: str,
        button_text: str
    ):
        self.data = data
        self.button_text = button_text


class WebAppInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#webappinfo

    Describes a `Web App <https://core.telegram.org/bots/webapps>`_.

    :param url: An HTTPS URL of a Web App to be opened with additional data as specified in `Initializing Web Apps <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_.
    :type url: :obj:`str`
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['url'] = res.get('url')
        return cls(**obj)

    def __init__(
        self,
        url: str
    ):
        self.url = url


class WriteAccessAllowed(TelegramType):
    '''
    https://core.telegram.org/bots/api#writeaccessallowed

    This object represents a service message about a user allowing a bot to write
    messages after adding it to the attachment menu, launching a Web App from a link,
    or accepting an explicit request from a Web App sent by the method `requestWriteAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_.

    :param from_request: :obj:`True`, if the access was granted after the user accepted an explicit request from a Web App sent by the method `requestWriteAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_.
    :type from_request: :obj:`bool`, optional
    :param web_app_name: Name of the Web App, if the access was granted when the Web App was launched from a link.
    :type web_app_name: :obj:`str`, optional
    :param from_attachment_menu: :obj:`True`, if the access was granted when the bot was added to the attachment or side menu.
    :type from_attachment_menu: :obj:`bool`, optional
    '''
    @classmethod
    @_parse_result
    def _dese(cls, res: dict):
        obj = {}
        obj['from_request'] = res.get('from_request')
        obj['web_app_name'] = res.get('web_app_name')
        obj['from_attachment_menu'] = res.get('from_attachment_menu')
        return cls(**obj)

    def __init__(
        self,
        from_request: Optional[bool] = None,
        web_app_name: Optional[str] = None,
        from_attachment_menu: Optional[bool] = None
    ):
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
REPLY_MARKUP_TYPES = Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
'''
One of the following reply markups:

- :obj:`~apitele.types.InlineKeyboardMarkup`
- :obj:`~apitele.types.ReplyKeyboardMarkup`
- :obj:`~apitele.types.ReplyKeyboardRemove`
- :obj:`~apitele.types.ForceReply`
'''


BackgroundFill = Union[
    BackgroundFillSolid,
    BackgroundFillGradient,
    BackgroundFillFreeformGradient
]
'''
https://core.telegram.org/bots/api#backgroundfill

This object describes the way a background is filled based on the selected colors. Currently, it can be one of:

- :obj:`~apitele.types.BackgroundFillSolid`
- :obj:`~apitele.types.BackgroundFillGradient`
- :obj:`~apitele.types.BackgroundFillFreeformGradient`
'''

def _dese_background_fill(res: Optional[dict], /) -> Optional[BackgroundFill]:
    '''
    Function to deserialize BackgroundFill.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_BACKGROUND_FILL_SOLID:
        return BackgroundFillSolid._dese(obj, check_dict=False)

    elif type == DEFAULT_BACKGROUND_FILL_GRADIENT:
        return BackgroundFillGradient._dese(obj, check_dict=False)

    elif type == DEFAULT_BACKGROUND_FILL_FREEFORM_GRADIENT:
        return BackgroundFillFreeformGradient._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization of the'
            f' type BackgroundFill. Invalid type: {type!r}.'
        )
 

BackgroundType = Union[
    BackgroundTypeFill,
    BackgroundTypeWallpaper,
    BackgroundTypePattern,
    BackgroundTypeChatTheme
]
'''
https://core.telegram.org/bots/api#backgroundtype

This object describes the type of a background. Currently, it can be one of:

- :obj:`~apitele.types.BackgroundTypeFill`
- :obj:`~apitele.types.BackgroundTypeWallpaper`
- :obj:`~apitele.types.BackgroundTypePattern`
- :obj:`~apitele.types.BackgroundTypeChatTheme`
'''

def _dese_background_type(res: Optional[dict], /) -> Optional[BackgroundType]:
    '''
    Function to deserialize BackgroundType.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_BACKGROUND_TYPE_FILL:
        return BackgroundTypeFill._dese(obj, check_dict=False)

    elif type == DEFAULT_BACKGROUND_TYPE_WALLPAPER:
        return BackgroundTypeWallpaper._dese(obj, check_dict=False)

    elif type == DEFAULT_BACKGROUND_TYPE_PATTERN:
        return BackgroundTypePattern._dese(obj, check_dict=False)

    elif type == DEFAULT_BACKGROUND_TYPE_CHAT_THEME:
        return BackgroundTypeChatTheme._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization of the'
            f' type BackgroundType. Invalid type: {type!r}.'
        )


BotCommandScope = Union[
    BotCommandScopeDefault,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember
]
'''
https://core.telegram.org/bots/api#botcommandscope

This object represents the scope to which bot commands are applied.
Currently, the following 7 scopes are supported:

- :obj:`~apitele.types.BotCommandScopeDefault`
- :obj:`~apitele.types.BotCommandScopeAllPrivateChats`
- :obj:`~apitele.types.BotCommandScopeAllGroupChats`
- :obj:`~apitele.types.BotCommandScopeAllChatAdministrators`
- :obj:`~apitele.types.BotCommandScopeChat`
- :obj:`~apitele.types.BotCommandScopeChatAdministrators`
- :obj:`~apitele.types.BotCommandScopeChatMember`

**Determining list of commands**

The following algorithm is used to determine the list of commands for a particular user viewing the bot menu. The first list of commands which is set is returned:

**Commands in the chat with the bot**

- :obj:`~apitele.types.BotCommandScopeChat` + language_code
- :obj:`~apitele.types.BotCommandScopeChat`
- :obj:`~apitele.types.BotCommandScopeAllPrivateChats` + language_code
- :obj:`~apitele.types.BotCommandScopeAllPrivateChats`
- :obj:`~apitele.types.BotCommandScopeDefault` + language_code
- :obj:`~apitele.types.BotCommandScopeDefault`

**Commands in group and supergroup chats**

- :obj:`~apitele.types.BotCommandScopeChatMember` + language_code
- :obj:`~apitele.types.BotCommandScopeChatMember`
- :obj:`~apitele.types.BotCommandScopeChatAdministrators` + language_code (administrators only)
- :obj:`~apitele.types.BotCommandScopeChatAdministrators` (administrators only)
- :obj:`~apitele.types.BotCommandScopeChat` + language_code
- :obj:`~apitele.types.BotCommandScopeChat`
- :obj:`~apitele.types.BotCommandScopeAllChatAdministrators` + language_code (administrators only)
- :obj:`~apitele.types.BotCommandScopeAllChatAdministrators` (administrators only)
- :obj:`~apitele.types.BotCommandScopeAllGroupChats` + language_code
- :obj:`~apitele.types.BotCommandScopeAllGroupChats`
- :obj:`~apitele.types.BotCommandScopeDefault` + language_code
- :obj:`~apitele.types.BotCommandScopeDefault`

'''


ChatBoostSource = Union[ChatBoostSourcePremium, ChatBoostSourceGiftCode, ChatBoostSourceGiveaway]
'''
https://core.telegram.org/bots/api#chatboostsource

This object describes the source of a chat boost. It can be one of:

- :obj:`~apitele.types.ChatBoostSourcePremium`
- :obj:`~apitele.types.ChatBoostSourceGiftCode`
- :obj:`~apitele.types.ChatBoostSourceGiveaway`
'''

def _dese_chat_boost_source(res: Optional[dict], /) -> Optional[ChatBoostSource]:
    '''
    Function to deserialize ChatBoostSource.
    '''
    if res is None: return None
    obj = _check_dict(res)

    source = obj.pop('source')

    if source == DEFAULT_CHAT_BOOST_SOURCE_PREMIUM:
        return ChatBoostSourcePremium._dese(obj, check_dict=False)

    elif source == DEFAULT_CHAT_BOOST_SOURCE_GIFT_CODE:
        return ChatBoostSourceGiftCode._dese(obj, check_dict=False)

    elif source == DEFAULT_CHAT_BOOST_SOURCE_GIVEAWAY:
        return ChatBoostSourceGiveaway._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization of the'
            f' type ChatBoostSource. Invalid source: {source!r}.'
        )


ChatMember = Union[
    ChatMemberOwner,
    ChatMemberAdministrator,
    ChatMemberMember,
    ChatMemberRestricted,
    ChatMemberLeft,
    ChatMemberBanned
]
'''
https://core.telegram.org/bots/api#chatmember

This object contains information about one member of a chat.
Currently, the following 6 types of chat members are supported:

- :obj:`~apitele.types.ChatMemberOwner`
- :obj:`~apitele.types.ChatMemberAdministrator`
- :obj:`~apitele.types.ChatMemberMember`
- :obj:`~apitele.types.ChatMemberRestricted`
- :obj:`~apitele.types.ChatMemberLeft`
- :obj:`~apitele.types.ChatMemberBanned`
'''

def _dese_chat_member(res: Optional[dict], /) -> Optional[ChatMember]:
    '''
    Function to deserialize ChatMember.
    '''
    if res is None: return None
    obj = _check_dict(res)        

    status = obj.pop('status')

    if status == DEFAULT_CHAT_MEMBER_OWNER:
        return ChatMemberOwner._dese(obj, check_dict=False)

    elif status == DEFAULT_CHAT_MEMBER_ADMINISTRATOR:
        return ChatMemberAdministrator._dese(obj, check_dict=False)

    elif status == DEFAULT_CHAT_MEMBER_MEMBER:
        return ChatMemberMember._dese(obj, check_dict=False)

    elif status == DEFAULT_CHAT_MEMBER_RESTRICTED:
        return ChatMemberRestricted._dese(obj, check_dict=False)

    elif status == DEFAULT_CHAT_MEMBER_LEFT:
        return ChatMemberLeft._dese(obj, check_dict=False)

    elif status == DEFAULT_CHAT_MEMBER_BANNED:
        return ChatMemberBanned._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type ChatMember. Invalid status: {status!r}.'
        )


InlineQueryResult = Union[
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultContact,
    InlineQueryResultGame,
    InlineQueryResultDocument,
    InlineQueryResultGif,
    InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoice,
]
'''
https://core.telegram.org/bots/api#inlinequeryresult

This object represents one result of an inline query.
Telegram clients currently support results of the following 20 types:

- :obj:`~apitele.types.InlineQueryResultCachedAudio`
- :obj:`~apitele.types.InlineQueryResultCachedDocument`
- :obj:`~apitele.types.InlineQueryResultCachedGif`
- :obj:`~apitele.types.InlineQueryResultCachedMpeg4Gif`
- :obj:`~apitele.types.InlineQueryResultCachedPhoto`
- :obj:`~apitele.types.InlineQueryResultCachedSticker`
- :obj:`~apitele.types.InlineQueryResultCachedVideo`
- :obj:`~apitele.types.InlineQueryResultCachedVoice`
- :obj:`~apitele.types.InlineQueryResultArticle`
- :obj:`~apitele.types.InlineQueryResultAudio`
- :obj:`~apitele.types.InlineQueryResultContact`
- :obj:`~apitele.types.InlineQueryResultGame`
- :obj:`~apitele.types.InlineQueryResultDocument`
- :obj:`~apitele.types.InlineQueryResultGif`
- :obj:`~apitele.types.InlineQueryResultLocation`
- :obj:`~apitele.types.InlineQueryResultMpeg4Gif`
- :obj:`~apitele.types.InlineQueryResultPhoto`
- :obj:`~apitele.types.InlineQueryResultVenue`
- :obj:`~apitele.types.InlineQueryResultVideo`
- :obj:`~apitele.types.InlineQueryResultVoice`

**Note**: All URLs passed in inline query results will be
available to end users and therefore must be assumed to be **public**.
'''


InputMedia = Union[
    InputMediaAnimation,
    InputMediaDocument,
    InputMediaAudio,
    InputMediaPhoto,
    InputMediaVideo
]
'''
https://core.telegram.org/bots/api#inputmedia

This object represents the content of a media message to be sent. It should be one of:

- :obj:`~apitele.types.InputMediaAnimation`
- :obj:`~apitele.types.InputMediaDocument`
- :obj:`~apitele.types.InputMediaAudio`
- :obj:`~apitele.types.InputMediaPhoto`
- :obj:`~apitele.types.InputMediaVideo`
'''


InputMessageContent = Union[
    InputTextMessageContent,
    InputLocationMessageContent,
    InputVenueMessageContent,
    InputContactMessageContent,
    InputInvoiceMessageContent
]
'''
https://core.telegram.org/bots/api#inputmessagecontent

This object represents the content of a message to be sent as a result of an inline query.
Telegram clients currently support the following 5 types:

- :obj:`~apitele.types.InputTextMessageContent`
- :obj:`~apitele.types.InputLocationMessageContent`
- :obj:`~apitele.types.InputVenueMessageContent`
- :obj:`~apitele.types.InputContactMessageContent`
- :obj:`~apitele.types.InputInvoiceMessageContent`
'''


InputPaidMedia = Union[InputPaidMediaPhoto, InputPaidMediaVideo]
'''
https://core.telegram.org/bots/api#inputpaidmedia

This object describes the paid media to be sent. Currently, it can be one of:

- :obj:`~apitele.types.InputPaidMediaPhoto`
- :obj:`~apitele.types.InputPaidMediaVideo`
'''

InputProfilePhoto = Union[InputProfilePhotoStatic, InputProfilePhotoAnimated]
'''
https://core.telegram.org/bots/api#inputprofilephoto

This object describes a profile photo to set. Currently, it can be one of:

- :obj:`~apitele.types.InputProfilePhotoStatic`
- :obj:`~apitele.types.InputProfilePhotoAnimated`
'''

InputStoryContent = Union[InputStoryContentPhoto, InputStoryContentVideo]
'''
https://core.telegram.org/bots/api#inputstorycontent

This object describes the content of a story to post. Currently, it can be one of:

- :obj:`~apitele.types.InputStoryContentPhoto`
- :obj:`~apitele.types.InputStoryContentVideo`
'''

MaybeInaccessibleMessage = Union[Message, InaccessibleMessage]
'''
https://core.telegram.org/bots/api#maybeinaccessiblemessage

This object describes a message that can be inaccessible to the bot. It can be one of:

- :obj:`~apitele.types.Message`
- :obj:`~apitele.types.InaccessibleMessage`
'''

def _dese_maybe_inaccessible_message(res: Optional[dict], /) -> Optional[MaybeInaccessibleMessage]:
    '''
    Function to deserialize MaybeInaccessibleMessage.
    '''
    if res is None: return None
    obj = _check_dict(res)

    if obj['date'] == 0:
        return InaccessibleMessage._dese(obj, check_dict=False)
    else:
        return Message._dese(obj, check_dict=False)


MenuButton = Union[MenuButtonCommands, MenuButtonWebApp, MenuButtonDefault]
'''
https://core.telegram.org/bots/api#menubutton

This object describes the bot's menu button in a private chat. It should be one of

- :obj:`~apitele.types.MenuButtonCommands`
- :obj:`~apitele.types.MenuButtonWebApp`
- :obj:`~apitele.types.MenuButtonDefault`

If a menu button other than :obj:`~apitele.types.MenuButtonDefault` is set for a private
chat, then it is applied in the chat. Otherwise the default menu button is applied. By
default, the menu button opens the list of bot commands.
'''

def _dese_menu_button(res: Optional[dict], /) -> Optional[MenuButton]: # used in apitele.__init__
    '''
    Function to deserialize MenuButton.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_MENU_BUTTON_COMMANDS:
        return MenuButtonCommands._dese(obj, check_dict=False)

    elif type == DEFAULT_MENU_BUTTON_WEB_APP:
        return MenuButtonWebApp._dese(obj, check_dict=False)

    elif type == DEFAULT_MENU_BUTTON_DEFAULT:
        return MenuButtonDefault._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type MenuButton. Invalid type: {type!r}.'
        )


MessageOrigin = Union[
    MessageOriginUser,
    MessageOriginHiddenUser,
    MessageOriginChat,
    MessageOriginChannel
]
'''
https://core.telegram.org/bots/api#messageorigin

This object describes the origin of a message. It can be one of:

- :obj:`~apitele.types.MessageOriginUser`
- :obj:`~apitele.types.MessageOriginHiddenUser`
- :obj:`~apitele.types.MessageOriginChat`
- :obj:`~apitele.types.MessageOriginChannel`
'''

def _dese_message_origin(res: Optional[dict], /) -> Optional[MessageOrigin]:
    '''
    Function to deserialize MessageOrigin.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_MESSAGE_ORIGIN_USER:
        return MessageOriginUser._dese(obj, check_dict=False)

    elif type == DEFAULT_MESSAGE_ORIGIN_HIDDEN_USER:
        return MessageOriginHiddenUser._dese(obj, check_dict=False)

    elif type == DEFAULT_MESSAGE_ORIGIN_CHAT:
        return MessageOriginChat._dese(obj, check_dict=False)

    elif type == DEFAULT_MESSAGE_ORIGIN_CHANNEL:
        return MessageOriginChannel._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type MessageOrigin. Invalid type: {type!r}.'
        )


OwnedGift = Union[OwnedGiftRegular, OwnedGiftUnique]
'''
https://core.telegram.org/bots/api#ownedgift

This object describes a gift received and owned by a user or a chat. Currently, it can be one of:

- :obj:`~apitele.types.OwnedGiftRegular`
- :obj:`~apitele.types.OwnedGiftUnique`
'''

def _dese_owned_gift(res: Optional[dict], /) -> Optional[OwnedGift]:
    '''
    Function to deserialize OwnedGift.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_OWNED_GIFT_REGULAR:
        return OwnedGiftRegular._dese(obj, check_dict=False)

    elif type == DEFAULT_OWNED_GIFT_UNIQUE:
        return OwnedGiftUnique._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type OwnedGift. Invalid type: {type!r}.'
        )


PaidMedia = Union[PaidMediaPreview, PaidMediaPhoto, PaidMediaVideo]
'''
https://core.telegram.org/bots/api#paidmedia

This object describes paid media. Currently, it can be one of:

- :obj:`~apitele.types.PaidMediaPreview`
- :obj:`~apitele.types.PaidMediaPhoto`
- :obj:`~apitele.types.PaidMediaVideo`
'''

def _dese_paid_media(res: Optional[dict], /) -> Optional[PaidMedia]:
    '''
    Function to deserialize PaidMedia.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_PAID_MEDIA_PREVIEW:
        return PaidMediaPreview._dese(obj, check_dict=False)

    elif type == DEFAULT_PAID_MEDIA_PHOTO:
        return PaidMediaPhoto._dese(obj, check_dict=False)

    elif type == DEFAULT_PAID_MEDIA_VIDEO:
        return PaidMediaVideo._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type PaidMedia. Invalid type: {type!r}.'
        )


PassportElementError = Union[
    PassportElementErrorDataField,
    PassportElementErrorFrontSide,
    PassportElementErrorReverseSide,
    PassportElementErrorSelfie,
    PassportElementErrorFile,
    PassportElementErrorFiles,
    PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified
]
'''
https://core.telegram.org/bots/api#passportelementerror

This object represents an error in the Telegram Passport element which
was submitted that should be resolved by the user. It should be one of:

- :obj:`~apitele.types.PassportElementErrorDataField`
- :obj:`~apitele.types.PassportElementErrorFrontSide`
- :obj:`~apitele.types.PassportElementErrorReverseSide`
- :obj:`~apitele.types.PassportElementErrorSelfie`
- :obj:`~apitele.types.PassportElementErrorFile`
- :obj:`~apitele.types.PassportElementErrorFiles`
- :obj:`~apitele.types.PassportElementErrorTranslationFile`
- :obj:`~apitele.types.PassportElementErrorTranslationFiles`
- :obj:`~apitele.types.PassportElementErrorUnspecified`
'''


ReactionType = Union[
    ReactionTypeEmoji,
    ReactionTypeCustomEmoji,
    ReactionTypePaid
]
'''
https://core.telegram.org/bots/api#reactiontype

This object describes the type of a reaction. Currently, it can be one of:

- :obj:`~apitele.types.ReactionTypeEmoji`
- :obj:`~apitele.types.ReactionTypeCustomEmoji`
- :obj:`~apitele.types.ReactionTypePaid`
'''

def _dese_reaction_type(res: Optional[dict], /) -> Optional[ReactionType]:
    '''
    Function to deserialize ReactionType.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_REACTION_TYPE_EMOJI:
        return ReactionTypeEmoji._dese(obj, check_dict=False)

    elif type == DEFAULT_REACTION_TYPE_CUSTOM_EMOJI:
        return ReactionTypeCustomEmoji._dese(obj, check_dict=False)

    elif type == DEFAULT_REACTION_TYPE_PAID:
        return ReactionTypePaid._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type ReactionType. Invalid type: {type!r}.'
        )


RevenueWithdrawalState = Union[
    RevenueWithdrawalStatePending,
    RevenueWithdrawalStateSucceeded,
    RevenueWithdrawalStateFailed
]
'''
https://core.telegram.org/bots/api#revenuewithdrawalstate

This object describes the state of a revenue withdrawal operation.
Currently, it can be one of:

- :obj:`~apitele.types.RevenueWithdrawalStatePending`
- :obj:`~apitele.types.RevenueWithdrawalStateSucceeded`
- :obj:`~apitele.types.RevenueWithdrawalStateFailed`
'''

def _dese_revenue_withdrawal_state(res: Optional[dict], /) -> Optional[RevenueWithdrawalState]:
    '''
    Function to deserialize RevenueWithdrawalState.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_REVENUE_WITHDRAWAL_STATE_PENDING:
        return RevenueWithdrawalStatePending._dese(obj, check_dict=False)

    elif type == DEFAULT_REVENUE_WITHDRAWAL_STATE_SUCCEEDED:
        return RevenueWithdrawalStateSucceeded._dese(obj, check_dict=False)

    elif type == DEFAULT_REVENUE_WITHDRAWAL_STATE_FAILED:
        return RevenueWithdrawalStateFailed._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type RevenueWithdrawalState. Invalid type: {type!r}.'
        )


StoryAreaType = Union[
    StoryAreaTypeLocation,
    StoryAreaTypeSuggestedReaction,
    StoryAreaTypeLink,
    StoryAreaTypeWeather,
    StoryAreaTypeUniqueGift
]
'''
https://core.telegram.org/bots/api#storyareatype

Describes the type of a clickable area on a story. Currently, it can be one of:

- :obj:`~apitele.types.StoryAreaTypeLocation`
- :obj:`~apitele.types.StoryAreaTypeSuggestedReaction`
- :obj:`~apitele.types.StoryAreaTypeLink`
- :obj:`~apitele.types.StoryAreaTypeWeather`
- :obj:`~apitele.types.StoryAreaTypeUniqueGift`
'''


TransactionPartner = Union[
    TransactionPartnerAffiliateProgram,
    TransactionPartnerChat,
    TransactionPartnerFragment,
    TransactionPartnerUser,
    TransactionPartnerOther
]
'''
https://core.telegram.org/bots/api#transactionpartner

This object describes the source of a transaction, or its recipient for outgoing transactions.
Currently, it can be one of:

- :obj:`~apitele.types.TransactionPartnerAffiliateProgram`
- :obj:`~apitele.types.TransactionPartnerChat`
- :obj:`~apitele.types.TransactionPartnerFragment`
- :obj:`~apitele.types.TransactionPartnerUser`
- :obj:`~apitele.types.TransactionPartnerOther`
'''

def _dese_transaction_partner(res: Optional[dict], /) -> Optional[TransactionPartner]:
    '''
    Function to deserialize TransactionPartner.
    '''
    if res is None: return None
    obj = _check_dict(res)

    type = obj.pop('type')

    if type == DEFAULT_TRANSACTION_PARTNER_AFFILIATE_PROGRAM:
        return TransactionPartnerAffiliateProgram._dese(obj, check_dict=False)

    elif type == DEFAULT_TRANSACTION_PARTNER_CHAT:
        return TransactionPartnerChat._dese(obj, check_dict=False)

    elif type == DEFAULT_TRANSACTION_PARTNER_FRAGMENT:
        return TransactionPartnerFragment._dese(obj, check_dict=False)

    elif type == DEFAULT_TRANSACTION_PARTNER_USER:
        return TransactionPartnerUser._dese(obj, check_dict=False)

    elif type == DEFAULT_TRANSACTION_PARTNER_OTHER:
        return TransactionPartnerOther._dese(obj, check_dict=False)
    else:
        raise ValueError(
            'An error occurred during the deserialization'
            f' of the type TransactionPartner. Invalid type: {type!r}.'
        )
