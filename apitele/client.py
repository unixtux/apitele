#!/bin/env python3

__all__ = ()

import re
import asyncio
from .api import (
    TelegramApi,
    TelegramError,
)
from . import logger
from .types import *
from .types import (
    _dese_chat_member,
    _dese_menu_button,
)
from typing import (
    Any,
    Union,
    Literal,
    Optional,
    Callable,
    Awaitable,
)
from .update_manager import (
    UpdateManager,
    _run_coroutine,
    _is_next_function,
    MESSAGE_MANAGER,
    EDITED_MESSAGE_MANAGER, 
    CHANNEL_POST_MANAGER, 
    EDITED_CHANNEL_POST_MANAGER,
    BUSINESS_CONNECTION_MANAGER,
    BUSINESS_MESSAGE_MANAGER,
    EDITED_BUSINESS_MESSAGE_MANAGER,
    DELETED_BUSINESS_MESSAGES_MANAGER,
    MESSAGE_REACTION_MANAGER,
    MESSAGE_REACTION_COUNT_MANAGER,
    INLINE_QUERY_MANAGER,
    CHOSEN_INLINE_RESULT_MANAGER,
    CALLBACK_QUERY_MANAGER,
    SHIPPING_QUERY_MANAGER,
    PRE_CHECKOUT_QUERY_MANAGER,
    PURCHASED_PAID_MEDIA_MANAGER,
    POLL_MANAGER,
    POLL_ANSWER_MANAGER,
    MY_CHAT_MEMBER_MANAGER,
    CHAT_MEMBER_MANAGER,
    CHAT_JOIN_REQUEST_MANAGER,
    CHAT_BOOST_MANAGER,
    REMOVED_CHAT_BOOST_MANAGER,
)


class Client(TelegramApi):
    '''
    Main class to communicate with the `Telegram Bot API <https://core.telegram.org/bots/api>`_.

    :param token: Api token obtained from `@BotFather <https://t.me/botfather>`_.
    :type token: :obj:`str`
    :param proxy: Pass a proxy string to be used in the http requests.
    :type proxy: :obj:`str`, optional
    :param debug: Pass :obj:`True` for some debug information.
    :type debug: :obj:`bool`, optional
    :param deep_debug: Pass :obj:`True` for more debug information about http requests.
    :type deep_debug: :obj:`bool`, optional
    '''
    def __init__(
        self,
        token: str,
        *,
        proxy: Optional[str] = None,
        debug: Optional[bool] = None,
        deep_debug: Optional[bool] = None
    ):
        super().__init__(token, proxy, debug, deep_debug)

        self._offset = None

        self._user = None

        self._message_manager = UpdateManager(MESSAGE_MANAGER, Message)
        self._edited_message_manager = UpdateManager(EDITED_MESSAGE_MANAGER, Message)
        self._channel_post_manager = UpdateManager(CHANNEL_POST_MANAGER, Message)
        self._edited_channel_post_manager = UpdateManager(EDITED_CHANNEL_POST_MANAGER, Message)
        self._business_connection_manager = UpdateManager(BUSINESS_CONNECTION_MANAGER, BusinessConnection)
        self._business_message_manager = UpdateManager(BUSINESS_MESSAGE_MANAGER, Message)
        self._edited_business_message_manager = UpdateManager(EDITED_BUSINESS_MESSAGE_MANAGER, Message)
        self._deleted_business_messages_manager = UpdateManager(DELETED_BUSINESS_MESSAGES_MANAGER, BusinessMessagesDeleted)
        self._message_reaction_manager = UpdateManager(MESSAGE_REACTION_MANAGER, MessageReactionUpdated)
        self._message_reaction_count_manager = UpdateManager(MESSAGE_REACTION_COUNT_MANAGER, MessageReactionCountUpdated)
        self._inline_query_manager = UpdateManager(INLINE_QUERY_MANAGER, InlineQuery)
        self._chosen_inline_result_manager = UpdateManager(CHOSEN_INLINE_RESULT_MANAGER, ChosenInlineResult)
        self._callback_query_manager = UpdateManager(CALLBACK_QUERY_MANAGER, CallbackQuery)
        self._shipping_query_manager = UpdateManager(SHIPPING_QUERY_MANAGER, ShippingQuery)
        self._pre_checkout_query_manager = UpdateManager(PRE_CHECKOUT_QUERY_MANAGER, PreCheckoutQuery)
        self._purchased_paid_media_manager = UpdateManager(PURCHASED_PAID_MEDIA_MANAGER, PaidMediaPurchased)
        self._poll_manager = UpdateManager(POLL_MANAGER, Poll)
        self._poll_answer_manager = UpdateManager(POLL_ANSWER_MANAGER, PollAnswer)
        self._my_chat_member_manager = UpdateManager(MY_CHAT_MEMBER_MANAGER, ChatMemberUpdated)
        self._chat_member_manager = UpdateManager(CHAT_MEMBER_MANAGER, ChatMemberUpdated)
        self._chat_join_request_manager = UpdateManager(CHAT_JOIN_REQUEST_MANAGER, ChatJoinRequest)
        self._chat_boost_manager = UpdateManager(CHAT_BOOST_MANAGER, ChatBoostUpdated)
        self._removed_chat_boost_manager = UpdateManager(REMOVED_CHAT_BOOST_MANAGER, ChatBoostRemoved)

    @property
    def user(self) -> Optional[User]:
        return self._user

    # UpdateManagers

    def manage_message(self, checker: Callable[[Message], Any] = lambda message: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *message* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.Message`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.Message` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Message

            bot = apitele.Client('<your_api_token>')

            @bot.manage_message(lambda message: message.chat.id == xyz)
            async def foo(message: Message):
                ...

            asyncio.run(bot.long_polling())

        :param checker:  A function that takes only one argument to check an incoming *message* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[Message], Any]`
        '''
        def wrap(coroutine: Callable[[Message], Awaitable]):
            self._message_manager.add_rule(checker, coroutine)
        return wrap

    def manage_edited_message(self, checker: Callable[[Message], Any] = lambda edited_message: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *edited_message* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.Message`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.Message` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Message

            bot = apitele.Client('<your_api_token>')

            @bot.manage_edited_message(lambda edited_message: edited_message.chat.id == xyz)
            async def foo(edited_message: Message):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *edited_message* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[Message], Any]`
        '''
        def wrap(coroutine: Callable[[Message], Awaitable]):
            self._edited_message_manager.add_rule(checker, coroutine)
        return wrap

    def manage_channel_post(self, checker: Callable[[Message], Any] = lambda channel_post: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *channel_post* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.Message`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.Message` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Message

            bot = apitele.Client('<your_api_token>')

            @bot.manage_channel_post(lambda channel_post: channel_post.chat.id == xyz)
            async def foo(channel_post: Message):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *channel_post* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[Message], Any]`
        '''
        def wrap(coroutine: Callable[[Message], Awaitable]):
            self._channel_post_manager.add_rule(checker, coroutine)
        return wrap

    def manage_edited_channel_post(self, checker: Callable[[Message], Any] = lambda edited_channel_post: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *edited_channel_post* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.Message`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.Message` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Message

            bot = apitele.Client('<your_api_token>')

            @bot.manage_edited_channel_post(lambda edited_channel_post: edited_channel_post.chat.id == xyz)
            async def foo(edited_channel_post: Message):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *edited_channel_post* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[Message], Any]`
        '''
        def wrap(coroutine: Callable[[Message], Awaitable]):
            self._edited_channel_post_manager.add_rule(checker, coroutine)
        return wrap

    def manage_business_connection(self, checker: Callable[[BusinessConnection], Any] = lambda business_connection: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *business_connection* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.BusinessConnection`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.BusinessConnection` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import BusinessConnection

            bot = apitele.Client('<your_api_token>')

            @bot.manage_business_connection(lambda business_connection: business_connection.user.id == xyz)
            async def foo(business_connection: BusinessConnection):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *business_connection* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[BusinessConnection], Any]`
        '''
        def wrap(coroutine: Callable[[BusinessConnection], Awaitable]):
            self._business_connection_manager.add_rule(checker, coroutine)
        return wrap

    def manage_business_message(self, checker: Callable[[Message], Any] = lambda business_message: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *business_message* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.Message`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.Message` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Message

            bot = apitele.Client('<your_api_token>')

            @bot.manage_business_message(lambda business_message: business_message.chat.id == xyz)
            async def foo(business_message: Message):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *business_message* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[Message], Any]`
        '''
        def wrap(coroutine: Callable[[Message], Awaitable]):
            self._business_message_manager.add_rule(checker, coroutine)
        return wrap

    def manage_edited_business_message(self, checker: Callable[[Message], Any] = lambda edited_business_message: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *edited_business_message* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.Message`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.Message` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Message

            bot = apitele.Client('<your_api_token>')

            @bot.manage_business_message(lambda edited_business_message: edited_business_message.chat.id == xyz)
            async def foo(edited_business_message: Message):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *edited_business_message* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[Message], Any]`
        '''
        def wrap(coroutine: Callable[[Message], Awaitable]):
            self._edited_business_message_manager.add_rule(checker, coroutine)
        return wrap

    def manage_deleted_business_messages(self, checker: Callable[[BusinessMessagesDeleted], Any] = lambda deleted_business_messages: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *deleted_business_messages* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.BusinessMessagesDeleted`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.BusinessMessagesDeleted` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import BusinessMessagesDeleted

            bot = apitele.Client('<your_api_token>')

            @bot.manage_deleted_business_messages(lambda deleted_business_messages: deleted_business_messages.chat.id == xyz)
            async def foo(deleted_business_messages: BusinessMessagesDeleted):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *deleted_business_messages* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[BusinessMessagesDeleted], Any]`
        '''
        def wrap(coroutine: Callable[[BusinessMessagesDeleted], Awaitable]):
            self._deleted_business_messages_manager.add_rule(checker, coroutine)
        return wrap

    def manage_message_reaction(self, checker: Callable[[MessageReactionUpdated], Any] = lambda message_reaction: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *message_reaction* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.MessageReactionUpdated`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.MessageReactionUpdated` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import MessageReactionUpdated

            bot = apitele.Client('<your_api_token>')

            @bot.manage_message_reaction(lambda message_reaction: message_reaction.chat.id == xyz)
            async def foo(message_reaction: MessageReactionUpdated):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *message_reaction* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[MessageReactionUpdated], Any]`
        '''
        def wrap(coroutine: Callable[[MessageReactionUpdated], Awaitable]):
            self._message_reaction_manager.add_rule(checker, coroutine)
        return wrap

    def manage_message_reaction_count(self, checker: Callable[[MessageReactionCountUpdated], Any] = lambda message_reaction_count: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *message_reaction_count* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.MessageReactionCountUpdated`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.MessageReactionCountUpdated` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import MessageReactionCountUpdated

            bot = apitele.Client('<your_api_token>')

            @bot.manage_message_reaction_count(lambda message_reaction_count: message_reaction_count.chat.id == xyz)
            async def foo(message_reaction_count: MessageReactionCountUpdated):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *message_reaction_count* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[MessageReactionCountUpdated], Any]`
        '''
        def wrap(coroutine: Callable[[MessageReactionCountUpdated], Awaitable]):
            self._message_reaction_count_manager.add_rule(checker, coroutine)
        return wrap

    def manage_inline_query(self, checker: Callable[[InlineQuery], Any] = lambda inline_query: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *inline_query* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.InlineQuery`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.InlineQuery` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import InlineQuery

            bot = apitele.Client('<your_api_token>')

            @bot.manage_inline_query(lambda inline_query: inline_query.from_user.id == xyz)
            async def foo(inline_query: InlineQuery):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *inline_query* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[InlineQuery], Any]`
        '''
        def wrap(coroutine: Callable[[InlineQuery], Awaitable]):
            self._inline_query_manager.add_rule(checker, coroutine)
        return wrap

    def manage_chosen_inline_result(self, checker: Callable[[ChosenInlineResult], Any] = lambda chosen_inline_result: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *chosen_inline_result* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.ChosenInlineResult`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.ChosenInlineResult` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import ChosenInlineResult

            bot = apitele.Client('<your_api_token>')

            @bot.manage_chosen_inline_result(lambda chosen_inline_result: chosen_inline_result.from_user.id == xyz)
            async def foo(chosen_inline_result: ChosenInlineResult):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *chosen_inline_result* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[ChosenInlineResult], Any]`
        '''
        def wrap(coroutine: Callable[[ChosenInlineResult], Awaitable]):
            self._chosen_inline_result_manager.add_rule(checker, coroutine)
        return wrap

    def manage_callback_query(self, checker: Callable[[CallbackQuery], Any] = lambda callback_query: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *callback_query* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.CallbackQuery`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.CallbackQuery` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import CallbackQuery

            bot = apitele.Client('<your_api_token>')

            @bot.manage_callback_query(lambda callback_query: callback_query.from_user.id == xyz)
            async def foo(callback_query: CallbackQuery):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *callback_query* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[CallbackQuery], Any]`
        '''
        def wrap(coroutine: Callable[[CallbackQuery], Awaitable]):
            self._callback_query_manager.add_rule(checker, coroutine)
        return wrap

    def manage_shipping_query(self, checker: Callable[[ShippingQuery], Any] = lambda shipping_query: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *shipping_query* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.ShippingQuery`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.ShippingQuery` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import ShippingQuery

            bot = apitele.Client('<your_api_token>')

            @bot.manage_shipping_query(lambda shipping_query: shipping_query.from_user.id == xyz)
            async def foo(shipping_query: ShippingQuery):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *shipping_query* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[ShippingQuery], Any]`
        '''
        def wrap(coroutine: Callable[[ShippingQuery], Awaitable]):
            self._shipping_query_manager.add_rule(checker, coroutine)
        return wrap

    def manage_pre_checkout_query(self, checker: Callable[[PreCheckoutQuery], Any] = lambda pre_checkout_query: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *pre_checkout_query* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.PreCheckoutQuery`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.PreCheckoutQuery` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import PreCheckoutQuery

            bot = apitele.Client('<your_api_token>')

            @bot.manage_pre_checkout_query(lambda pre_checkout_query: pre_checkout_query.from_user.id == xyz)
            async def foo(pre_checkout_query: PreCheckoutQuery):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *pre_checkout_query* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[PreCheckoutQuery], Any]`
        '''
        def wrap(coroutine: Callable[[PreCheckoutQuery], Awaitable]):
            self._pre_checkout_query_manager.add_rule(checker, coroutine)
        return wrap

    def manage_purchased_paid_media(self, checker: Callable[[PaidMediaPurchased], Any], /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *purchased_paid_media* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.PaidMediaPurchased`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.PaidMediaPurchased` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import PaidMediaPurchased

            bot = apitele.Client('<your_api_token>')

            @bot.manage_purchased_paid_media(lambda purchased_paid_media: purchased_paid_media.from_user.id == xyz)
            async def foo(purchased_paid_media: PaidMediaPurchased):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *purchased_paid_media* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[PaidMediaPurchased], Any]`
        '''
        def wrap(coroutine: Callable[[PaidMediaPurchased], Awaitable]):
            self._purchased_paid_media_manager.add_rule(checker, coroutine)
        return wrap

    def manage_poll(self, checker: Callable[[Poll], Any] = lambda poll: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *poll* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.Poll`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.Poll` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Poll

            bot = apitele.Client('<your_api_token>')

            @bot.manage_poll(lambda poll: poll.id == xyz)
            async def foo(poll: Poll):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *poll* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[Poll], Any]`
        '''
        def wrap(coroutine: Callable[[Poll], Awaitable]):
            self._poll_manager.add_rule(checker, coroutine)
        return wrap

    def manage_poll_answer(self, checker: Callable[[PollAnswer], Any] = lambda poll_answer: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *poll_answer* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.PollAnswer`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.PollAnswer` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import PollAnswer

            bot = apitele.Client('<your_api_token>')

            @bot.manage_poll_answer(lambda poll_answer: poll_answer.poll_id == xyz)
            async def foo(poll_answer: PollAnswer):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *poll_answer* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[PollAnswer], Any]`
        '''
        def wrap(coroutine: Callable[[PollAnswer], Awaitable]):
            self._poll_answer_manager.add_rule(checker, coroutine)
        return wrap

    def manage_my_chat_member(self, checker: Callable[[ChatMemberUpdated], Any] = lambda my_chat_member: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *my_chat_member* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.ChatMemberUpdated`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.ChatMemberUpdated` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import ChatMemberUpdated

            bot = apitele.Client('<your_api_token>')

            @bot.manage_my_chat_member(lambda my_chat_member: my_chat_member.chat.id == xyz)
            async def foo(my_chat_member: ChatMemberUpdated):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *my_chat_member* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[ChatMemberUpdated], Any]`
        '''
        def wrap(coroutine: Callable[[ChatMemberUpdated], Awaitable]):
            self._my_chat_member_manager.add_rule(checker, coroutine)
        return wrap

    def manage_chat_member(self, checker: Callable[[ChatMemberUpdated], Any] = lambda chat_member: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *chat_member* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.ChatMemberUpdated`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.ChatMemberUpdated` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import ChatMemberUpdated

            bot = apitele.Client('<your_api_token>')

            @bot.manage_chat_member(lambda chat_member: chat_member.chat.id == xyz)
            async def foo(chat_member: ChatMemberUpdated):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *chat_member* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[ChatMemberUpdated], Any]`
        '''
        def wrap(coroutine: Callable[[ChatMemberUpdated], Awaitable]):
            self._chat_member_manager.add_rule(checker, coroutine)
        return wrap

    def manage_chat_join_request(self, checker: Callable[[ChatJoinRequest], Any] = lambda chat_join_request: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *chat_join_request* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.ChatJoinRequest`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.ChatJoinRequest` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import ChatJoinRequest

            bot = apitele.Client('<your_api_token>')

            @bot.manage_chat_join_request(lambda chat_join_request: chat_join_request.chat.id == xyz)
            async def foo(chat_join_request: ChatJoinRequest):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *chat_join_request* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[ChatJoinRequest], Any]`
        '''
        def wrap(coroutine: Callable[[ChatJoinRequest], Awaitable]):
            self._chat_join_request_manager.add_rule(checker, coroutine)
        return wrap

    def manage_chat_boost(self, checker: Callable[[ChatBoostUpdated], Any] = lambda chat_boost: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *chat_boost* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.ChatBoostUpdated`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.ChatBoostUpdated` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import ChatBoostUpdated

            bot = apitele.Client('<your_api_token>')

            @bot.manage_chat_boost(lambda chat_boost: chat_boost.chat.id == xyz)
            async def foo(chat_boost: ChatBoostUpdated):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *chat_boost* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[ChatBoostUpdated], Any]`
        '''
        def wrap(coroutine: Callable[[ChatBoostUpdated], Awaitable]):
            self._chat_boost_manager.add_rule(checker, coroutine)
        return wrap

    def manage_removed_chat_boost(self, checker: Callable[[ChatBoostRemoved], Any] = lambda removed_chat_boost: ..., /):
        '''
        You must wrap a `coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
        inside this decorator to manage an incoming *removed_chat_boost* :obj:`~apitele.types.Update`.
        The coroutine must takes only one argument, it will be processed as :obj:`~apitele.types.ChatBoostRemoved`.
        Then you need to call the method :meth:`~apitele.Client.long_polling` using the function `asyncio.run() <https://docs.python.org/3/library/asyncio-runner.html#asyncio.run>`_ to process the :obj:`~apitele.types.ChatBoostRemoved` update.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import ChatBoostRemoved

            bot = apitele.Client('<your_api_token>')

            @bot.manage_removed_chat_boost(lambda removed_chat_boost: removed_chat_boost.chat.id == xyz)
            async def foo(removed_chat_boost: ChatBoostRemoved):
                ...

            asyncio.run(bot.long_polling())

        :param checker: A function that takes only one argument to check an incoming *removed_chat_boost* :obj:`~apitele.types.Update`. E.g. a lambda function.
        :type checker: :obj:`Callable[[ChatBoostRemoved], Any]`
        '''
        def wrap(coroutine: Callable[[ChatBoostRemoved], Awaitable]):
            self._removed_chat_boost_manager.add_rule(checker, coroutine)
        return wrap


    # Processing new updates

    async def long_polling(
        self,
        timeout: int = 45,
        *,
        limit: Optional[int] = None,
        allowed_updates: Optional[list[str]] = None
    ):
        '''
        Use this method with the `asyncio <https://docs.python.org/3/library/asyncio.html>`_
        module, to receive :obj:`updates <apitele.types.Update>` from the Telegram Bot API Server
        and manage them using decorators method like :meth:`~apitele.Client.manage_message`.

        Usage:

        .. code-block:: python3

            import apitele
            import asyncio
            from apitele.types import Message

            bot = apitele.Client('<your_api_token>')

            @bot.manage_message()
            async def foo(msg: Message):
                await bot.send_message(msg.chat.id, 'hello')

            asyncio.run(bot.long_polling())

        :param timeout: Timeout in seconds for `long polling <https://en.wikipedia.org/wiki/Push_technology#Long_polling>`_. Should be higher than 30, short polling should be used for testing purposes only.
        :type timeout: :obj:`int`
        :param limit: Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to :obj:`100`.
        :type limit: :obj:`int`, optional
        :param allowed_updates:
            A JSON-serialized list of the update types you want your bot to receive. For example, specify ``["message", "edited_channel_post", "callback_query"]`` to only receive updates of these types. See :obj:`~apitele.types.Update` for a complete list of available update types. Specify an empty list to receive all update types except *chat_member*, *message_reaction*, and *message_reaction_count* (default). If not specified, the previous setting will be used.

            Please note that this parameter doesn't affect updates created before the call to the :meth:`~apitele.Client.get_updates`, so unwanted updates may be received for a short period of time.
        :type allowed_updates: :obj:`list` of :obj:`str`, optional
        '''
        if not type(timeout) in (int, float):
            raise TypeError(
                'long polling timeout must be int or float,'
                ' got {}.'.format(timeout.__class__.__name__)
            )
        params = {'timeout': timeout}
        if limit is not None: params['limit'] = limit
        if allowed_updates is not None: params['allowed_updates'] = allowed_updates
        await self.get_me()
        logger.info('Welcome @{}.'.format(self.user.username))
        logger.info('long polling has been started.')
        bad_gateway = re.compile(r'bad.*gateway', re.IGNORECASE)
        while True:
            try:
                if self._offset is not None:
                    params['offset'] = self._offset

                result = await super().get_updates(
                    params,
                    max_retries=float('inf'),
                    keep_alive=True
                )
                updates = [Update._dese(update) for update in result]

            except TelegramError as exc:
                if bad_gateway.search(exc.description):
                    logger.error('{!r} occurred in long polling.'.format(exc))
                    await asyncio.sleep(2)
                else:
                    await self.session.close()
                    logger.info('long polling was interrupted.')
                    raise exc from None

            except BaseException as exc:
                await self.session.close()
                logger.info('long polling was interrupted.')
                raise exc from None
            else:
                if updates:
                    self._offset = updates[-1].update_id + 1
                    for update in updates:
                        asyncio.create_task(self._process_update(update))


    async def _process_update(self, update: Update, /):

        if update.message:
            obj: Message = update.message
            for rule in self._message_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.edited_message:
            obj: Message = update.edited_message
            for rule in self._edited_message_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.channel_post:
            obj: Message = update.channel_post
            for rule in self._channel_post_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.edited_channel_post:
            obj: Message = update.edited_channel_post
            for rule in self._edited_channel_post_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.business_connection:
            obj: BusinessConnection = update.business_connection
            for rule in self._business_connection_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.business_message:
            obj: Message = update.business_message
            for rule in self._business_message_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.edited_business_message:
            obj: Message = update.edited_business_message
            for rule in self._edited_business_message_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.deleted_business_messages:
            obj: BusinessMessagesDeleted = update.deleted_business_messages
            for rule in self._deleted_business_messages_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.message_reaction:
            obj: MessageReactionUpdated = update.message_reaction
            for rule in self._message_reaction_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.message_reaction_count:
            obj: MessageReactionCountUpdated = update.message_reaction_count
            for rule in self._message_reaction_count_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.inline_query:
            obj: InlineQuery = update.inline_query
            for rule in self._inline_query_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.chosen_inline_result:
            obj: ChosenInlineResult = update.chosen_inline_result
            for rule in self._chosen_inline_result_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.callback_query:
            obj: CallbackQuery = update.callback_query
            for rule in self._callback_query_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.shipping_query:
            obj: ShippingQuery = update.shipping_query
            for rule in self._shipping_query_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.pre_checkout_query:
            obj: PreCheckoutQuery = update.pre_checkout_query
            for rule in self._pre_checkout_query_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.purchased_paid_media:
            obj: PaidMediaPurchased = update.purchased_paid_media
            for rule in self._purchased_paid_media_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.poll:
            obj: Poll = update.poll
            for rule in self._poll_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.poll_answer:
            obj: PollAnswer = update.poll_answer
            for rule in self._poll_answer_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.my_chat_member:
            obj: ChatMemberUpdated = update.my_chat_member
            for rule in self._my_chat_member_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.chat_member:
            obj: ChatMemberUpdated = update.chat_member
            for rule in self._chat_member_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.chat_join_request:
            obj: ChatJoinRequest = update.chat_join_request
            for rule in self._chat_join_request_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.chat_boost:
            obj: ChatBoostUpdated = update.chat_boost
            for rule in self._chat_boost_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

        elif update.removed_chat_boost:
            obj: ChatBoostRemoved = update.removed_chat_boost
            for rule in self._removed_chat_boost_manager:
                result = await _run_coroutine(rule, obj)
                if not _is_next_function(result):
                    return

    # Available methods

    async def add_sticker_to_set(
        self,
        user_id: int,
        name: str,
        sticker: InputSticker
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#addstickertoset

        Use this method to add a new sticker to a set created by the bot.
        Emoji sticker sets can have up to 200 stickers.
        Other sticker sets can have up to 120 stickers. Returns :obj:`True` on success.

        :param user_id: User identifier of sticker set owner.
        :type user_id: :obj:`int`
        :param name: Sticker set name.
        :type name: :obj:`str`
        :param sticker: A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn't changed.
        :type sticker: :obj:`~apitele.types.InputSticker`
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'name': name,
            'sticker': sticker
        }
        return await super().add_sticker_to_set(params)


    async def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#answercallbackquery

        Use this method to send answers to callback queries sent from `inline
        keyboards <https://core.telegram.org/bots/features#inline-keyboards>`_.
        The answer will be displayed to the user as a notification at the top
        of the chat screen or as an alert. On success, :obj:`True` is returned.

            Alternatively, the user can be redirected to the specified Game URL.
            For this option to work, you must first create a game for your bot via `@BotFather <https://t.me/botfather>`_ and accept the terms.
            Otherwise, you may use links like ``t.me/your_bot?start=XXXX`` that open your bot with a parameter.

        :param callback_query_id: Unique identifier for the query to be answered.
        :type callback_query_id: :obj:`str`
        :param text: Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters.
        :type text: :obj:`str`, optional
        :param show_alert: If :obj:`True`, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to :obj:`False`.
        :type show_alert: :obj:`bool`, optional
        :param url:
            URL that will be opened by the user's client. If you have created a :obj:`~apitele.types.Game` and accepted the conditions via `@BotFather <https://t.me/botfather>`_, specify the URL that opens your game - note that this will only work if the query comes from a :obj:`callback_game <apitele.types.InlineKeyboardButton>` button.

            Otherwise, you may use links like ``t.me/your_bot?start=XXXX`` that open your bot with a parameter.
        :type url: :obj:`str`, optional
        :param cache_time: The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to :obj:`0`.
        :type cache_time: :obj:`int`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'callback_query_id': callback_query_id
        }
        if text is not None: params['text'] = text
        if show_alert is not None: params['show_alert'] = show_alert
        if url is not None: params['url'] = url
        if cache_time is not None: params['cache_time'] = cache_time
        return await super().answer_callback_query(params)


    async def answer_inline_query(
        self,
        inline_query_id: str,
        results: list[InlineQueryResult],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        button: Optional[InlineQueryResultsButton] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#answerinlinequery

        Use this method to send answers to an inline query. On success,
        :obj:`True` is returned. No more than **50** results per query are allowed.

        :param inline_query_id: Unique identifier for the answered query.
        :type inline_query_id: :obj:`str`
        :param results: A JSON-serialized array of results for the inline query.
        :type results: :obj:`list` of :obj:`~apitele.types.InlineQueryResult`
        :param cache_time: The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to :obj:`300`.
        :type cache_time: :obj:`int`, optional
        :param is_personal: Pass :obj:`True` if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query.
        :type is_personal: :obj:`bool`, optional
        :param next_offset: Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
        :type next_offset: :obj:`str`, optional
        :param button: A JSON-serialized object describing a button to be shown above inline query results.
        :type button: :obj:`~apitele.types.InlineQueryResultsButton`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'inline_query_id': inline_query_id,
            'results': results
        }
        if cache_time is not None: params['cache_time'] = cache_time
        if is_personal is not None: params['is_personal'] = is_personal
        if next_offset is not None: params['next_offset'] = next_offset
        if button is not None: params['button'] = button
        return await super().answer_inline_query(params)


    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#answerprecheckoutquery

        Once the user has confirmed their payment and shipping details, the Bot API sends the
        final confirmation in the form of an :obj:`~apitele.types.Update` with the field *pre_checkout_query*. Use this
        method to respond to such pre-checkout queries. On success, :obj:`True` is returned. **Note**: The
        Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

        :param pre_checkout_query_id: Unique identifier for the query to be answered.
        :type pre_checkout_query_id: :obj:`str`
        :param ok: Specify :obj:`True` if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use :obj:`False` if there are any problems.
        :type ok: :obj:`bool`
        :param error_message: Required if *ok* is :obj:`False`. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.
        :type error_message: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'pre_checkout_query_id': pre_checkout_query_id,
            'ok': ok
        }
        if error_message is not None: params['error_message'] = error_message
        return await super().answer_pre_checkout_query(params)


    async def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: Optional[list[ShippingOption]] = None,
        error_message: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#answershippingquery

        If you sent an invoice requesting a shipping address and the parameter *is_flexible*
        was specified, the Bot API will send an :obj:`~apitele.types.Update` with a *shipping_query* field to the
        bot. Use this method to reply to shipping queries. On success, :obj:`True` is returned.

        :param shipping_query_id: Unique identifier for the query to be answered.
        :type shipping_query_id: :obj:`str`
        :param ok: Pass :obj:`True` if delivery to the specified address is possible and :obj:`False` if there are any problems (for example, if delivery to the specified address is not possible).
        :type ok: :obj:`bool`
        :param shipping_options: Required if *ok* is :obj:`True`. A JSON-serialized array of available shipping options.
        :type shipping_options: :obj:`list` of :obj:`~apitele.types.ShippingOption`, optional
        :param error_message: Required if *ok* is :obj:`False`. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user.
        :type error_message: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'shipping_query_id': shipping_query_id,
            'ok': ok
        }
        if shipping_options is not None: params['shipping_options'] = shipping_options
        if error_message is not None: params['error_message'] = error_message
        return await super().answer_shipping_query(params)


    async def answer_web_app_query(
        self,
        web_app_query_id: str,
        result: InlineQueryResult
    ) -> SentWebAppMessage:
        '''
        https://core.telegram.org/bots/api#answerwebappquery

        Use this method to set the result of an interaction with a
        `Web App <https://core.telegram.org/bots/webapps>`_ and send a corresponding message on behalf of
        the user to the chat from which the query originated. On success, a :obj:`~apitele.types.SentWebAppMessage` object is returned.

        :param web_app_query_id: Unique identifier for the query to be answered.
        :type web_app_query_id: :obj:`str`
        :param result: A JSON-serialized object describing the message to be sent.
        :type result: :obj:`~apitele.types.InlineQueryResult`
        :rtype: :obj:`~apitele.types.SentWebAppMessage`
        '''
        params = {
            'web_app_query_id': web_app_query_id,
            'result': result
        }
        result = await super().answer_web_app_query(params)
        return SentWebAppMessage._dese(result)


    async def approve_chat_join_request(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#approvechatjoinrequest

        Use this method to approve a chat join request. The bot must be an administrator in the chat
        for this to work and must have the *can_invite_users* administrator right. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await super().approve_chat_join_request(params)


    async def ban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#banchatmember

        Use this method to ban a user in a group, a supergroup or a channel. In the case of
        supergroups and channels, the user will not be able to return to the chat on their own using
        invite links, etc., unless :meth:`unbanned <apitele.Client.unban_chat_member>` first. The bot must be an administrator
        in the chat for this to work and must have the appropriate administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :param until_date: Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.
        :type until_date: :obj:`int`, optional
        :param revoke_messages: Pass :obj:`True` to delete all messages from the chat for the user that is being removed. If :obj:`False`, the user will be able to see messages in the group that were sent before the user was removed. Always :obj:`True` for supergroups and channels.
        :type revoke_messages: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        if until_date is not None: params['until_date'] = until_date
        if revoke_messages is not None: params['revoke_messages'] = revoke_messages
        return await super().ban_chat_member(params)


    async def ban_chat_sender_chat(
        self,
        chat_id: Union[int, str],
        sender_chat_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#banchatsenderchat

        Use this method to ban a channel chat in a supergroup or a channel. Until the chat
        is :meth:`unbanned <apitele.Client.unban_chat_sender_chat>`, the owner of the banned chat won't be able to
        send messages on behalf of **any of their channels**. The bot must be an administrator in the supergroup or
        channel for this to work and must have the appropriate administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param sender_chat_id: Unique identifier of the target sender chat.
        :type sender_chat_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id
        }
        return await super().ban_chat_sender_chat(params)


    async def close(self) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#close

        Use this method to close the bot instance before moving it from one local server to another. You need to delete the
        webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will
        return error 429 in the first 10 minutes after the bot is launched. Returns :obj:`True` on success. Requires no parameters.

        :rtype: :obj:`True`
        '''
        return await super().close()


    async def close_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#closeforumtopic

        Use this method to close an open topic in a forum supergroup chat. The bot must
        be an administrator in the chat for this to work and must have the *can_manage_topics*
        administrator rights, unless it is the creator of the topic. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_thread_id: Unique identifier for the target message thread of the forum topic.
        :type message_thread_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().close_forum_topic(params)


    async def close_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#closegeneralforumtopic

        Use this method to close an open 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the *can_manage_topics* administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().close_general_forum_topic(params)


    async def convert_gift_to_stars(
        self,
        business_connection_id: str,
        owned_gift_id: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#convertgifttostars

        Converts a given regular gift to Telegram Stars. Requires the *can_convert_gifts_to_stars* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param owned_gift_id: Unique identifier of the regular gift that should be converted to Telegram Stars.
        :type owned_gift_id: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'owned_gift_id': owned_gift_id
        }
        return await super().convert_gift_to_stars(params)


    async def copy_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        video_start_timestamp: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> MessageId:
        '''
        https://core.telegram.org/bots/api#copymessage

        Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied.
        A quiz :obj:`poll <apitele.types.Poll>` can be copied only if the value of the field *correct_option_id* is known to the bot. The method is analogous to the method
        :meth:`~apitele.Client.forward_message`, but the copied message doesn't have a link to the original message. Returns the :obj:`~apitele.types.MessageId` of the sent message on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format ``@channelusername``).
        :type from_chat_id: :obj:`int` or :obj:`str`
        :param message_id: Message identifier in the chat specified in *from_chat_id*.
        :type message_id: :obj:`int`
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param video_start_timestamp: New start timestamp for the copied video in the message.
        :type video_start_timestamp: :obj:`int`, optional
        :param caption: New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the new caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media. Ignored if a new caption isn't specified.
        :type show_caption_above_media: :obj:`bool`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.MessageId`
        '''
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if video_start_timestamp is not None: params['video_start_timestamp'] = video_start_timestamp
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if show_caption_above_media is not None: params['show_caption_above_media'] = show_caption_above_media
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().copy_message(params)
        return MessageId._dese(result)


    async def copy_messages(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: list[int],
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        remove_caption: Optional[bool] = None
    ) -> list[MessageId]:
        '''
        https://core.telegram.org/bots/api#copymessages

        Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages,
        giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz :obj:`poll <apitele.types.Poll>` can be copied only if the value
        of the field *correct_option_id* is known to the bot. The method is analogous to the method :meth:`~apitele.Client.forward_messages`, but the copied messages don't have
        a link to the original message. Album grouping is kept for copied messages. On success, an array of :obj:`~apitele.types.MessageId` of the sent messages is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param from_chat_id: Unique identifier for the chat where the original messages were sent (or channel username in the format ``@channelusername``).
        :type from_chat_id: :obj:`int` or :obj:`str`
        :param message_ids: Identifiers of 1-100 messages in the chat *from_chat_id* to copy. The identifiers must be specified in a strictly increasing order.
        :type message_ids: :obj:`list` of :obj:`int`
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param disable_notification: Sends the messages `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent messages from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param remove_caption: Pass :obj:`True` to copy the messages without their captions.
        :type remove_caption: :obj:`bool`, optional
        :rtype: :obj:`list` of :obj:`~apitele.types.MessageId`
        '''
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_ids': message_ids
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if remove_caption is not None: params['remove_caption'] = remove_caption
        result = await super().copy_messages(params)
        return [MessageId._dese(mid) for mid in result]


    async def create_chat_invite_link(
        self,
        chat_id: Union[int, str],
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None
    ) -> ChatInviteLink:
        '''
        https://core.telegram.org/bots/api#createchatinvitelink

        Use this method to create an additional invite link for a chat. The bot must be an administrator
        in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the
        method :meth:`~apitele.Client.revoke_chat_invite_link`. Returns the new invite link as :obj:`~apitele.types.ChatInviteLink` object.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param name: Invite link name; 0-32 characters.
        :type name: :obj:`str`, optional
        :param expire_date: Point in time (Unix timestamp) when the link will expire.
        :type expire_date: :obj:`int`, optional
        :param member_limit: The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.
        :type member_limit: :obj:`int`, optional
        :param creates_join_request: :obj:`True`, if users joining the chat via the link need to be approved by chat administrators. If :obj:`True`, *member_limit* can't be specified.
        :type creates_join_request: :obj:`bool`, optional
        :rtype: :obj:`~apitele.types.ChatInviteLink`
        '''
        params = {
            'chat_id': chat_id
        }
        if name is not None: params['name'] = name
        if expire_date is not None: params['expire_date'] = expire_date
        if member_limit is not None: params['member_limit'] = member_limit
        if creates_join_request is not None: params['creates_join_request'] = creates_join_request
        result = await super().create_chat_invite_link(params)
        return ChatInviteLink._dese(result)


    async def create_chat_subscription_invite_link(
        self,
        chat_id: Union[int, str],
        subscription_period: int,
        subscription_price: int,
        name: Optional[str] = None
    ) -> ChatInviteLink:
        '''
        https://core.telegram.org/bots/api#createchatsubscriptioninvitelink

        Use this method to create a `subscription invite link <https://telegram.org/blog/superchannels-star-reactions-subscriptions#star-subscriptions>`_ for a channel chat.
        The bot must have the *can_invite_users* administrator rights. The link can be edited using the method :meth:`~apitele.Client.edit_chat_subscription_invite_link`
        or revoked using the method :meth:`~apitele.Client.revoke_chat_invite_link`. Returns the new invite link as a :obj:`~apitele.types.ChatInviteLink` object.

        :param chat_id: Unique identifier for the target channel chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param subscription_period: The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days).
        :type subscription_period: :obj:`int`
        :param subscription_price: The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-2500.
        :type subscription_price: :obj:`int`
        :param name: Invite link name; 0-32 characters.
        :type name: :obj:`str`, optional
        :rtype: :obj:`~apitele.types.ChatInviteLink`
        '''
        params = {
            'chat_id': chat_id,
            'subscription_period': subscription_period,
            'subscription_price': subscription_price
        }
        if name is not None: params['name'] = name
        result = await super().create_chat_subscription_invite_link(params)
        return ChatInviteLink._dese(result)


    async def create_forum_topic(
        self,
        chat_id: Union[int, str],
        name: str,
        icon_color: Optional[int] = None,
        icon_custom_emoji_id: Optional[str] = None
    ) -> ForumTopic:
        '''
        https://core.telegram.org/bots/api#createforumtopic

        Use this method to create a topic in a forum supergroup chat. The bot must be an
        administrator in the chat for this to work and must have the *can_manage_topics* administrator
        rights. Returns information about the created topic as a :obj:`~apitele.types.ForumTopic` object.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param name: Topic name, 1-128 characters.
        :type name: :obj:`str`
        :param icon_color: Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F).
        :type icon_color: :obj:`int`, optional
        :param icon_custom_emoji_id: Unique identifier of the custom emoji shown as the topic icon. Use :meth:`~apitele.Client.get_forum_topic_icon_stickers` to get all allowed custom emoji identifiers.
        :type icon_custom_emoji_id: :obj:`str`, optional
        :rtype: :obj:`~apitele.types.ForumTopic`
        '''
        params = {
            'chat_id': chat_id,
            'name': name
        }
        if icon_color is not None: params['icon_color'] = icon_color
        if icon_custom_emoji_id is not None: params['icon_custom_emoji_id'] = icon_custom_emoji_id
        result = await super().create_forum_topic(params)
        return ForumTopic._dese(result)


    async def create_invoice_link(
        self,
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: list[LabeledPrice],
        business_connection_id: Optional[str] = None,
        provider_token: Optional[str] = None,
        subscription_period: Optional[int] = None,
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
    ) -> str:
        '''
        https://core.telegram.org/bots/api#createinvoicelink

        Use this method to create a link for an invoice. Returns the created invoice link as :obj:`String` on success.

        :param title: Product name, 1-32 characters.
        :type title: :obj:`str`
        :param description: Product description, 1-255 characters.
        :type description: :obj:`str`
        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
        :type payload: :obj:`str`
        :param currency: Three-letter ISO 4217 currency code, see `more on currencies <https://core.telegram.org/bots/payments#supported-currencies>`_. Pass “XTR” for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type currency: :obj:`str`
        :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in `Telegram Stars <https://t.me/BotNews/90>`_
        :type prices: :obj:`list` of :obj:`~apitele.types.LabeledPrice`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the link will be created. For payments in `Telegram Stars <https://t.me/BotNews/90>`_ only.
        :type business_connection_id: :obj:`str`, optional
        :param provider_token: Payment provider token, obtained via `BotFather <https://t.me/botfather>`_. Pass an empty string for payments in `Telegram Stars <https://t.me/BotNews/90>`_
        :type provider_token: :obj:`str`, optional
        :param subscription_period: The number of seconds the subscription will be active for before the next payment. The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must no exceed 10000 Telegram Stars.
        :type subscription_period: :obj:`int`, optional
        :param max_tip_amount: The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of ``US$ 1.45`` pass ``max_tip_amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to :obj:`0`. Not supported for payments in `Telegram Stars <https://t.me/BotNews/90>`_
        :type max_tip_amount: :obj:`int`, optional
        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*.
        :type suggested_tip_amounts: :obj:`list` of :obj:`int`, optional
        :param provider_data: JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
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
        :param send_phone_number_to_provider: Pass :obj:`True` if the user's phone number should be sent to the provider. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type send_phone_number_to_provider: :obj:`bool`, optional
        :param send_email_to_provider: Pass :obj:`True` if the user's email address should be sent to the provider. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type send_email_to_provider: :obj:`bool`, optional
        :param is_flexible: Pass :obj:`True` if the final price depends on the shipping method. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type is_flexible: :obj:`bool`, optional
        :rtype: :obj:`str`
        '''
        params = {
            'title': title,
            'description': description,
            'payload': payload,
            'currency': currency,
            'prices': prices
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if provider_token is not None: params['provider_token'] = provider_token
        if subscription_period is not None: params['subscription_period'] = subscription_period
        if max_tip_amount is not None: params['max_tip_amount'] = max_tip_amount
        if suggested_tip_amounts is not None: params['suggested_tip_amounts'] = suggested_tip_amounts
        if provider_data is not None: params['provider_data'] = provider_data
        if photo_url is not None: params['photo_url'] = photo_url
        if photo_size is not None: params['photo_size'] = photo_size
        if photo_width is not None: params['photo_width'] = photo_width
        if photo_height is not None: params['photo_height'] = photo_height
        if need_name is not None: params['need_name'] = need_name
        if need_phone_number is not None: params['need_phone_number'] = need_phone_number
        if need_email is not None: params['need_email'] = need_email
        if need_shipping_address is not None: params['need_shipping_address'] = need_shipping_address
        if send_phone_number_to_provider is not None: params['send_phone_number_to_provider'] = send_phone_number_to_provider
        if send_email_to_provider is not None: params['send_email_to_provider'] = send_email_to_provider
        if is_flexible is not None: params['is_flexible'] = is_flexible
        return await super().create_invoice_link(params)


    async def create_new_sticker_set(
        self,
        user_id: int,
        name: str,
        title: str,
        stickers: list[InputSticker],
        sticker_type: Optional[str] = None,
        needs_repainting: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#createnewstickerset

        Use this method to create a new sticker set owned by a user. The bot
        will be able to edit the sticker set thus created. Returns :obj:`True` on success.

        :param user_id: User identifier of created sticker set owner.
        :type user_id: :obj:`int`
        :param name: Short name of sticker set, to be used in ``t.me/addstickers/`` URLs (e.g., *animals*). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in ``"_by_<bot_username>"``. ``<bot_username>`` is case insensitive. 1-64 characters.
        :type name: :obj:`str`
        :param title: Sticker set title, 1-64 characters.
        :type title: :obj:`str`
        :param stickers: A JSON-serialized list of 1-50 initial stickers to be added to the sticker set.
        :type stickers: :obj:`list` of :obj:`~apitele.types.InputSticker`
        :param sticker_type: Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created.
        :type sticker_type: :obj:`str`, optional
        :param needs_repainting: Pass :obj:`True` if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only.
        :type needs_repainting: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'name': name,
            'title': title,
            'stickers': stickers
        }
        if sticker_type is not None: params['sticker_type'] = sticker_type
        if needs_repainting is not None: params['needs_repainting'] = needs_repainting
        return await super().create_new_sticker_set(params)


    async def decline_chat_join_request(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#declinechatjoinrequest

        Use this method to decline a chat join request. The bot must be an administrator in the chat
        for this to work and must have the *can_invite_users* administrator right. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await super().decline_chat_join_request(params)


    async def delete_business_messages(
        self,
        business_connection_id: str,
        message_ids: list[int]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletebusinessmessages

        Delete messages on behalf of a business account. Requires the *can_delete_sent_messages* business bot right to delete messages
        sent by the bot itself, or the *can_delete_all_messages* business bot right to delete any message. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection on behalf of which to delete the messages.
        :type business_connection_id: :obj:`str`
        :param message_ids: A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat. See `deleteMessage <https://core.telegram.org/bots/api#deletemessage>`_ for limitations on which messages can be deleted.
        :type message_ids: :obj:`list` of :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'message_ids': message_ids
        }
        return await super().delete_business_messages(params)


    async def delete_chat_photo(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletechatphoto

        Use this method to delete a chat photo. Photos can't be changed for
        private chats. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().delete_chat_photo(params)


    async def delete_chat_sticker_set(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletechatstickerset

        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat
        for this to work and must have the appropriate administrator rights. Use the field *can_set_sticker_set* optionally
        returned in :meth:`~apitele.Client.get_chat` requests to check if the bot can use this method. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().delete_chat_sticker_set(params)


    async def delete_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deleteforumtopic

        Use this method to delete a forum topic along with all its messages in a forum
        supergroup chat. The bot must be an administrator in the chat for this to work and
        must have the *can_delete_messages* administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_thread_id: Unique identifier for the target message thread of the forum topic.
        :type message_thread_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().delete_forum_topic(params)


    async def delete_message(
        self,
        chat_id: Union[int, str],
        message_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletemessage

        Use this method to delete a message, including service messages, with the following limitations:

        - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted *can_post_messages* permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has *can_delete_messages* permission in a supergroup or a channel, it can delete any message there.

        Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_id: Identifier of the message to delete.
        :type message_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        return await super().delete_message(params)


    async def delete_messages(
        self,
        chat_id: Union[int, str],
        message_ids: list[int]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletemessages

        Use this method to delete multiple messages simultaneously. If some of the
        specified messages can't be found, they are skipped. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_ids: A JSON-serialized list of 1-100 identifiers of messages to delete. See :meth:`~apitele.Client.delete_message` for limitations on which messages can be deleted.
        :type message_ids: :obj:`list` of :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_ids': message_ids
        }
        return await super().delete_messages(params)


    async def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletemycommands

        Use this method to delete the list of the bot's commands for the given scope and user language.
        After deletion, `higher level commands <https://core.telegram.org/bots/api#determining-list-of-commands>`_ will be shown to affected users. Returns :obj:`True` on success.

        :param scope: A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to :obj:`~apitele.types.BotCommandScopeDefault`.
        :type scope: :obj:`~apitele.types.BotCommandScope`, optional
        :param language_code: A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        return await super().delete_my_commands(params)


    async def delete_sticker_from_set(
        self,
        sticker: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletestickerfromset

        Use this method to delete a sticker from a set created by the bot. Returns :obj:`True` on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'sticker': sticker
        }
        return await super().delete_sticker_from_set(params)


    async def delete_sticker_set(
        self,
        name: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletestickerset

        Use this method to delete a sticker set that was created by the bot. Returns :obj:`True` on success.

        :param name: Sticker set name.
        :type name: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'name': name
        }
        return await super().delete_sticker_set(params)


    async def delete_story(
        self,
        business_connection_id: str,
        story_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#deletestory

        Deletes a story previously posted by the bot on behalf of a managed business account.
        Requires the *can_manage_stories* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param story_id: Unique identifier of the story to delete.
        :type story_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'story_id': story_id
        }
        return await super().delete_story(params)


    async def edit_chat_invite_link(
        self,
        chat_id: Union[int, str],
        invite_link: str,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None
    ) -> ChatInviteLink:
        '''
        https://core.telegram.org/bots/api#editchatinvitelink

        Use this method to edit a non-primary invite link created by the bot. The bot
        must be an administrator in the chat for this to work and must have the appropriate
        administrator rights. Returns the edited invite link as a :obj:`~apitele.types.ChatInviteLink` object.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param invite_link: The invite link to edit.
        :type invite_link: :obj:`str`
        :param name: Invite link name; 0-32 characters.
        :type name: :obj:`str`, optional
        :param expire_date: Point in time (Unix timestamp) when the link will expire.
        :type expire_date: :obj:`int`, optional
        :param member_limit: The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.
        :type member_limit: :obj:`int`, optional
        :param creates_join_request: :obj:`True`, if users joining the chat via the link need to be approved by chat administrators. If :obj:`True`, *member_limit* can't be specified.
        :type creates_join_request: :obj:`bool`, optional
        :rtype: :obj:`~apitele.types.ChatInviteLink`
        '''
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link
        }
        if name is not None: params['name'] = name
        if expire_date is not None: params['expire_date'] = expire_date
        if member_limit is not None: params['member_limit'] = member_limit
        if creates_join_request is not None: params['creates_join_request'] = creates_join_request
        result = await super().edit_chat_invite_link(params)
        return ChatInviteLink._dese(result)


    async def edit_chat_subscription_invite_link(
        self,
        chat_id: Union[int, str],
        invite_link: str,
        name: Optional[str] = None
    ) -> ChatInviteLink:
        '''
        https://core.telegram.org/bots/api#editchatsubscriptioninvitelink

        Use this method to edit a subscription invite link created by the bot.
        The bot must have the *can_invite_users* administrator rights.
        Returns the edited invite link as a :obj:`~apitele.types.ChatInviteLink` object.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param invite_link: The invite link to edit.
        :type invite_link: :obj:`str`
        :param name: Invite link name; 0-32 characters.
        :type name: :obj:`str`, optional
        :rtype: :obj:`~apitele.types.ChatInviteLink`
        '''
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link
        }
        if name is not None: params['name'] = name
        result = await super().edit_chat_subscription_invite_link(params)
        return ChatInviteLink._dese(result)


    async def edit_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        name: Optional[str] = None,
        icon_custom_emoji_id: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#editforumtopic

        Use this method to edit name and icon of a topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have *can_manage_topics*
        administrator rights, unless it is the creator of the topic. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_thread_id: Unique identifier for the target message thread of the forum topic.
        :type message_thread_id: :obj:`int`
        :param name: New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept.
        :type name: :obj:`str`, optional
        :param icon_custom_emoji_id: New unique identifier of the custom emoji shown as the topic icon. Use :meth:`~apitele.Client.get_forum_topic_icon_stickers` to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept.
        :type icon_custom_emoji_id: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        if name is not None: params['name'] = name
        if icon_custom_emoji_id is not None: params['icon_custom_emoji_id'] = icon_custom_emoji_id
        return await super().edit_forum_topic(params)


    async def edit_general_forum_topic(
        self,
        chat_id: Union[int, str],
        name: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#editgeneralforumtopic

        Use this method to edit the name of the 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work and must
        have *can_manage_topics* administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param name: New topic name, 1-128 characters.
        :type name: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'name': name
        }
        return await super().edit_general_forum_topic(params)


    async def edit_message_caption(
        self,
        business_connection_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''
        https://core.telegram.org/bots/api#editmessagecaption

        Use this method to edit captions of messages. On success, if the edited message is
        not an inline message, the edited :obj:`~apitele.types.Message` is returned, otherwise :obj:`True` is returned.
        Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.
        
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message to be edited was sent.
        :type business_connection_id: :obj:`str`, optional
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the message to edit.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :param caption: New caption of the message, 0-1024 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the message caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media. Supported only for animation, photo and video messages.
        :type show_caption_above_media: :obj:`bool`, optional
        :param reply_markup: A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message` or :obj:`True`
        '''
        params = {}
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if show_caption_above_media is not None: params['show_caption_above_media'] = show_caption_above_media
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_caption(params)
        return Message._dese(result) if result is not True else True


    async def edit_message_live_location(
        self,
        latitude: float,
        longitude: float,
        business_connection_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        live_period: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''
        https://core.telegram.org/bots/api#editmessagelivelocation

        Use this method to edit live location messages. A location can be edited until its *live_period* expires or editing
        is explicitly disabled by a call to :meth:`~apitele.Client.stop_message_live_location`. On success, if the edited
        message is not an inline message, the edited :obj:`~apitele.types.Message` is returned, otherwise :obj:`True` is returned.

        :param latitude: Latitude of new location.
        :type latitude: :obj:`float`
        :param longitude: Longitude of new location.
        :type longitude: :obj:`float`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message to be edited was sent.
        :type business_connection_id: :obj:`str`, optional
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the message to edit.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :param live_period: New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current *live_period* by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then *live_period* remains unchanged.
        :type live_period: :obj:`int`, optional
        :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500.
        :type horizontal_accuracy: :obj:`float`, optional
        :param heading: Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        :type heading: :obj:`int`, optional
        :param proximity_alert_radius: The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        :type proximity_alert_radius: :obj:`int`, optional
        :param reply_markup: A JSON-serialized object for a new `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message` or :obj:`True`
        '''
        params = {
            'latitude': latitude,
            'longitude': longitude
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if live_period is not None: params['live_period'] = live_period
        if horizontal_accuracy is not None: params['horizontal_accuracy'] = horizontal_accuracy
        if heading is not None: params['heading'] = heading
        if proximity_alert_radius is not None: params['proximity_alert_radius'] = proximity_alert_radius
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_live_location(params)
        return Message._dese(result) if result is not True else True


    async def edit_message_media(
        self,
        media: InputMedia,
        business_connection_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''
        https://core.telegram.org/bots/api#editmessagemedia

        Use this method to edit animation, audio, document, photo, or video messages. If a message is part
        of a message album, then it can be edited only to an audio for audio albums, only to a document for
        document albums and to a photo or a video otherwise. When an inline message is edited, a new file
        can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited
        message is not an inline message, the edited :obj:`~apitele.types.Message` is returned, otherwise :obj:`True` is returned.
        Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.
        
        :param media: A JSON-serialized object for a new media content of the message.
        :type media: :obj:`~apitele.types.InputMedia`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message to be edited was sent.
        :type business_connection_id: :obj:`str`, optional
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the message to edit.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :param reply_markup: A JSON-serialized object for a new `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message` or :obj:`True`
        '''
        params = {
            'media': media
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_media(params)
        return Message._dese(result) if result is not True else True


    async def edit_message_reply_markup(
        self,
        business_connection_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''
        https://core.telegram.org/bots/api#editmessagereplymarkup

        Use this method to edit only the reply markup of messages. On success, if the edited message is not an
        inline message, the edited :obj:`~apitele.types.Message` is returned, otherwise :obj:`True` is returned.
        Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message to be edited was sent.
        :type business_connection_id: :obj:`str`, optional
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the message to edit.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :param reply_markup: A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message` or :obj:`True`
        '''
        params = {}
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_reply_markup(params)
        return Message._dese(result) if result is not True else True


    async def edit_message_text(
        self,
        text: str,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        business_connection_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''
        https://core.telegram.org/bots/api#editmessagetext

        Use this method to edit text and `game <https://core.telegram.org/bots/api#games>`_ messages.
        On success, if the edited message is not an inline message, the edited :obj:`~apitele.types.Message` is returned, otherwise :obj:`True` is returned.
        Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        :param text: New text of the message, 1-4096 characters after entities parsing.
        :type text: :obj:`str`
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the message to edit.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the message text. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param entities: A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*.
        :type entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param link_preview_options: Link preview generation options for the message.
        :type link_preview_options: :obj:`~apitele.types.LinkPreviewOptions`, optional
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message to be edited was sent.
        :type business_connection_id: :obj:`str`, optional
        :param reply_markup: A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message` or :obj:`True`
        '''
        params = {
            'text': text
        }
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if entities is not None: params['entities'] = entities
        if link_preview_options is not None: params['link_preview_options'] = link_preview_options
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_text(params)
        return Message._dese(result) if result is not True else True


    async def edit_story(
        self,
        business_connection_id: str,
        story_id: int,
        content: InputStoryContent,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        areas: Optional[list[StoryArea]] = None
    ) -> Story:
        '''
        https://core.telegram.org/bots/api#editstory

        Edits a story previously posted by the bot on behalf of a managed business account.
        Requires the *can_manage_stories* business bot right. Returns :obj:`~apitele.types.Story` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param story_id: Unique identifier of the story to edit.
        :type story_id: :obj:`int`
        :param content: Content of the story.
        :type content: :obj:`~apitele.types.InputStoryContent`
        :param caption: Caption of the story, 0-2048 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the story caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param areas: A JSON-serialized list of clickable areas to be shown on the story.
        :type areas: :obj:`list` of :obj:`~apitele.types.StoryArea`, optional
        :rtype: :obj:`~apitele.types.Story`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'story_id': story_id,
            'content': content
        }
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if areas is not None: params['areas'] = areas
        result = await super().edit_story(params)
        return Story._dese(result)


    async def edit_user_star_subscription(
        self,
        user_id: int,
        telegram_payment_charge_id: str,
        is_canceled: bool
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#edituserstarsubscription

        Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns :obj:`True` on success.

        :param user_id: Identifier of the user whose subscription will be edited.
        :type user_id: :obj:`int`
        :param telegram_payment_charge_id: Telegram payment identifier for the subscription.
        :type telegram_payment_charge_id: :obj:`str`
        :param is_canceled: Pass :obj:`True` to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass :obj:`False` to allow the user to re-enable a subscription that was previously canceled by the bot.
        :type is_canceled: :obj:`bool`
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'telegram_payment_charge_id': telegram_payment_charge_id,
            'is_canceled': is_canceled
        }
        return await super().edit_user_star_subscription(params)


    async def export_chat_invite_link(
        self,
        chat_id: Union[int, str]
    ) -> str:
        '''
        https://core.telegram.org/bots/api#exportchatinvitelink

        Use this method to generate a new primary invite link for a chat; any previously generated
        primary link is revoked. The bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Returns the new invite link as :obj:`String` on success.

            Note: Each administrator in a chat generates their own invite links. Bots can't use invite links generated by other administrators. If you want
            your bot to work with invite links, it will need to generate its own link using :meth:`~apitele.Client.export_chat_invite_link` or by calling the
            :meth:`~apitele.Client.get_chat` method. If your bot needs to generate a new primary invite link replacing its previous one, use :meth:`~apitele.Client.export_chat_invite_link` again.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`str`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().export_chat_invite_link(params)


    async def forward_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        video_start_timestamp: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#forwardmessage

        Use this method to forward messages of any kind. Service messages and messages with
        protected content can't be forwarded. On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format ``@channelusername``).
        :type from_chat_id: :obj:`int` or :obj:`str`
        :param message_id: Message identifier in the chat specified in *from_chat_id*.
        :type message_id: :obj:`int`
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param video_start_timestamp: New start timestamp for the forwarded video in the message.
        :type video_start_timestamp: :obj:`int`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the forwarded message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if video_start_timestamp is not None: params['video_start_timestamp'] = video_start_timestamp
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        result = await super().forward_message(params)
        return Message._dese(result)


    async def forward_messages(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: list[int],
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None
    ) -> list[MessageId]:
        '''
        https://core.telegram.org/bots/api#forwardmessages

        Use this method to forward multiple messages of any kind. If some of the specified messages can't be found
        or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album
        grouping is kept for forwarded messages. On success, an array of :obj:`~apitele.types.MessageId` of the sent messages is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param from_chat_id: Unique identifier for the chat where the original messages were sent (or channel username in the format ``@channelusername``).
        :type from_chat_id: :obj:`int` or :obj:`str`
        :param message_ids: A JSON-serialized list of 1-100 identifiers of messages in the chat *from_chat_id* to forward. The identifiers must be specified in a strictly increasing order.
        :type message_ids: :obj:`list` of :obj:`int`
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param disable_notification: Sends the messages `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the forwarded messages from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :rtype: :obj:`list` of :obj:`~apitele.types.MessageId`
        '''
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_ids': message_ids
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        result = await super().forward_messages(params)
        return [MessageId._dese(mid) for mid in result]


    async def get_available_gifts(self) -> Gifts:
        '''
        https://core.telegram.org/bots/api#getavailablegifts

        Returns the list of gifts that can be sent by the bot to users and channel chats. Requires no parameters. Returns a :obj:`~apitele.types.Gifts` object.

        :rtype: :obj:`~apitele.types.Gifts`
        '''
        result = await super().get_available_gifts()
        return Gifts._dese(result)


    async def get_business_account_gifts(
        self,
        business_connection_id: str,
        exclude_unsaved: Optional[bool] = None,
        exclude_saved: Optional[bool] = None,
        exclude_unlimited: Optional[bool] = None,
        exclude_limited: Optional[bool] = None,
        exclude_unique: Optional[bool] = None,
        sort_by_price: Optional[bool] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None
    ) -> OwnedGifts:
        '''
        https://core.telegram.org/bots/api#getbusinessaccountgifts

        Returns the gifts received and owned by a managed business account.
        Requires the *can_view_gifts_and_stars* business bot right. Returns :obj:`~apitele.types.OwnedGifts` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param exclude_unsaved: Pass :obj:`True` to exclude gifts that aren't saved to the account's profile page.
        :type exclude_unsaved: :obj:`bool`, optional
        :param exclude_saved: Pass :obj:`True` to exclude gifts that are saved to the account's profile page.
        :type exclude_saved: :obj:`bool`, optional
        :param exclude_unlimited: Pass :obj:`True` to exclude gifts that can be purchased an unlimited number of times.
        :type exclude_unlimited: :obj:`bool`, optional
        :param exclude_limited: Pass :obj:`True` to exclude gifts that can be purchased a limited number of times.
        :type exclude_limited: :obj:`bool`, optional
        :param exclude_unique: Pass :obj:`True` to exclude unique gifts.
        :type exclude_unique: :obj:`bool`, optional
        :param sort_by_price: Pass :obj:`True` to sort results by gift price instead of send date. Sorting is applied before pagination.
        :type sort_by_price: :obj:`bool`, optional
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results.
        :type offset: :obj:`str`, optional
        :param limit: The maximum number of gifts to be returned; 1-100. Defaults to 100.
        :type limit: :obj:`int`, optional
        '''
        params = {
            'business_connection_id': business_connection_id
        }
        if exclude_unsaved is not None: params['exclude_unsaved'] = exclude_unsaved
        if exclude_saved is not None: params['exclude_saved'] = exclude_saved
        if exclude_unlimited is not None: params['exclude_unlimited'] = exclude_unlimited
        if exclude_limited is not None: params['exclude_limited'] = exclude_limited
        if exclude_unique is not None: params['exclude_unique'] = exclude_unique
        if sort_by_price is not None: params['sort_by_price'] = sort_by_price
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        result = await super().get_business_account_gifts(params)
        return OwnedGifts._dese(result)


    async def get_business_account_star_balance(
        self,
        business_connection_id: str
    ) -> StarAmount:
        '''
        https://core.telegram.org/bots/api#getbusinessaccountstarbalance

        Returns the amount of Telegram Stars owned by a managed business account.
        Requires the *can_view_gifts_and_stars* business bot right. Returns :obj:`~apitele.types.StarAmount` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :rtype: :obj:`~apitele.types.StarAmount`
        '''
        params = {
            'business_connection_id': business_connection_id
        }
        result = await super().get_business_account_star_balance(params)
        return StarAmount._dese(result)


    async def get_business_connection(
        self,
        business_connection_id: str
    ) -> BusinessConnection:
        '''
        https://core.telegram.org/bots/api#getbusinessconnection

        Use this method to get information about the connection of the bot with a business account.
        Returns a :obj:`~apitele.types.BusinessConnection` object on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :rtype: :obj:`~apitele.types.BusinessConnection`
        '''
        params = {
            'business_connection_id': business_connection_id
        }
        result = await super().get_business_connection(params)
        return BusinessConnection._dese(result)


    async def get_chat(
        self,
        chat_id: Union[int, str]
    ) -> ChatFullInfo:
        '''
        https://core.telegram.org/bots/api#getchat

        Use this method to get up-to-date information about the chat.
        Returns a :obj:`~apitele.types.ChatFullInfo` object on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`~apitele.types.ChatFullInfo`
        '''
        params = {
            'chat_id': chat_id
        }
        result = await super().get_chat(params)
        return ChatFullInfo._dese(result)


    async def get_chat_administrators(
        self,
        chat_id: Union[int, str]
    ) -> list[ChatMember]:
        '''
        https://core.telegram.org/bots/api#getchatadministrators

        Use this method to get a list of administrators in a chat, which aren't bots.
        Returns an Array of :obj:`~apitele.types.ChatMember` objects.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`list` of :obj:`~apitele.types.ChatMember`
        '''
        params = {
            'chat_id': chat_id
        }
        result = await super().get_chat_administrators(params)
        return [_dese_chat_member(chat_member) for chat_member in result]


    async def get_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> ChatMember:
        '''
        https://core.telegram.org/bots/api#getchatmember

        Use this method to get information about a member of a chat. The method is only guaranteed to work for other
        users if the bot is an administrator in the chat. Returns a :obj:`~apitele.types.ChatMember` object on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :rtype: :obj:`~apitele.types.ChatMember`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        result = await super().get_chat_member(params)
        return _dese_chat_member(result)


    async def get_chat_member_count(
        self,
        chat_id: Union[int, str]
    ) -> int:
        '''
        https://core.telegram.org/bots/api#getchatmembercount

        Use this method to get the number of members in a chat. Returns :obj:`Int` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`int`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().get_chat_member_count(params)


    async def get_chat_menu_button(
        self,
        chat_id: Optional[int] = None
    ) -> MenuButton:
        '''
        https://core.telegram.org/bots/api#getchatmenubutton

        Use this method to get the current value of the bot's menu button in a private
        chat, or the default menu button. Returns :obj:`~apitele.types.MenuButton` on success.

        :param chat_id: Unique identifier for the target private chat. If not specified, default bot's menu button will be returned.
        :type chat_id: :obj:`int`, optional
        :rtype: :obj:`~apitele.types.MenuButton`
        '''
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        result = await super().get_chat_menu_button(params)
        return _dese_menu_button(result)


    async def get_custom_emoji_stickers(
        self,
        custom_emoji_ids: list[str]
    ) -> list[Sticker]:
        '''
        https://core.telegram.org/bots/api#getcustomemojistickers

        Use this method to get information about custom emoji stickers by their
        identifiers. Returns an Array of :obj:`~apitele.types.Sticker` objects.

        :param custom_emoji_ids: A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.
        :type custom_emoji_ids: :obj:`list` of :obj:`str`
        :rtype: :obj:`list` of :obj:`~apitele.types.Sticker`
        '''
        params = {
            'custom_emoji_ids': custom_emoji_ids
        }
        result = await super().get_custom_emoji_stickers(params)
        return [Sticker._dese(sticker) for sticker in result]


    async def get_file(
        self,
        file_id: str
    ) -> File:
        '''
        https://core.telegram.org/bots/api#getfile

        Use this method to get basic information about a file and prepare it for
        downloading. For the moment, bots can download files of up to 20MB in size.
        On success, a :obj:`~apitele.types.File` object is returned. The file can then be
        downloaded via the link ``https://api.telegram.org/file/bot<token>/<file_path>``, where
        ``<file_path>`` is taken from the response. It is guaranteed that the link will be valid for at least 1 hour.
        When the link expires, a new one can be requested by calling :meth:`~apitele.Client.get_file` again.

            Note: This function may not preserve the original file name and MIME type.
            You should save the file's MIME type and name (if available) when the File object is received.

        :param file_id: File identifier to get information about.
        :type file_id: :obj:`str`
        :rtype: :obj:`~apitele.types.File`
        '''
        params = {
            'file_id': file_id
        }
        result = await super().get_file(params)
        return File._dese(result)


    async def get_forum_topic_icon_stickers(self) -> list[Sticker]:
        '''
        https://core.telegram.org/bots/api#getforumtopiciconstickers

        Use this method to get custom emoji stickers, which can be used as a forum topic icon by
        any user. Requires no parameters. Returns an Array of :obj:`~apitele.types.Sticker` objects.

        :rtype: :obj:`list` of :obj:`~apitele.types.Sticker`
        '''
        result = await super().get_forum_topic_icon_stickers()
        return [Sticker._dese(sticker) for sticker in result]


    async def get_game_high_scores(
        self,
        user_id: int,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> list[GameHighScore]:
        '''
        https://core.telegram.org/bots/api#getgamehighscores

        Use this method to get data for high score tables. Will return the score of the specified user and
        several of their neighbors in a game. Returns an Array of :obj:`~apitele.types.GameHighScore` objects.

            This method will currently return scores for the target user, plus two of their closest neighbors on each side.
            Will also return the top three users if the user and their neighbors are not among them. Please note that this behavior is subject to change.

        :param user_id: Target user id.
        :type user_id: :obj:`int`
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat.
        :type chat_id: :obj:`int`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the sent message.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :rtype: :obj:`list` of :obj:`~apitele.types.GameHighScore`
        '''
        params = {
            'user_id': user_id
        }
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        result = await super().get_game_high_scores(params)
        return [GameHighScore._dese(score) for score in result]


    async def get_me(self) -> User:
        '''
        https://core.telegram.org/bots/api#getme

        A simple method for testing your bot's authentication token. Requires no parameters.
        Returns basic information about the bot in form of a :obj:`~apitele.types.User` object.

        :rtype: :obj:`~apitele.types.User`
        '''
        if isinstance(self.user, User):
            return self.user
        result = await super().get_me()
        self._user = User._dese(result)
        return self.user


    async def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> list[BotCommand]:
        '''
        https://core.telegram.org/bots/api#getmycommands

        Use this method to get the current list of the bot's commands for the given scope and user language.
        Returns an Array of :obj:`~apitele.types.BotCommand` objects. If commands aren't set, an empty list is returned.

        :param scope: 
        :type scope: :obj:`~apitele.types.BotCommandScope`, optional
        :param language_code: 
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`list` of :obj:`~apitele.types.BotCommand`
        '''
        params = {}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_commands(params)
        return [BotCommand._dese(bot_command) for bot_command in result]


    async def get_my_default_administrator_rights(
        self,
        for_channels: Optional[bool] = None
    ) -> ChatAdministratorRights:
        '''
        https://core.telegram.org/bots/api#getmydefaultadministratorrights

        Use this method to get the current default administrator rights of the bot.
        Returns :obj:`~apitele.types.ChatAdministratorRights` on success.

        :param for_channels: Pass :obj:`True` to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned.
        :type for_channels: :obj:`bool`, optional
        :rtype: :obj:`~apitele.types.ChatAdministratorRights`
        '''
        params = {}
        if for_channels is not None: params['for_channels'] = for_channels
        result = await super().get_my_default_administrator_rights(params)
        return ChatAdministratorRights._dese(result)


    async def get_my_description(
        self,
        language_code: Optional[str] = None
    ) -> BotDescription:
        '''
        https://core.telegram.org/bots/api#getmydescription

        Use this method to get the current bot description for the given
        user language. Returns :obj:`~apitele.types.BotDescription` on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`~apitele.types.BotDescription`
        '''
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_description(params)
        return BotDescription._dese(result)


    async def get_my_name(
        self,
        language_code: Optional[str] = None
    ) -> BotName:
        '''
        https://core.telegram.org/bots/api#getmyname

        Use this method to get the current bot name for the given user language.
        Returns :obj:`~apitele.types.BotName` on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`~apitele.types.BotName`
        '''
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_name(params)
        return BotName._dese(result)


    async def get_my_short_description(
        self,
        language_code: Optional[str] = None
    ) -> BotShortDescription:
        '''
        https://core.telegram.org/bots/api#getmyshortdescription

        Use this method to get the current bot short description for the given
        user language. Returns :obj:`~apitele.types.BotShortDescription` on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`~apitele.types.BotShortDescription`
        '''
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_short_description(params)
        return BotShortDescription._dese(result)


    async def get_star_transactions(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None
    ) -> StarTransactions:
        '''
        https://core.telegram.org/bots/api#getstartransactions

        Returns the bot's Telegram Star transactions in chronological order.
        On success, returns a :obj:`~apitele.types.StarTransactions` object.

        :param offset: Number of transactions to skip in the response.
        :type offset: :obj:`int`, optional
        :param limit: The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to :obj:`100`.
        :type limit: :obj:`int`, optional
        :rtype: :obj:`~apitele.types.StarTransactions`
        '''
        params = {}
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        result = await super().get_star_transactions(params)
        return StarTransactions._dese(result)


    async def get_sticker_set(
        self,
        name: str
    ) -> StickerSet:
        '''
        https://core.telegram.org/bots/api#getstickerset

        Use this method to get a sticker set.
        On success, a :obj:`~apitele.types.StickerSet` object is returned.

        :param name: Name of the sticker set.
        :type name: :obj:`str`
        :rtype: :obj:`~apitele.types.StickerSet`
        '''
        params = {
            'name': name
        }
        result = await super().get_sticker_set(params)
        return StickerSet._dese(result)


    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[list[str]] = None
    ) -> list[Update]:
        '''
        https://core.telegram.org/bots/api#getupdates

        Use this method to receive incoming updates using long polling (`wiki <https://en.wikipedia.org/wiki/Push_technology#Long_polling>`_).
        Returns an Array of :obj:`~apitele.types.Update` objects.

            | **Notes**
            | **1.** This method will not work if an outgoing webhook is set up.
            | **2.** In order to avoid getting duplicate updates, recalculate *offset* after each server response.

        :param offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as :meth:`~apitele.Client.get_updates` is called with an *offset* higher than its *update_id*. The negative offset can be specified to retrieve updates starting from -*offset* update from the end of the updates queue. All previous updates will be forgotten.
        :type offset: :obj:`int`, optional
        :param limit: Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to :obj:`100`.
        :type limit: :obj:`int`, optional
        :param timeout: Timeout in seconds for long polling. Defaults to :obj:`0`, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
        :type timeout: :obj:`int`, optional
        :param allowed_updates:
            A JSON-serialized list of the update types you want your bot to receive. For example, specify ``["message", "edited_channel_post", "callback_query"]`` to only receive updates of these types. See :obj:`~apitele.types.Update` for a complete list of available update types. Specify an empty list to receive all update types except *chat_member*, *message_reaction*, and *message_reaction_count* (default). If not specified, the previous setting will be used.

            Please note that this parameter doesn't affect updates created before the call to the :meth:`~apitele.Client.get_updates`, so unwanted updates may be received for a short period of time.
        :type allowed_updates: :obj:`list` of :obj:`str`, optional
        :rtype: :obj:`list` of :obj:`~apitele.types.Update`
        '''
        params = {}
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        if timeout is not None: params['timeout'] = timeout
        if allowed_updates is not None: params['allowed_updates'] = allowed_updates
        result = await super().get_updates(params)
        return [Update._dese(update) for update in result]


    async def get_user_chat_boosts(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> UserChatBoosts:
        '''
        https://core.telegram.org/bots/api#getuserchatboosts

        Use this method to get the list of boosts added to a chat by a user. Requires
        administrator rights in the chat. Returns a :obj:`~apitele.types.UserChatBoosts` object.

        :param chat_id: Unique identifier for the chat or username of the channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :rtype: :obj:`~apitele.types.UserChatBoosts`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        result = await super().get_user_chat_boosts(params)
        return UserChatBoosts._dese(result)


    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None
    ) -> UserProfilePhotos:
        '''
        https://core.telegram.org/bots/api#getuserprofilephotos

        Use this method to get a list of profile pictures for a user.
        Returns a :obj:`~apitele.types.UserProfilePhotos` object.

        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :param offset: Sequential number of the first photo to be returned. By default, all photos are returned.
        :type offset: :obj:`int`, optional
        :param limit: Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to :obj:`100`.
        :type limit: :obj:`int`, optional
        :rtype: :obj:`~apitele.types.UserProfilePhotos`
        '''
        params = {
            'user_id': user_id
        }
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        result = await super().get_user_profile_photos(params)
        return UserProfilePhotos._dese(result)


    async def gift_premium_subscription(
        self,
        user_id: int,
        month_count: int,
        star_count: int,
        text: Optional[str] = None,
        text_parse_mode: Optional[str] = None,
        text_entities: Optional[list[MessageEntity]] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#giftpremiumsubscription

        Gifts a Telegram Premium subscription to the given user. Returns :obj:`True` on success.

        :param user_id: Unique identifier of the target user who will receive a Telegram Premium subscription.
        :type user_id: :obj:`int`
        :param month_count: Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12.
        :type month_count: :obj:`int`
        :param star_count: Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months.
        :type star_count: :obj:`int`
        :param text: Text that will be shown along with the service message about the subscription; 0-128 characters.
        :type text: :obj:`str`, optional
        :param text_parse_mode: Mode for parsing entities in the text. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
        :type text_parse_mode: :obj:`str`, optional
        :param text_entities: A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text_parse_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
        :type text_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'month_count': month_count,
            'star_count': star_count
        }
        if text is not None: params['text'] = text
        if text_parse_mode is not None: params['text_parse_mode'] = text_parse_mode
        if text_entities is not None: params['text_entities'] = text_entities
        return await super().gift_premium_subscription(params)


    async def hide_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#hidegeneralforumtopic

        Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an
        administrator in the chat for this to work and must have the *can_manage_topics* administrator
        rights. The topic will be automatically closed if it was open. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().hide_general_forum_topic(params)


    async def leave_chat(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#leavechat

        Use this method for your bot to leave a group, supergroup or channel.
        Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().leave_chat(params)


    async def log_out(self) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#logout

        Use this method to log out from the cloud Bot API server before launching the bot locally.
        You **must** log out the bot before running it locally, otherwise there is no guarantee that the
        bot will receive updates. After a successful call, you can immediately log in on a local server, but will
        not be able to log in back to the cloud Bot API server for 10 minutes. Returns :obj:`True` on success. Requires no parameters.

        :rtype: :obj:`True`
        '''
        return await super().log_out()


    async def pin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: Optional[bool] = None,
        business_connection_id: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#pinchatmessage

        Use this method to add a message to the list of pinned messages in a chat. If the chat is not a
        private chat, the bot must be an administrator in the chat for this to work and must have the *can_pin_messages*
        administrator right in a supergroup or *can_edit_messages* administrator right in a channel. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_id: Identifier of a message to pin.
        :type message_id: :obj:`int`
        :param disable_notification: Pass :obj:`True` if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.
        :type disable_notification: :obj:`bool`, optional
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be pinned.
        :type business_connection_id: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        return await super().pin_chat_message(params)


    async def post_story(
        self,
        business_connection_id: str,
        content: InputStoryContent,
        active_period: int,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        areas: Optional[list[StoryArea]] = None,
        post_to_chat_page: Optional[bool] = None,
        protect_content: Optional[bool] = None
    ) -> Story:
        '''
        https://core.telegram.org/bots/api#poststory

        Posts a story on behalf of a managed business account.
        Requires the *can_manage_stories* business bot right. Returns :obj:`~apitele.types.Story` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param content: Content of the story.
        :type content: :obj:`~apitele.types.InputStoryContent`
        :param active_period: Period after which the story is moved to the archive, in seconds; must be one of ``6 * 3600``, ``12 * 3600``, ``86400``, or ``2 * 86400``.
        :type active_period: :obj:`int`
        :param caption: Caption of the story, 0-2048 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the story caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param areas: A JSON-serialized list of clickable areas to be shown on the story.
        :type areas: :obj:`list` of :obj:`~apitele.types.StoryArea`, optional
        :param post_to_chat_page: Pass :obj:`True` to keep the story accessible after it expires.
        :type post_to_chat_page: :obj:`bool`, optional
        :param protect_content: Pass :obj:`True` if the content of the story must be protected from forwarding and screenshotting.
        :type protect_content: :obj:`bool`, optional
        :rtype: :obj:`~apitele.types.Story`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'content': content,
            'active_period': active_period
        }
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if areas is not None: params['areas'] = areas
        if post_to_chat_page is not None: params['post_to_chat_page'] = post_to_chat_page
        if protect_content is not None: params['protect_content'] = protect_content
        result = await super().post_story(params)
        return Story._dese(result)


    async def promote_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_post_stories: Optional[bool] = None,
        can_edit_stories: Optional[bool] = None,
        can_delete_stories: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#promotechatmember

        Use this method to promote or demote a user in a supergroup or a channel. The bot must be
        an administrator in the chat for this to work and must have the appropriate administrator
        rights. Pass :obj:`False` for all boolean parameters to demote a user. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :param is_anonymous: Pass :obj:`True` if the administrator's presence in the chat is hidden.
        :type is_anonymous: :obj:`bool`, optional
        :param can_manage_chat: Pass :obj:`True` if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
        :type can_manage_chat: :obj:`bool`, optional
        :param can_delete_messages: Pass :obj:`True` if the administrator can delete messages of other users.
        :type can_delete_messages: :obj:`bool`, optional
        :param can_manage_video_chats: Pass :obj:`True` if the administrator can manage video chats.
        :type can_manage_video_chats: :obj:`bool`, optional
        :param can_restrict_members: Pass :obj:`True` if the administrator can restrict, ban or unban chat members, or access supergroup statistics.
        :type can_restrict_members: :obj:`bool`, optional
        :param can_promote_members: Pass :obj:`True` if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him).
        :type can_promote_members: :obj:`bool`, optional
        :param can_change_info: Pass :obj:`True` if the administrator can change chat title, photo and other settings.
        :type can_change_info: :obj:`bool`, optional
        :param can_invite_users: Pass :obj:`True` if the administrator can invite new users to the chat.
        :type can_invite_users: :obj:`bool`, optional
        :param can_post_stories: Pass :obj:`True` if the administrator can post stories to the chat.
        :type can_post_stories: :obj:`bool`, optional
        :param can_edit_stories: Pass :obj:`True` if the administrator can edit stories posted by other users.
        :type can_edit_stories: :obj:`bool`, optional
        :param can_delete_stories: Pass :obj:`True` if the administrator can delete stories posted by other users.
        :type can_delete_stories: :obj:`bool`, optional
        :param can_post_messages: Pass :obj:`True` if the administrator can post messages in the channel, or access channel statistics; for channels only.
        :type can_post_messages: :obj:`bool`, optional
        :param can_edit_messages: Pass :obj:`True` if the administrator can edit messages of other users and can pin messages; for channels only.
        :type can_edit_messages: :obj:`bool`, optional
        :param can_pin_messages: Pass :obj:`True` if the administrator can pin messages; for supergroups only.
        :type can_pin_messages: :obj:`bool`, optional
        :param can_manage_topics: Pass :obj:`True` if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only.
        :type can_manage_topics: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        if is_anonymous is not None: params['is_anonymous'] = is_anonymous
        if can_manage_chat is not None: params['can_manage_chat'] = can_manage_chat
        if can_delete_messages is not None: params['can_delete_messages'] = can_delete_messages
        if can_manage_video_chats is not None: params['can_manage_video_chats'] = can_manage_video_chats
        if can_restrict_members is not None: params['can_restrict_members'] = can_restrict_members
        if can_promote_members is not None: params['can_promote_members'] = can_promote_members
        if can_change_info is not None: params['can_change_info'] = can_change_info
        if can_invite_users is not None: params['can_invite_users'] = can_invite_users
        if can_post_stories is not None: params['can_post_stories'] = can_post_stories
        if can_edit_stories is not None: params['can_edit_stories'] = can_edit_stories
        if can_delete_stories is not None: params['can_delete_stories'] = can_delete_stories
        if can_post_messages is not None: params['can_post_messages'] = can_post_messages
        if can_edit_messages is not None: params['can_edit_messages'] = can_edit_messages
        if can_pin_messages is not None: params['can_pin_messages'] = can_pin_messages
        if can_manage_topics is not None: params['can_manage_topics'] = can_manage_topics
        return await super().promote_chat_member(params)


    async def read_business_message(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#readbusinessmessage

        Marks incoming message as read on behalf of a business account. Requires the *can_read_messages* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection on behalf of which to read the message.
        :type business_connection_id: :obj:`str`
        :param chat_id: Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours.
        :type chat_id: :obj:`int`
        :param message_id: Unique identifier of the message to mark as read.
        :type message_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id
        }
        return await super().read_business_message(params)


    async def refund_star_payment(
        self,
        user_id: int,
        telegram_payment_charge_id: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#refundstarpayment

        Refunds a successful payment in `Telegram Stars <https://t.me/BotNews/90>`_. Returns :obj:`True` on success.

        :param user_id: Identifier of the user whose payment will be refunded.
        :type user_id: :obj:`int`
        :param telegram_payment_charge_id: Telegram payment identifier.
        :type telegram_payment_charge_id: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'telegram_payment_charge_id': telegram_payment_charge_id
        }
        return await super().refund_star_payment(params)


    async def remove_business_account_profile_photo(
        self,
        business_connection_id: str,
        is_public: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#removebusinessaccountprofilephoto

        Removes the current profile photo of a managed business account. Requires the *can_edit_profile_photo* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param is_public: Pass :obj:`True` to remove the public photo, which is visible even if the main photo is hidden by the business account's privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo.
        :type is_public: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id
        }
        if is_public is not None: params['is_public'] = is_public
        return await super().remove_business_account_profile_photo(params)


    async def remove_chat_verification(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#removechatverification

        Removes verification from a chat that is currently verified `on behalf of the organization <https://telegram.org/verify#third-party-verification>`_ represented by the bot. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().remove_chat_verification(params)


    async def remove_user_verification(
        self,
        user_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#removeuserverification

        Removes verification from a user who is currently verified `on behalf of the organization <https://telegram.org/verify#third-party-verification>`_ represented by the bot. Returns :obj:`True` on success.

        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id
        }
        return await super().remove_user_verification(params)


    async def reopen_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#reopenforumtopic

        Use this method to reopen a closed topic in a forum supergroup chat. The bot must
        be an administrator in the chat for this to work and must have the *can_manage_topics*
        administrator rights, unless it is the creator of the topic. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_thread_id: Unique identifier for the target message thread of the forum topic.
        :type message_thread_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().reopen_forum_topic(params)


    async def reopen_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#reopengeneralforumtopic

        Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the *can_manage_topics* administrator
        rights. The topic will be automatically unhidden if it was hidden. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().reopen_general_forum_topic(params)


    async def replace_sticker_in_set(
        self,
        user_id: int,
        name: str,
        old_sticker: str,
        sticker: InputSticker,
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#replacestickerinset

        Use this method to replace an existing sticker in a sticker set with a new one.
        The method is equivalent to calling :meth:`~apitele.Client.delete_sticker_from_set`,
        then :meth:`~apitele.Client.add_sticker_to_set`, then :meth:`~apitele.Client.set_sticker_position_in_set`.
        Returns :obj:`True` on success.

        :param user_id: User identifier of the sticker set owner.
        :type user_id: :obj:`int`
        :param name: Sticker set name.
        :type name: :obj:`str`
        :param old_sticker: File identifier of the replaced sticker.
        :type old_sticker: :obj:`str`
        :param sticker: A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.
        :type sticker: :obj:`~apitele.types.InputSticker`
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'name': name,
            'old_sticker': old_sticker,
            'sticker': sticker
        }
        return await super().replace_sticker_in_set(params)


    async def restrict_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None,
        until_date: Optional[int] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#restrictchatmember

        Use this method to restrict a user in a supergroup. The bot must be an administrator in
        the supergroup for this to work and must have the appropriate administrator rights. Pass
        :obj:`True` for all permissions to lift restrictions from a user. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :param permissions: A JSON-serialized object for new user permissions.
        :type permissions: :obj:`~apitele.types.ChatPermissions`
        :param use_independent_chat_permissions: Pass :obj:`True` if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission.
        :type use_independent_chat_permissions: :obj:`bool`, optional
        :param until_date: Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever.
        :type until_date: :obj:`int`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'permissions': permissions
        }
        if use_independent_chat_permissions is not None: params['use_independent_chat_permissions'] = use_independent_chat_permissions
        if until_date is not None: params['until_date'] = until_date
        return await super().restrict_chat_member(params)


    async def revoke_chat_invite_link(
        self,
        chat_id: Union[int, str],
        invite_link: str
    ) -> ChatInviteLink:
        '''
        https://core.telegram.org/bots/api#revokechatinvitelink

        Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new
        link is automatically generated. The bot must be an administrator in the chat for this to work and must have
        the appropriate administrator rights. Returns the revoked invite link as :obj:`~apitele.types.ChatInviteLink` object.

        :param chat_id: Unique identifier of the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param invite_link: The invite link to revoke.
        :type invite_link: :obj:`str`
        :rtype: :obj:`~apitele.types.ChatInviteLink`
        '''
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link
        }
        result = await super().revoke_chat_invite_link(params)
        return ChatInviteLink._dese(result)


    async def save_prepared_inline_message(
        self,
        user_id: int,
        result: InlineQueryResult,
        allow_user_chats: Optional[bool] = None,
        allow_bot_chats: Optional[bool] = None,
        allow_group_chats: Optional[bool] = None,
        allow_channel_chats: Optional[bool] = None
    ) -> PreparedInlineMessage:
        '''
        https://core.telegram.org/bots/api#savepreparedinlinemessage

        Stores a message that can be sent by a user of a Mini App. Returns a :obj:`~apitele.types.PreparedInlineMessage` object.

        :param user_id: Unique identifier of the target user that can use the prepared message.
        :type user_id: :obj:`int`
        :param result: A JSON-serialized object describing the message to be sent.
        :type result: :obj:`~apitele.types.InlineQueryResult`
        :param allow_user_chats: Pass :obj:`True` if the message can be sent to private chats with users.
        :type allow_user_chats: :obj:`bool`, optional
        :param allow_bot_chats: Pass :obj:`True` if the message can be sent to private chats with bots.
        :type allow_bot_chats: :obj:`bool`, optional
        :param allow_group_chats: Pass :obj:`True` if the message can be sent to group and supergroup chats.
        :type allow_group_chats: :obj:`bool`, optional
        :param allow_channel_chats: Pass :obj:`True` if the message can be sent to channel chats.
        :type allow_channel_chats: :obj:`bool`, optional
        :rtype: :obj:`~apitele.types.PreparedInlineMessage`
        '''
        params = {
            'user_id': user_id,
            'result': result
        }
        if allow_user_chats is not None: params['allow_user_chats'] = allow_user_chats
        if allow_bot_chats is not None: params['allow_bot_chats'] = allow_bot_chats
        if allow_group_chats is not None: params['allow_group_chats'] = allow_group_chats
        if allow_channel_chats is not None: params['allow_channel_chats'] = allow_channel_chats
        result = await super().save_prepared_inline_message(params)
        return PreparedInlineMessage._dese(result)


    async def send_animation(
        self,
        chat_id: Union[int, str],
        animation: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendanimation

        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound).
        On success, the sent :obj:`~apitele.types.Message` is returned. Bots can currently
        send animation files of up to 50 MB in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param animation: Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type animation: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param duration: Duration of sent animation in seconds.
        :type duration: :obj:`int`, optional
        :param width: Animation width.
        :type width: :obj:`int`, optional
        :param height: Animation height.
        :type height: :obj:`int`, optional
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
        :param caption: Animation caption (may also be used when resending animation by *file_id*), 0-1024 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the animation caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
        :type show_caption_above_media: :obj:`bool`, optional
        :param has_spoiler: Pass :obj:`True` if the animation needs to be covered with a spoiler animation.
        :type has_spoiler: :obj:`bool`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'animation': animation
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if show_caption_above_media is not None: params['show_caption_above_media'] = show_caption_above_media
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_animation(params)
        return Message._dese(result)


    async def send_audio(
        self,
        chat_id: Union[int, str],
        audio: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendaudio

        Use this method to send audio files, if you want Telegram clients to display them in the music
        player. Your audio must be in the .MP3 or .M4A format. On success, the sent :obj:`~apitele.types.Message`
        is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the
        future. For sending voice messages, use the :meth:`~apitele.Client.send_voice` method instead.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type audio: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param caption: Audio caption, 0-1024 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the audio caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param duration: Duration of the audio in seconds.
        :type duration: :obj:`int`, optional
        :param performer: Performer.
        :type performer: :obj:`str`, optional
        :param title: Track name.
        :type title: :obj:`str`, optional
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'audio': audio
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if duration is not None: params['duration'] = duration
        if performer is not None: params['performer'] = performer
        if title is not None: params['title'] = title
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_audio(params)
        return Message._dese(result)


    async def send_chat_action(
        self,
        chat_id: Union[int, str],
        action: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#sendchataction

        Use this method when you need to tell the user that something is happening on
        the bot's side. The status is set for 5 seconds or less (when a message arrives
        from your bot, Telegram clients clear its typing status). Returns :obj:`True` on success.

            Example: The `ImageBot <https://t.me/imagebot>`_ needs some time to process a request
            and upload the image. Instead of sending a text message along the lines of “Retrieving
            image, please wait…”, the bot may use :meth:`~apitele.Client.send_chat_action` with
            *action = upload_photo*. The user will see a “sending photo” status for the bot.

        We only recommend using this method when a response from the bot will take a **noticeable** amount of time to arrive.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param action: Type of action to broadcast. Choose one, depending on what the user is about to receive: *typing* for :obj:`text messages <apitele.Client.send_message>`, *upload_photo* for :obj:`photos <apitele.Client.send_photo>`, *record_video* or *upload_video* for :obj:`videos <apitele.Client.send_video>`, *record_voice* or *upload_voice* for :obj:`voice notes <apitele.Client.send_voice>`, *upload_document* for :obj:`general files <apitele.Client.send_document>`, *choose_sticker* for :obj:`stickers <apitele.Client.send_sticker>`, *find_location* for :obj:`location data <apitele.Client.send_location>`, *record_video_note* or *upload_video_note* for :obj:`video notes <apitele.Client.send_video_note>`.
        :type action: :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the action will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread; for supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'action': action
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        return await super().send_chat_action(params)


    async def send_contact(
        self,
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendcontact

        Use this method to send phone contacts.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param phone_number: Contact's phone number.
        :type phone_number: :obj:`str`
        :param first_name: Contact's first name.
        :type first_name: :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param last_name: Contact's last name.
        :type last_name: :obj:`str`, optional
        :param vcard: Additional data about the contact in the form of a `vCard <https://en.wikipedia.org/wiki/VCard>`_, 0-2048 bytes.
        :type vcard: :obj:`str`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if last_name is not None: params['last_name'] = last_name
        if vcard is not None: params['vcard'] = vcard
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_contact(params)
        return Message._dese(result)


    async def send_dice(
        self,
        chat_id: Union[int, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#senddice

        Use this method to send an animated emoji that will display a random
        value. On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param emoji: Emoji on which the dice throw animation is based. Currently, must be one of “🎲”, “🎯”, “🏀”, “⚽”, “🎳”, or “🎰”. Dice can have values 1-6 for “🎲”, “🎯” and “🎳”, values 1-5 for “🏀” and “⚽”, and values 1-64 for “🎰”. Defaults to “🎲”.
        :type emoji: :obj:`str`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if emoji is not None: params['emoji'] = emoji
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_dice(params)
        return Message._dese(result)


    async def send_document(
        self,
        chat_id: Union[int, str],
        document: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#senddocument

        Use this method to send general files.
        On success, the sent :obj:`~apitele.types.Message` is returned.
        Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type document: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
        :param caption: Document caption (may also be used when resending documents by *file_id*), 0-1024 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the document caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param disable_content_type_detection: Disables automatic server-side content type detection for files uploaded using multipart/form-data.
        :type disable_content_type_detection: :obj:`bool`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'document': document
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if disable_content_type_detection is not None: params['disable_content_type_detection'] = disable_content_type_detection
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_document(params)
        return Message._dese(result)


    async def send_game(
        self,
        chat_id: int,
        game_short_name: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendgame

        Use this method to send a game.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat.
        :type chat_id: :obj:`int`
        :param game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via `@BotFather <https://t.me/botfather>`_.
        :type game_short_name: :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'game_short_name': game_short_name
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_game(params)
        return Message._dese(result)


    async def send_gift(
        self,
        gift_id: str,
        user_id: Optional[int] = None,
        chat_id: Optional[Union[int, str]] = None,
        pay_for_upgrade: Optional[bool] = None,
        text: Optional[str] = None,
        text_parse_mode: Optional[str] = None,
        text_entities: Optional[list[MessageEntity]] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#sendgift

        Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns :obj:`True` on success.

        :param gift_id: Identifier of the gift.
        :type gift_id: :obj:`str`
        :param user_id: Required if *chat_id* is not specified. Unique identifier of the target user who will receive the gift.
        :type user_id: :obj:`int`, optional
        :param chat_id: Required if *user_id* is not specified. Unique identifier for the chat or username of the channel (in the format ``@channelusername``) that will receive the gift.
        :type chat_id: :obj:`int` or :obj:`str`, optional
        :param pay_for_upgrade: Pass :obj:`True` to pay for the gift upgrade from the bot's balance, thereby making the upgrade free for the receiver.
        :type pay_for_upgrade: :obj:`bool`, optional
        :param text: Text that will be shown along with the gift; 0-128 characters.
        :type text: :obj:`str`, optional
        :param text_parse_mode: Mode for parsing entities in the text. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
        :type text_parse_mode: :obj:`str`, optional
        :param text_entities: A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text_parse_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
        :type text_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'gift_id': gift_id
        }
        if user_id is not None: params['user_id'] = user_id
        if chat_id is not None: params['chat_id'] = chat_id
        if pay_for_upgrade is not None: params['pay_for_upgrade'] = pay_for_upgrade
        if text is not None: params['text'] = text
        if text_parse_mode is not None: params['text_parse_mode'] = text_parse_mode
        if text_entities is not None: params['text_entities'] = text_entities
        return await super().send_gift(params)


    async def send_invoice(
        self,
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: list[LabeledPrice],
        message_thread_id: Optional[int] = None,
        provider_token: Optional[str] = None,
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[list[int]] = None,
        start_parameter: Optional[str] = None,
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
        is_flexible: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendinvoice

        Use this method to send invoices.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param title: Product name, 1-32 characters.
        :type title: :obj:`str`
        :param description: Product description, 1-255 characters.
        :type description: :obj:`str`
        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
        :type payload: :obj:`str`
        :param currency: Three-letter ISO 4217 currency code, see `more on currencies <https://core.telegram.org/bots/payments#supported-currencies>`_. Pass “XTR” for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type currency: :obj:`str`
        :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type prices: :obj:`list` of :obj:`~apitele.types.LabeledPrice`
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param provider_token: Payment provider token, obtained via `@BotFather <https://t.me/botfather>`_. Pass an empty string for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type provider_token: :obj:`str`, optional
        :param max_tip_amount: The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of ``US$ 1.45`` pass ``max_tip_amount = 145``. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to :obj:`0`. Not supported for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
        :type max_tip_amount: :obj:`int`, optional
        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*.
        :type suggested_tip_amounts: :obj:`list` of :obj:`int`, optional
        :param start_parameter: Unique deep-linking parameter. If left empty, **forwarded copies** of the sent message will have a *Pay* button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a *URL* button with a deep link to the bot (instead of a *Pay* button), with the value used as the start parameter.
        :type start_parameter: :obj:`str`, optional
        :param provider_data: JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
        :type provider_data: :obj:`str`, optional
        :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
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
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_. If empty, one 'Pay ``total price``' button will be shown. If not empty, the first button must be a Pay button.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'title': title,
            'description': description,
            'payload': payload,
            'provider_token': provider_token,
            'currency': currency,
            'prices': prices
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if max_tip_amount is not None: params['max_tip_amount'] = max_tip_amount
        if suggested_tip_amounts is not None: params['suggested_tip_amounts'] = suggested_tip_amounts
        if start_parameter is not None: params['start_parameter'] = start_parameter
        if provider_data is not None: params['provider_data'] = provider_data
        if photo_url is not None: params['photo_url'] = photo_url
        if photo_size is not None: params['photo_size'] = photo_size
        if photo_width is not None: params['photo_width'] = photo_width
        if photo_height is not None: params['photo_height'] = photo_height
        if need_name is not None: params['need_name'] = need_name
        if need_phone_number is not None: params['need_phone_number'] = need_phone_number
        if need_email is not None: params['need_email'] = need_email
        if need_shipping_address is not None: params['need_shipping_address'] = need_shipping_address
        if send_phone_number_to_provider is not None: params['send_phone_number_to_provider'] = send_phone_number_to_provider
        if send_email_to_provider is not None: params['send_email_to_provider'] = send_email_to_provider
        if is_flexible is not None: params['is_flexible'] = is_flexible
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_invoice(params)
        return Message._dese(result)


    async def send_location(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendlocation

        Use this method to send point on the map.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param latitude: Latitude of the location.
        :type latitude: :obj:`float`
        :param longitude: Longitude of the location.
        :type longitude: :obj:`float`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500.
        :type horizontal_accuracy: :obj:`float`, optional
        :param live_period: Period in seconds for which the location will be updated (see `Live Locations <https://telegram.org/blog/live-locations>`_, should be between 60 and 86400.
        :type live_period: :obj:`int`, optional
        :param heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        :type heading: :obj:`int`, optional
        :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        :type proximity_alert_radius: :obj:`int`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if horizontal_accuracy is not None: params['horizontal_accuracy'] = horizontal_accuracy
        if live_period is not None: params['live_period'] = live_period
        if heading is not None: params['heading'] = heading
        if proximity_alert_radius is not None: params['proximity_alert_radius'] = proximity_alert_radius
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_location(params)
        return Message._dese(result)


    async def send_media_group(
        self,
        chat_id: Union[int, str],
        media: list[Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None
    ) -> list[Message]:
        '''
        https://core.telegram.org/bots/api#sendmediagroup

        Use this method to send a group of photos, videos, documents or audios as an album.
        Documents and audio files can be only grouped in an album with messages of the same type.
        On success, an array of :obj:`Messages <apitele.types.Message>` that were sent is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param media: A JSON-serialized array describing messages to be sent, must include 2-10 items.
        :type media: :obj:`list` of :obj:`~apitele.types.InputMediaAudio`, :obj:`~apitele.types.InputMediaDocument`, :obj:`~apitele.types.InputMediaPhoto` and :obj:`~apitele.types.InputMediaVideo`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param disable_notification: Sends messages `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent messages from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :rtype: :obj:`list` of :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'media': media
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        result = await super().send_media_group(params)
        return [Message._dese(message) for message in result]


    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendmessage

        Use this method to send text messages.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param text: Text of the message to be sent, 1-4096 characters after entities parsing.
        :type text: :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param parse_mode: Mode for parsing entities in the message text. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param entities: A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*.
        :type entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param link_preview_options: Link preview generation options for the message.
        :type link_preview_options: :obj:`~apitele.types.LinkPreviewOptions`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'text': text
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if entities is not None: params['entities'] = entities
        if link_preview_options is not None: params['link_preview_options'] = link_preview_options
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_message(params)
        return Message._dese(result)


    async def send_paid_media(
        self,
        chat_id: Union[int, str],
        star_count: int,
        media: list[InputPaidMedia],
        business_connection_id: Optional[str] = None,
        payload: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendpaidmedia

        Use this method to send paid media to channel chats.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param star_count: The number of Telegram Stars that must be paid to buy access to the media.
        :type star_count: :obj:`int`
        :param media: A JSON-serialized array describing the media to be sent; up to 10 items.
        :type media: :obj:`list` of :obj:`~apitele.types.InputPaidMedia`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param payload: Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes.
        :type payload: :obj:`str`, optional
        :param caption: Media caption, 0-1024 characters after entities parsing
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the media caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
        :type show_caption_above_media: :obj:`bool`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove a reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'star_count': star_count,
            'media': media
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if payload is not None: params['payload'] = payload
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if show_caption_above_media is not None: params['show_caption_above_media'] = show_caption_above_media
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_paid_media(params)
        return Message._dese(result)


    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendphoto

        Use this method to send photos.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type photo: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param caption: Photo caption (may also be used when resending photos by *file_id*), 0-1024 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the photo caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
        :type show_caption_above_media: :obj:`bool`, optional
        :param has_spoiler: Pass :obj:`True` if the photo needs to be covered with a spoiler animation.
        :type has_spoiler: :obj:`bool`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if show_caption_above_media is not None: params['show_caption_above_media'] = show_caption_above_media
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_photo(params)
        return Message._dese(result)


    async def send_poll(
        self,
        chat_id: Union[int, str],
        question: str,
        options: list[InputPollOption],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        question_parse_mode: Optional[str] = None,
        question_entities: Optional[list[MessageEntity]] = None,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[list[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendpoll

        Use this method to send a native poll.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param question: Poll question, 1-300 characters.
        :type question: :obj:`str`
        :param options: A JSON-serialized list of 2-10 answer options.
        :type options: :obj:`list` of :obj:`~apitele.types.InputPollOption`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param question_parse_mode: Mode for parsing entities in the question. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details. Currently, only custom emoji entities are allowed.
        :type question_parse_mode: :obj:`str`, optional
        :param question_entities: A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of *question_parse_mode*.
        :type question_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param is_anonymous: :obj:`True`, if the poll needs to be anonymous, defaults to :obj:`True`.
        :type is_anonymous: :obj:`bool`, optional
        :param type: Poll type, “quiz” or “regular”, defaults to “regular”.
        :type type: :obj:`str`, optional
        :param allows_multiple_answers: :obj:`True`, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to :obj:`False`.
        :type allows_multiple_answers: :obj:`bool`, optional
        :param correct_option_id: 0-based identifier of the correct answer option, required for polls in quiz mode.
        :type correct_option_id: :obj:`int`, optional
        :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing.
        :type explanation: :obj:`str`, optional
        :param explanation_parse_mode: Mode for parsing entities in the explanation. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type explanation_parse_mode: :obj:`str`, optional
        :param explanation_entities: A JSON-serialized list of special entities that appear in the poll explanation, which can be specified instead of *parse_mode*.
        :type explanation_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param open_period: Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with *close_date*.
        :type open_period: :obj:`int`, optional
        :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with *open_period*.
        :type close_date: :obj:`int`, optional
        :param is_closed: Pass :obj:`True` if the poll needs to be immediately closed. This can be useful for poll preview.
        :type is_closed: :obj:`bool`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'question': question,
            'options': options
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if question_parse_mode is not None: params['question_parse_mode'] = question_parse_mode
        if question_entities is not None: params['question_entities'] = question_entities
        if is_anonymous is not None: params['is_anonymous'] = is_anonymous
        if type is not None: params['type'] = type
        if allows_multiple_answers is not None: params['allows_multiple_answers'] = allows_multiple_answers
        if correct_option_id is not None: params['correct_option_id'] = correct_option_id
        if explanation is not None: params['explanation'] = explanation
        if explanation_parse_mode is not None: params['explanation_parse_mode'] = explanation_parse_mode
        if explanation_entities is not None: params['explanation_entities'] = explanation_entities
        if open_period is not None: params['open_period'] = open_period
        if close_date is not None: params['close_date'] = close_date
        if is_closed is not None: params['is_closed'] = is_closed
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_poll(params)
        return Message._dese(result)


    async def send_sticker(
        self,
        chat_id: Union[int, str],
        sticker: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendsticker

        Use this method to send static .WEBP, `animated <https://telegram.org/blog/animated-stickers>`_ .TGS, or `video <https://telegram.org/blog/video-stickers-better-reactions>`_ .WEBM stickers.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP or .TGS sticker using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_. Video stickers can only be sent by a file_id. Animated stickers can't be sent via an HTTP URL.
        :type sticker: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param emoji: Emoji associated with the sticker; only for just uploaded stickers.
        :type emoji: :obj:`str`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'sticker': sticker
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if emoji is not None: params['emoji'] = emoji
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_sticker(params)
        return Message._dese(result)


    async def send_venue(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendvenue

        Use this method to send information about a venue.
        On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param latitude: Latitude of the venue.
        :type latitude: :obj:`float`
        :param longitude: Longitude of the venue.
        :type longitude: :obj:`float`
        :param title: Name of the venue.
        :type title: :obj:`str`
        :param address: Address of the venue.
        :type address: :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param foursquare_id: Foursquare identifier of the venue.
        :type foursquare_id: :obj:`str`, optional
        :param foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
        :type foursquare_type: :obj:`str`, optional
        :param google_place_id: Google Places identifier of the venue.
        :type google_place_id: :obj:`str`, optional
        :param google_place_type: Google Places type of the venue. (See `supported types <https://developers.google.com/places/web-service/supported_types>`_.)
        :type google_place_type: :obj:`str`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if foursquare_id is not None: params['foursquare_id'] = foursquare_id
        if foursquare_type is not None: params['foursquare_type'] = foursquare_type
        if google_place_id is not None: params['google_place_id'] = google_place_id
        if google_place_type is not None: params['google_place_type'] = google_place_type
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_venue(params)
        return Message._dese(result)


    async def send_video(
        self,
        chat_id: Union[int, str],
        video: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        cover: Optional[Union[InputFile, str]] = None,
        start_timestamp: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendvideo

        Use this method to send video files, Telegram clients support MPEG4 videos
        (other formats may be sent as :obj:`~apitele.types.Document`). On success,
        the sent :obj:`~apitele.types.Message` is returned. Bots can currently send
        video files of up to 50 MB in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type video: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param duration: Duration of sent video in seconds.
        :type duration: :obj:`int`, optional
        :param width: Video width.
        :type width: :obj:`int`, optional
        :param height: Video height.
        :type height: :obj:`int`, optional
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
        :param cover: Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type cover: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
        :param start_timestamp: Start timestamp for the video in the message.
        :type start_timestamp: :obj:`int`, optional
        :param caption: Video caption (may also be used when resending videos by *file_id*), 0-1024 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the video caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param show_caption_above_media: Pass :obj:`True`, if the caption must be shown above the message media.
        :type show_caption_above_media: :obj:`bool`, optional
        :param has_spoiler: Pass :obj:`True` if the video needs to be covered with a spoiler animation.
        :type has_spoiler: :obj:`bool`, optional
        :param supports_streaming: Pass :obj:`True` if the uploaded video is suitable for streaming.
        :type supports_streaming: :obj:`bool`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'video': video
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if cover is not None: params['cover'] = cover
        if start_timestamp is not None: params['start_timestamp'] = start_timestamp
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if show_caption_above_media is not None: params['show_caption_above_media'] = show_caption_above_media
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if supports_streaming is not None: params['supports_streaming'] = supports_streaming
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_video(params)
        return Message._dese(result)


    async def send_video_note(
        self,
        chat_id: Union[int, str],
        video_note: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendvideonote

        As of `v.4.0 <https://telegram.org/blog/video-messages-and-telescope>`_,
        Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this
        method to send video messages. On success, the sent :obj:`~apitele.types.Message` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param video_note: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_. Sending video notes by a URL is currently unsupported.
        :type video_note: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param duration: Duration of sent video in seconds.
        :type duration: :obj:`int`, optional
        :param length: Video width and height, i.e. diameter of the video message.
        :type length: :obj:`int`, optional
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'video_note': video_note
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if length is not None: params['length'] = length
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_video_note(params)
        return Message._dese(result)


    async def send_voice(
        self,
        chat_id: Union[int, str],
        voice: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[REPLY_MARKUP_TYPES] = None
    ) -> Message:
        '''
        https://core.telegram.org/bots/api#sendvoice

        Use this method to send audio files, if you want Telegram clients to display the file as
        a playable voice message. For this to work, your audio must be in an .OGG file encoded with
        OPUS, or in .MP3 format, or in .M4A (other formats may be sent as :obj:`~apitele.types.Audio` or :obj:`~apitele.types.Document`).
        On success, the sent :obj:`~apitele.types.Message` is returned. Bots can currently send voice
        messages of up to 50 MB in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param voice: Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type voice: :obj:`~apitele.types.InputFile` or :obj:`str`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent.
        :type business_connection_id: :obj:`str`, optional
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
        :type message_thread_id: :obj:`int`, optional
        :param caption: Voice message caption, 0-1024 characters after entities parsing.
        :type caption: :obj:`str`, optional
        :param parse_mode: Mode for parsing entities in the voice message caption. See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        :type parse_mode: :obj:`str`, optional
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*.
        :type caption_entities: :obj:`list` of :obj:`~apitele.types.MessageEntity`, optional
        :param duration: Duration of the voice message in seconds.
        :type duration: :obj:`int`, optional
        :param disable_notification: Sends the message `silently <https://telegram.org/blog/channels-2-0#silent-messages>`_. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`, optional
        :param protect_content: Protects the contents of the sent message from forwarding and saving.
        :type protect_content: :obj:`bool`, optional
        :param allow_paid_broadcast: Pass :obj:`True` to allow up to 1000 messages per second, ignoring `broadcasting limits <https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once>`_ for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance.
        :type allow_paid_broadcast: :obj:`bool`, optional
        :param message_effect_id: Unique identifier of the message effect to be added to the message; for private chats only.
        :type message_effect_id: :obj:`str`, optional
        :param reply_parameters: Description of the message to reply to.
        :type reply_parameters: :obj:`~apitele.types.ReplyParameters`, optional
        :param reply_markup: Additional interface options. A JSON-serialized object for an `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_, `custom reply keyboard <https://core.telegram.org/bots/features#keyboards>`_, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`~apitele.types.REPLY_MARKUP_TYPES`, optional
        :rtype: :obj:`~apitele.types.Message`
        '''
        params = {
            'chat_id': chat_id,
            'voice': voice
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if duration is not None: params['duration'] = duration
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if allow_paid_broadcast is not None: params['allow_paid_broadcast'] = allow_paid_broadcast
        if message_effect_id is not None: params['message_effect_id'] = message_effect_id
        if reply_parameters is not None: params['reply_parameters'] = reply_parameters
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_voice(params)
        return Message._dese(result)


    async def set_business_account_bio(
        self,
        business_connection_id: str,
        bio: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setbusinessaccountbio

        Changes the bio of a managed business account. Requires the *can_change_bio* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param bio: The new value of the bio for the business account; 0-140 characters.
        :type bio: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id
        }
        if bio is not None: params['bio'] = bio
        return await super().set_business_account_bio(params)


    async def set_business_account_gift_settings(
        self,
        business_connection_id: str,
        show_gift_button: bool,
        accepted_gift_types: AcceptedGiftTypes
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setbusinessaccountgiftsettings

        Changes the privacy settings pertaining to incoming gifts in a managed business account.
        Requires the *can_change_gift_settings* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param show_gift_button: Pass :obj:`True`, if a button for sending a gift to the user or by the business account must always be shown in the input field.
        :type show_gift_button: :obj:`bool`
        :param accepted_gift_types: Types of gifts accepted by the business account.
        :type accepted_gift_types: :obj:`~apitele.types.AcceptedGiftTypes`
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'show_gift_button': show_gift_button,
            'accepted_gift_types': accepted_gift_types
        }
        return await super().set_business_account_gift_settings(params)


    async def set_business_account_name(
        self,
        business_connection_id: str,
        first_name: str,
        last_name: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setbusinessaccountname

        Changes the first and last name of a managed business account. Requires the *can_change_name* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param first_name: The new value of the first name for the business account; 1-64 characters.
        :type first_name: :obj:`str`
        :param last_name: The new value of the last name for the business account; 0-64 characters.
        :type last_name: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'first_name': first_name
        }
        if last_name is not None: params['last_name'] = last_name
        return await super().set_business_account_name(params)


    async def set_business_account_profile_photo(
        self,
        business_connection_id: str,
        photo: InputProfilePhoto,
        is_public: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setbusinessaccountprofilephoto

        Changes the profile photo of a managed business account. Requires the *can_edit_profile_photo* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param photo: The new profile photo to set.
        :type photo: :obj:`~apitele.types.InputProfilePhoto`
        :param is_public: Pass :obj:`True` to set the public photo, which will be visible even if the main photo is hidden by the business account's privacy settings. An account can have only one public photo.
        :type is_public: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'photo': photo
        }
        if is_public is not None: params['is_public'] = is_public
        return await super().set_business_account_profile_photo(params)


    async def set_business_account_username(
        self,
        business_connection_id: str,
        username: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setbusinessaccountusername

        Changes the username of a managed business account. Requires the *can_change_username* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param username: The new value of the username for the business account; 0-32 characters.
        :type username: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id
        }
        if username is not None: params['username'] = username
        return await super().set_business_account_username(params)


    async def set_chat_administrator_custom_title(
        self,
        chat_id: Union[int, str],
        user_id: int,
        custom_title: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setchatadministratorcustomtitle

        Use this method to set a custom title for an administrator
        in a supergroup promoted by the bot. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :param custom_title: New custom title for the administrator; 0-16 characters, emoji are not allowed.
        :type custom_title: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'custom_title': custom_title
        }
        return await super().set_chat_administrator_custom_title(params)


    async def set_chat_description(
        self,
        chat_id: Union[int, str],
        description: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setchatdescription

        Use this method to change the description of a group, a supergroup or a
        channel. The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param description: New chat description, 0-255 characters.
        :type description: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        if description is not None: params['description'] = description
        return await super().set_chat_description(params)


    async def set_chat_menu_button(
        self,
        chat_id: Optional[int] = None,
        menu_button: Optional[MenuButton] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setchatmenubutton

        Use this method to change the bot's menu button in a private
        chat, or the default menu button. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target private chat. If not specified, default bot's menu button will be changed.
        :type chat_id: :obj:`int`, optional
        :param menu_button: A JSON-serialized object for the bot's new menu button. Defaults to :obj:`~apitele.types.MenuButtonDefault`.
        :type menu_button: :obj:`~apitele.types.MenuButton`, optional
        :rtype: :obj:`True`
        '''
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if menu_button is not None: params['menu_button'] = menu_button
        return await super().set_chat_menu_button(params)


    async def set_chat_permissions(
        self,
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setchatpermissions

        Use this method to set default chat permissions for all members. The bot
        must be an administrator in the group or a supergroup for this to work and must
        have the *can_restrict_members* administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param permissions: A JSON-serialized object for new default chat permissions.
        :type permissions: :obj:`~apitele.types.ChatPermissions`
        :param use_independent_chat_permissions: Pass :obj:`True` if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission.
        :type use_independent_chat_permissions: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'permissions': permissions
        }
        if use_independent_chat_permissions is not None: params['use_independent_chat_permissions'] = use_independent_chat_permissions
        return await super().set_chat_permissions(params)


    async def set_chat_photo(
        self,
        chat_id: Union[int, str],
        photo: InputFile
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setchatphoto

        Use this method to set a new profile photo for the chat. Photos can't be changed
        for private chats. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param photo: New chat photo, uploaded using multipart/form-data.
        :type photo: :obj:`~apitele.types.InputFile`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        return await super().set_chat_photo(params)


    async def set_chat_sticker_set(
        self,
        chat_id: Union[int, str],
        sticker_set_name: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setchatstickerset

        Use this method to set a new group sticker set for a supergroup.
        The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. Use the field
        *can_set_sticker_set* optionally returned in :meth:`~apitele.Client.get_chat`
        requests to check if the bot can use this method. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param sticker_set_name: Name of the sticker set to be set as the group sticker set.
        :type sticker_set_name: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'sticker_set_name': sticker_set_name
        }
        return await super().set_chat_sticker_set(params)


    async def set_chat_title(
        self,
        chat_id: Union[int, str],
        title: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setchattitle

        Use this method to change the title of a chat. Titles can't be changed for
        private chats. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param title: New chat title, 1-128 characters.
        :type title: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'title': title
        }
        return await super().set_chat_title(params)


    async def set_custom_emoji_sticker_set_thumbnail(
        self,
        name: str,
        custom_emoji_id: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setcustomemojistickersetthumbnail

        Use this method to set the thumbnail of a custom emoji sticker set.
        Returns :obj:`True` on success.

        :param name: Sticker set name.
        :type name: :obj:`str`
        :param custom_emoji_id: Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.
        :type custom_emoji_id: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'name': name
        }
        if custom_emoji_id is not None: params['custom_emoji_id'] = custom_emoji_id
        return await super().set_custom_emoji_sticker_set_thumbnail(params)


    async def set_game_score(
        self,
        user_id: int,
        score: int,
        force: Optional[bool] = None,
        disable_edit_message: Optional[bool] = None,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> Union[Message, Literal[True]]:
        '''
        https://core.telegram.org/bots/api#setgamescore

        Use this method to set the score of the specified user in a game message.
        On success, if the message is not an inline message, the :obj:`~apitele.types.Message`
        is returned, otherwise :obj:`True` is returned. Returns an error, if the new score
        is not greater than the user's current score in the chat and *force* is :obj:`False`.

        :param user_id: User identifier.
        :type user_id: :obj:`int`
        :param score: New score, must be non-negative.
        :type score: :obj:`int`
        :param force: Pass :obj:`True` if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters.
        :type force: :obj:`bool`, optional
        :param disable_edit_message: Pass :obj:`True` if the game message should not be automatically edited to include the current scoreboard.
        :type disable_edit_message: :obj:`bool`, optional
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat.
        :type chat_id: :obj:`int`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the sent message.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :rtype: :obj:`~apitele.types.Message` or :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'score': score
        }
        if force is not None: params['force'] = force
        if disable_edit_message is not None: params['disable_edit_message'] = disable_edit_message
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        result = await super().set_game_score(params)
        return Message._dese(result) if result is not True else True


    async def set_message_reaction(
        self,
        chat_id: Union[int, str],
        message_id: int,
        reaction: Optional[list[ReactionType]] = None,
        is_big: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setmessagereaction

        Use this method to change the chosen reactions on a message. Service messages can't
        be reacted to. Automatically forwarded messages from a channel to its discussion group
        have the same available reactions as messages in the channel. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_id: Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead.
        :type message_id: :obj:`int`
        :param reaction: A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators.
        :type reaction: :obj:`list` of :obj:`~apitele.types.ReactionType`, optional
        :param is_big: Pass :obj:`True` to set the reaction with a big animation.
        :type is_big: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        if reaction is not None: params['reaction'] = reaction
        if is_big is not None: params['is_big'] = is_big
        return await super().set_message_reaction(params)


    async def set_my_commands(
        self,
        commands: list[BotCommand],
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setmycommands

        Use this method to change the list of the bot's commands.
        See `this manual <https://core.telegram.org/bots/features#commands>`_ 
        for more details about bot commands. Returns :obj:`True` on success.

        :param commands: A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
        :type commands: :obj:`list` of :obj:`~apitele.types.BotCommand`
        :param scope: A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to :obj:`~apitele.types.BotCommandScopeDefault`.
        :type scope: :obj:`~apitele.types.BotCommandScope`, optional
        :param language_code: A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'commands': commands
        }
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_commands(params)


    async def set_my_default_administrator_rights(
        self,
        rights: Optional[ChatAdministratorRights] = None,
        for_channels: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setmydefaultadministratorrights

        Use this method to change the default administrator rights requested by the bot when
        it's added as an administrator to groups or channels. These rights will be suggested to
        users, but they are free to modify the list before adding the bot. Returns :obj:`True` on success.

        :param rights: A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared.
        :type rights: :obj:`~apitele.types.ChatAdministratorRights`, optional
        :param for_channels: Pass :obj:`True` to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
        :type for_channels: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {}
        if rights is not None: params['rights'] = rights
        if for_channels is not None: params['for_channels'] = for_channels
        return await super().set_my_default_administrator_rights(params)


    async def set_my_description(
        self,
        description: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setmydescription

        Use this method to change the bot's description, which is shown in
        the chat with the bot if the chat is empty. Returns :obj:`True` on success.

        :param description: New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.
        :type description: :obj:`str`, optional
        :param language_code: A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {}
        if description is not None: params['description'] = description
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_description(params)


    async def set_my_name(
        self,
        name: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setmyname

        Use this method to change the bot's name. Returns :obj:`True` on success.

        :param name: New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.
        :type name: :obj:`str`, optional
        :param language_code: A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {}
        if name is not None: params['name'] = name
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_name(params)


    async def set_my_short_description(
        self,
        short_description: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setmyshortdescription

        Use this method to change the bot's short description, which is shown on the bot's profile
        page and is sent together with the link when users share the bot. Returns :obj:`True` on success.

        :param short_description: New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.
        :type short_description: :obj:`str`, optional
        :param language_code: A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description.
        :type language_code: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {}
        if short_description is not None: params['short_description'] = short_description
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_short_description(params)


    async def set_passport_data_errors(
        self,
        user_id: int,
        errors: list[PassportElementError]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setpassportdataerrors

        Informs a user that some of the Telegram Passport elements they provided contains errors. The user
        will not be able to re-submit their Passport to you until the errors are fixed (the contents of the
        field for which you returned the error must change). Returns :obj:`True` on success.

        Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason.
        For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering,
        etc. Supply some details in the error message to make sure the user knows how to correct the issues.

        :param user_id: User identifier.
        :type user_id: :obj:`int`
        :param errors: A JSON-serialized array describing the errors.
        :type errors: :obj:`list` of :obj:`~apitele.types.PassportElementError`
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id,
            'errors': errors
        }
        return await super().set_passport_data_errors(params)


    async def set_sticker_emoji_list(
        self,
        sticker: str,
        emoji_list: list[str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setstickeremojilist

        Use this method to change the list of emoji assigned to a regular or custom emoji sticker.
        The sticker must belong to a sticker set created by the bot. Returns :obj:`True` on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`
        :param emoji_list: A JSON-serialized list of 1-20 emoji associated with the sticker.
        :type emoji_list: :obj:`list` of :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'sticker': sticker,
            'emoji_list': emoji_list
        }
        return await super().set_sticker_emoji_list(params)


    async def set_sticker_keywords(
        self,
        sticker: str,
        keywords: Optional[list[str]] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setstickerkeywords

        Use this method to change search keywords assigned to a regular or custom emoji sticker.
        The sticker must belong to a sticker set created by the bot. Returns :obj:`True` on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`
        :param keywords: A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters.
        :type keywords: :obj:`list` of :obj:`str`, optional

        :rtype: :obj:`True`
        '''
        params = {
            'sticker': sticker
        }
        if keywords is not None: params['keywords'] = keywords
        return await super().set_sticker_keywords(params)


    async def set_sticker_mask_position(
        self,
        sticker: str,
        mask_position: Optional[MaskPosition] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setstickermaskposition

        Use this method to change the :obj:`mask position <apitele.types.MaskPosition>` of a mask sticker.
        The sticker must belong to a sticker set that was created by the bot. Returns :obj:`True` on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`
        :param mask_position: A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position.
        :type mask_position: :obj:`~apitele.types.MaskPosition`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'sticker': sticker
        }
        if mask_position is not None: params['mask_position'] = mask_position
        return await super().set_sticker_mask_position(params)


    async def set_sticker_position_in_set(
        self,
        sticker: str,
        position: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setstickerpositioninset

        Use this method to move a sticker in a set created by the bot to a specific position.
        Returns :obj:`True` on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`
        :param position: New sticker position in the set, zero-based.
        :type position: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'sticker': sticker,
            'position': position
        }
        return await super().set_sticker_position_in_set(params)


    async def set_sticker_set_thumbnail(
        self,
        name: str,
        user_id: int,
        format: str,
        thumbnail: Optional[Union[InputFile, str]] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setstickersetthumbnail

        Use this method to set the thumbnail of a regular or mask sticker set. The format of the
        thumbnail file must match the format of the stickers in the set. Returns :obj:`True` on success.

        :param name: Sticker set name.
        :type name: :obj:`str`
        :param user_id: User identifier of the sticker set owner.
        :type user_id: :obj:`int`
        :param format: Format of the thumbnail, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, or “video” for a **WEBM** video.
        :type format: :obj:`str`
        :param thumbnail: A **.WEBP** or **.PNG** image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a **.TGS** animation with a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements), or a **WEBM** video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical requirements. Pass a *file_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_. Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.
        :type thumbnail: :obj:`~apitele.types.InputFile` or :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'name': name,
            'user_id': user_id,
            'format': format
        }
        if thumbnail is not None: params['thumbnail'] = thumbnail
        return await super().set_sticker_set_thumbnail(params)


    async def set_sticker_set_title(
        self,
        name: str,
        title: str
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setstickersettitle

        Use this method to set the title of a created sticker set. Returns :obj:`True` on success.

        :param name: Sticker set name.
        :type name: :obj:`str`
        :param title: Sticker set title, 1-64 characters.
        :type title: :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'name': name,
            'title': title
        }
        return await super().set_sticker_set_title(params)


    async def set_user_emoji_status(
        self,
        user_id: int,
        emoji_status_custom_emoji_id: Optional[str] = None,
        emoji_status_expiration_date: Optional[int] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#setuseremojistatus

        Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method `requestEmojiStatusAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`_. Returns :obj:`True` on success.

        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :param emoji_status_custom_emoji_id: Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status.
        :type emoji_status_custom_emoji_id: :obj:`str`, optional
        :param emoji_status_expiration_date: Expiration date of the emoji status, if any.
        :type emoji_status_expiration_date: :obj:`int`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id
        }
        if emoji_status_custom_emoji_id is not None: params['emoji_status_custom_emoji_id'] = emoji_status_custom_emoji_id
        if emoji_status_expiration_date is not None: params['emoji_status_expiration_date'] = emoji_status_expiration_date
        return await super().set_user_emoji_status(params)


    async def stop_message_live_location(
        self,
        business_connection_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''
        https://core.telegram.org/bots/api#stopmessagelivelocation

        Use this method to stop updating a live location message before *live_period*
        expires. On success, if the message is not an inline message, the edited
        :obj:`~apitele.types.Message` is returned, otherwise :obj:`True` is returned.

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message to be edited was sent.
        :type business_connection_id: :obj:`str`, optional
        :param chat_id: Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`, optional
        :param message_id: Required if *inline_message_id* is not specified. Identifier of the message with live location to stop.
        :type message_id: :obj:`int`, optional
        :param inline_message_id: Required if *chat_id* and *message_id* are not specified. Identifier of the inline message.
        :type inline_message_id: :obj:`str`, optional
        :param reply_markup: A JSON-serialized object for a new `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Message` or :obj:`True`
        '''
        params = {}
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().stop_message_live_location(params)
        return Message._dese(result) if result is not True else True


    async def stop_poll(
        self,
        chat_id: Union[int, str],
        message_id: int,
        business_connection_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Poll:
        '''
        https://core.telegram.org/bots/api#stoppoll

        Use this method to stop a poll which was sent by the bot.
        On success, the stopped :obj:`~apitele.types.Poll` is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_id: Identifier of the original message with the poll.
        :type message_id: :obj:`int`
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message to be edited was sent.
        :type business_connection_id: :obj:`str`, optional
        :param reply_markup: A JSON-serialized object for a new `inline keyboard <https://core.telegram.org/bots/features#inline-keyboards>`_.
        :type reply_markup: :obj:`~apitele.types.InlineKeyboardMarkup`, optional
        :rtype: :obj:`~apitele.types.Poll`
        '''
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().stop_poll(params)
        return Poll._dese(result)


    async def transfer_business_account_stars(
        self,
        business_connection_id: str,
        star_count: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#transferbusinessaccountstars

        Transfers Telegram Stars from the business account balance to the bot's balance. Requires the *can_transfer_stars* business bot right. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param star_count: Number of Telegram Stars to transfer; 1-10000.
        :type star_count: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'star_count': star_count
        }
        return await super().transfer_business_account_stars(params)


    async def transfer_gift(
        self,
        business_connection_id: str,
        owned_gift_id: str,
        new_owner_chat_id: int,
        star_count: Optional[int] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#transfergift

        Transfers an owned unique gift to another user. Requires the *can_transfer_and_upgrade_gifts* business bot right.
        Requires *can_transfer_stars* business bot right if the transfer is paid. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param owned_gift_id: Unique identifier of the regular gift that should be transferred.
        :type owned_gift_id: :obj:`str`
        :param new_owner_chat_id: Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours.
        :type new_owner_chat_id: :obj:`int`
        :param star_count: The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the *can_transfer_stars* business bot right is required.
        :type star_count: :obj:`int`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'owned_gift_id': owned_gift_id,
            'new_owner_chat_id': new_owner_chat_id
        }
        if star_count is not None: params['star_count'] = star_count
        return await super().transfer_gift(params)


    async def unban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: Optional[bool] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#unbanchatmember

        Use this method to unban a previously banned user in a supergroup or channel.
        The user will **not** return to the group or channel automatically, but will be able to
        join via link, etc. The bot must be an administrator for this to work. By default, this
        method guarantees that after the call the user is not a member of the chat, but will be able
        to join it. So if the user is a member of the chat they will also be **removed** from the chat.
        If you don't want this, use the parameter *only_if_banned*. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param user_id: Unique identifier of the target user.
        :type user_id: :obj:`int`
        :param only_if_banned: Do nothing if the user is not banned.
        :type only_if_banned: :obj:`bool`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        if only_if_banned is not None: params['only_if_banned'] = only_if_banned
        return await super().unban_chat_member(params)


    async def unban_chat_sender_chat(
        self,
        chat_id: Union[int, str],
        sender_chat_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#unbanchatsenderchat

        Use this method to unban a previously banned channel chat in a supergroup or channel.
        The bot must be an administrator for this to work and must have the appropriate administrator rights.
        Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param sender_chat_id: Unique identifier of the target sender chat.
        :type sender_chat_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id
        }
        return await super().unban_chat_sender_chat(params)


    async def unhide_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#unhidegeneralforumtopic

        Use this method to unhide the 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work and must
        have the *can_manage_topics* administrator rights. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().unhide_general_forum_topic(params)


    async def unpin_all_chat_messages(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#unpinallchatmessages

        Use this method to clear the list of pinned messages in a chat.
        If the chat is not a private chat, the bot must be an administrator in
        the chat for this to work and must have the 'can_pin_messages' administrator right in
        a supergroup or 'can_edit_messages' administrator right in a channel. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().unpin_all_chat_messages(params)


    async def unpin_all_forum_topic_messages(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#unpinallforumtopicmessages

        Use this method to clear the list of pinned messages in a forum topic.
        The bot must be an administrator in the chat for this to work and must have the
        *can_pin_messages* administrator right in the supergroup. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_thread_id: Unique identifier for the target message thread of the forum topic.
        :type message_thread_id: :obj:`int`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().unpin_all_forum_topic_messages(params)


    async def unpin_all_general_forum_topic_messages(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#unpinallgeneralforumtopicmessages

        Use this method to clear the list of pinned messages in a General forum topic.
        The bot must be an administrator in the chat for this to work and must have the
        *can_pin_messages* administrator right in the supergroup. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format ``@supergroupusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        return await super().unpin_all_general_forum_topic_messages(params)


    async def unpin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: Optional[int] = None,
        business_connection_id: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#unpinchatmessage

        Use this method to remove a message from the list of pinned messages in a chat.
        If the chat is not a private chat, the bot must be an administrator in the chat for this
        to work and must have the 'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param message_id: Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned.
        :type message_id: :obj:`int`, optional
        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be unpinned.
        :type business_connection_id: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        if message_id is not None: params['message_id'] = message_id
        if business_connection_id is not None: params['business_connection_id'] = business_connection_id
        return await super().unpin_chat_message(params)


    async def upgrade_gift(
        self,
        business_connection_id: str,
        owned_gift_id: str,
        keep_original_details: Optional[bool] = None,
        star_count: Optional[int] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#upgradegift

        Upgrades a given regular gift to a unique gift. Requires the *can_transfer_and_upgrade_gifts* business bot right.
        Additionally requires the *can_transfer_stars* business bot right if the upgrade is paid. Returns :obj:`True` on success.

        :param business_connection_id: Unique identifier of the business connection.
        :type business_connection_id: :obj:`str`
        :param owned_gift_id: Unique identifier of the regular gift that should be upgraded to a unique one.
        :type owned_gift_id: :obj:`str`
        :param keep_original_details: Pass :obj:`True` to keep the original gift text, sender and receiver in the upgraded gift.
        :type keep_original_details: :obj:`bool`, optional
        :param star_count: The amount of Telegram Stars that will be paid for the upgrade from the business account balance. ``If gift.prepaid_upgrade_star_count > 0``, then pass 0, otherwise, the *can_transfer_stars* business bot right is required and ``gift.upgrade_star_count`` must be passed.
        :type star_count: :obj:`int`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'business_connection_id': business_connection_id,
            'owned_gift_id': owned_gift_id
        }
        if keep_original_details is not None: params['keep_original_details'] = keep_original_details
        if star_count is not None: params['star_count'] = star_count
        return await super().upgrade_gift(params)


    async def upload_sticker_file(
        self,
        user_id: int,
        sticker: InputFile,
        sticker_format: str
    ) -> File:
        '''
        https://core.telegram.org/bots/api#uploadstickerfile

        Use this method to upload a file with a sticker for later use in the
        :meth:`~apitele.Client.create_new_sticker_set` and :meth:`~apitele.Client.add_sticker_to_set` methods
        (the file can be used multiple times). Returns the uploaded :obj:`~apitele.types.File` on success.

        :param user_id: User identifier of sticker file owner.
        :type user_id: :obj:`int`
        :param sticker: A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See https://core.telegram.org/stickers for technical requirements. `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_.
        :type sticker: :obj:`~apitele.types.InputFile`
        :param sticker_format: Format of the sticker, must be one of “static”, “animated”, “video”.
        :type sticker_format: :obj:`str`
        :rtype: :obj:`~apitele.types.File`
        '''
        params = {
            'user_id': user_id,
            'sticker': sticker,
            'sticker_format': sticker_format
        }
        result = await super().upload_sticker_file(params)
        return File._dese(result)


    async def verify_chat(
        self,
        chat_id: Union[int, str],
        custom_description: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#verifychat

        Verifies a chat `on behalf of the organization <https://telegram.org/verify#third-party-verification>`_ which is represented by the bot. Returns :obj:`True` on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type chat_id: :obj:`int` or :obj:`str`
        :param custom_description: Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description.
        :type custom_description: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'chat_id': chat_id
        }
        if custom_description is not None: params['custom_description'] = custom_description
        return await super().verify_chat(params)


    async def verify_user(
        self,
        user_id: Union[int, str],
        custom_description: Optional[str] = None
    ) -> Literal[True]:
        '''
        https://core.telegram.org/bots/api#verifyuser

        Verifies a user `on behalf of the organization <https://telegram.org/verify#third-party-verification>`_ which is represented by the bot. Returns :obj:`True` on success.

        :param user_id: Unique identifier for the target chat or username of the target channel (in the format ``@channelusername``).
        :type user_id: :obj:`int` or :obj:`str`
        :param custom_description: Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description.
        :type custom_description: :obj:`str`, optional
        :rtype: :obj:`True`
        '''
        params = {
            'user_id': user_id
        }
        if custom_description is not None: params['custom_description'] = custom_description
        return await super().verify_user(params)

