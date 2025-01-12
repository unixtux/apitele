===========
Get Started
===========

Prerequisites
-------------

You require a good python knowledge with the `asyncio module <https://docs.python.org/3/library/asyncio.html>`_
and a Telegram Bot API token, you can get it via `@BotFather <https://t.me/botfather>`_.

Dependencies
------------

* Python >= 3.8
* `aiohttp <https://github.com/aio-libs/aiohttp>`_
* Optional `ujson <https://github.com/ultrajson/ultrajson>`_ & `certifi <https://github.com/certifi/python-certifi>`_

Installation
------------

Install the module using `pip <https://pypi.org/project/apitele/>`_ with your shell.

.. code-block:: bash

    $ pip install apitele

Update the module regurarly with the following command.

.. code-block:: bash

    $ pip install -U apitele

Usage
-----

Call the method :meth:`~apitele.Client.long_polling` to manage :obj:`updates <apitele.types.Update>` from the Telegram Bot API Server.

.. code-block:: python3

    import apitele
    import asyncio
    from apitele.types import Message, CallbackQuery

    bot = apitele.Client('<your_api_token>')

    @bot.manage_message()
    async def foo(msg: Message):
        await bot.send_message(msg.chat.id, 'hello')

    @bot.manage_callback_query()
    async def foo(call: CallbackQuery):
        await bot.answer_callback_query(call.id, 'hello')

    if __name__ == '__main__':
        try:
            asyncio.run(bot.long_polling())
        except KeyboardInterrupt:
            pass

There are 22 decorator methods to manage differrent :obj:`updates <apitele.types.Update>`:

* :meth:`~apitele.Client.manage_message`
* :meth:`~apitele.Client.manage_edited_message`
* :meth:`~apitele.Client.manage_channel_post`
* :meth:`~apitele.Client.manage_edited_channel_post`
* :meth:`~apitele.Client.manage_business_connection`
* :meth:`~apitele.Client.manage_business_message`
* :meth:`~apitele.Client.manage_edited_business_message`
* :meth:`~apitele.Client.manage_deleted_business_messages`
* :meth:`~apitele.Client.manage_message_reaction`
* :meth:`~apitele.Client.manage_message_reaction_count`
* :meth:`~apitele.Client.manage_inline_query`
* :meth:`~apitele.Client.manage_chosen_inline_result`
* :meth:`~apitele.Client.manage_callback_query`
* :meth:`~apitele.Client.manage_shipping_query`
* :meth:`~apitele.Client.manage_pre_checkout_query`
* :meth:`~apitele.Client.manage_poll`
* :meth:`~apitele.Client.manage_poll_answer`
* :meth:`~apitele.Client.manage_my_chat_member`
* :meth:`~apitele.Client.manage_chat_member`
* :meth:`~apitele.Client.manage_chat_join_request`
* :meth:`~apitele.Client.manage_chat_boost`
* :meth:`~apitele.Client.manage_removed_chat_boost`
