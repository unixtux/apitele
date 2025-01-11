#!/bin/env python3

__all__ = (
    'get_logger',
)

import logging

def get_logger(name: str, /) -> logging.Logger:
    '''
    Function to get a preformatted Logger instance.
    If the Logger already exists, level won't
    be set, otherwise it is logging.INFO.
    '''
    if name in logging.Logger.manager.loggerDict:
        return logging.getLogger(name)
    else:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            fmt='%(asctime)s %(name)s [%(levelname)s] %(message)s',
            datefmt='%H:%M.%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
