#!/bin/env python3

if __name__ != '__main__':
    raise RuntimeError()

import re
with open('pyproject.toml') as r:
    version = re.search(r'^version\s*=\s*"(.*?)"', r.read(), re.MULTILINE)
    if not version:
        raise ValueError('No version found in pyproject.toml')

VERSION = version.group(1)

with open('pro-telegram/__init__.py') as r:
    PROJECT_CONTENT = r.readlines()

lines = ''
for line in PROJECT_CONTENT:
    version = re.match(r"__version__\s*=\s*'(.*?)'", line)
    if version:
        if version.group(1) == VERSION:
            import sys
            print('Versions are the same.', VERSION)
            sys.exit(0)
        line = "__version__ = '{}'\n".format(VERSION)
    lines += line # add line to all the lines for the final file

with open('pro-telegram/__init__.py', 'w') as w:
    w.write(lines)

print('Version updated to', VERSION)
