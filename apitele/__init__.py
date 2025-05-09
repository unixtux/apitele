#!/bin/env python3

__all__ = (
    'Client',
    'NextFunction',
    'TelegramError',
)

__version__ = '0.0.4'
VERSION = __version__

from .logging import get_logger
logger = get_logger('aiotgm ' + VERSION)
del get_logger

from .client import (
    Client,
    TelegramError,
)
from .update_manager import NextFunction
