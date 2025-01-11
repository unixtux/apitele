#!/bin/env python3

__all__ = (
    'escape_markdown',
    'seconds_to_next_hour',
)

MARKDOWN_ESCAPES = {
    '_': '\_',
    '*': '\*',
    '[': '\[',
    ']': '\]',
    '(': '\(',
    ')': '\)',
    '~': '\~',
    '`': '\`',
    '>': '\>',
    '#': '\#',
    '+': '\+',
    '-': '\-',
    '=': '\=',
    '|': '\|',
    '{': '\{',
    '}': '\}',
    '.': '\.',
    '!': '\!',
    '\\': '\\\\'
}

def escape_markdown(text) -> str:
    return str(text).translate(str.maketrans(MARKDOWN_ESCAPES))

def seconds_to_next_hour() -> float:
    from datetime import datetime
    now = datetime.now()
    return 3600 - (now.minute * 60 + now.second)
