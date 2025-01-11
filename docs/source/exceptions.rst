==========
Exceptions
==========

Example:

.. code-block:: python3

    import asyncio
    from aiotgm.types import Message
    from aiotgm import Client, TelegramError

    bot = Client('<your_api_token>')

    @bot.manage_message()
    async def foo(msg: Message):
        try:
            await bot.send_message(msg.chat.id, "Hello my friend.")
        except (TelegramError, TimeoutError) as e:
            print(e)

.. autoexception:: pro_telegram.TelegramError
    :members:
    :undoc-members:
    :show-inheritance:

.. exception:: TimeoutError

    This `error <https://docs.python.org/3/library/exceptions.html#TimeoutError>`_
    is raised when a request is not returned in 5 minutes.
