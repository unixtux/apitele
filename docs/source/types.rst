===============
Available Types
===============

All the names of the types are exactly the same described in the `offical documentation <https://core.telegram.org/bots/api#available-types>`_.

**Note**:

* Attribute *from* of the types, has been changed to *from_user* because in python it causes conflict.
* If the type :obj:`~pro_telegram.types.Message` has not *text*, the *text* it's an empty string instead of :obj:`None`, so you can do as follows without getting an `AttributeError <https://docs.python.org/3/library/exceptions.html#AttributeError>`_.

.. code-block:: python3

    import aiotgm
    from aiotgm.types import Message

    bot = aiotgm.Client('<yor_api_token>')

    @bot.manage_message()
    async def foo(msg: Message):
        if msg.text.startswith('/start'):
            ...
            # An error will never be raised
            # because the text is always of type string.

* All other optional attributes are :obj:`None` if they are not in the received *JSON*.

---------------------------

.. automodule:: pro_telegram.types
    :members:
    :undoc-members:
