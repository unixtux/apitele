#!/bin/env python3

__all__ = (
    'Client',
    'NextFunction',
    'TelegramError',
)

__version__ = '1.0.8'
VERSION = __version__

from .logging import get_logger
logger = get_logger('apitele ' + VERSION)
del get_logger

from .client import (
    Client,
    TelegramError,
)
from .update_manager import NextFunction
