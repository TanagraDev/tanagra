#!/usr/bin/python
# Written for Python 2.7.10

import os

from enum import Enum

# initialize variables
cwd = os.getcwd()
metadata_path = os.path.expanduser(cwd + '/metadata.md')
outline_path = os.path.expanduser(cwd + '/outline.md')
content_path = os.path.expanduser(cwd + '/content')
output_path = os.path.expanduser(cwd + '/output')


class Command(Enum):
    FAIL = 0
    BUILD = 1
    CONVERT = 2
    COMPILE = 3
