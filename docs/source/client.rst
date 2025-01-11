================
Client Reference
================

This page refers to the :obj:`~pro-telegram.Client` and all its methods, which are the same described in the
`official documentation <https://core.telegram.org/bots/api#available-methods>`_, changed from camelCase to snake_case.
E.g. *sendMessage* becomes *send_message*.

They are all *asynchronous*, so you must use them in `await <https://docs.python.org/3/library/asyncio-task.html#awaitables>`_ expression.

Note: Webhook has not been implemented yet.

----------------------------------

.. autoclass:: pro-telegram.Client
    :members:
    :undoc-members:
