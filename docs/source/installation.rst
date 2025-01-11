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

Install the module using `pip <https://pypi.org/project/pro_telegram/>`_ with your shell.

.. code-block:: bash

    $ pip install pro_telegram

Update the module regurarly with the following command.

.. code-block:: bash

    $ pip install -U pro_telegram

Usage
-----

Call the method :meth:`~aiotgm.Client.long_polling` to manage :obj:`updates <aiotgm.types.Update>` from the Telegram Bot API Server.

.. code-block:: python3

    import aiotgm
    import asyncio
    from aiotgm.types import Message, CallbackQuery

    bot = aiotgm.Client('<your_api_token>')

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

There are 22 decorator methods to manage differrent :obj:`updates <aiotgm.types.Update>`:

* :meth:`~aiotgm.Client.manage_message`
* :meth:`~aiotgm.Client.manage_edited_message`
* :meth:`~aiotgm.Client.manage_channel_post`
* :meth:`~aiotgm.Client.manage_edited_channel_post`
* :meth:`~aiotgm.Client.manage_business_connection`
* :meth:`~aiotgm.Client.manage_business_message`
* :meth:`~aiotgm.Client.manage_edited_business_message`
* :meth:`~aiotgm.Client.manage_deleted_business_messages`
* :meth:`~aiotgm.Client.manage_message_reaction`
* :meth:`~aiotgm.Client.manage_message_reaction_count`
* :meth:`~aiotgm.Client.manage_inline_query`
* :meth:`~aiotgm.Client.manage_chosen_inline_result`
* :meth:`~aiotgm.Client.manage_callback_query`
* :meth:`~aiotgm.Client.manage_shipping_query`
* :meth:`~aiotgm.Client.manage_pre_checkout_query`
* :meth:`~aiotgm.Client.manage_poll`
* :meth:`~aiotgm.Client.manage_poll_answer`
* :meth:`~aiotgm.Client.manage_my_chat_member`
* :meth:`~aiotgm.Client.manage_chat_member`
* :meth:`~aiotgm.Client.manage_chat_join_request`
* :meth:`~aiotgm.Client.manage_chat_boost`
* :meth:`~aiotgm.Client.manage_removed_chat_boost`
