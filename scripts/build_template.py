#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import re
import shutil
import json

from os import path
from datetime import datetime


DEFAULT_BOOK_NAME = 'new_book_' + datetime.today().strftime('%Y%m%d-%H%M%S')

# initialize variables
book_name = None
book_dir = None


def build_template():
    global book_name
    global book_dir

    print(book_name)
    print(book_dir)
    book_path = book_dir + '/' + book_name

    try:
        if not os.path.exists(book_path):
            os.makedirs(book_path)
    except OSError:
        sys.exit('Output directory "' + book_path +
                 '" does not exist and cannot be created')


def build_template_init(p_book_name, p_book_dir):
    global book_name
    global book_dir

    book_name = p_book_name
    book_dir = p_book_dir

    book_name = cleanup_book_name(book_name)


def build_template_prompt():
    global book_name
    global book_dir

    print(DEFAULT_BOOK_NAME)

    print('What is a short name for your book project? This is not your title. [' +
          DEFAULT_BOOK_NAME + ']')
    book_name = str(raw_input())

    if not book_name:
        book_name = DEFAULT_BOOK_NAME

    book_name = cleanup_book_name(book_name)

    cwd = os.getcwd()
    print(
        'Where would you like to create your book project? [' + cwd + '/]')
    book_dir = os.path.expanduser(raw_input())
    if not book_dir:
        book_dir = cwd
    elif not os.path.isdir(book_dir):
        print('Book directory is invalid.')
        exit(1)


def cleanup_book_name(book_name):
    # make book_name a machine name string for directories
    book_name = book_name.lower().replace(' ', '_')
    book_name = re.sub('[^A-Za-z0-9_]+', '', book_name)

    return book_name


def main():
    global book_name
    global book_dir
    # print('Number of arguments:' + str(len(sys.argv)) + 'arguments.')
    # print('Argument List:' + str(sys.argv))

    # cwd = os.getcwd()
    # print('Current directory ' + cwd)

    # check for arguments or ask for input
    if len(sys.argv) == 3:
        book_name = str(sys.argv[1])
        book_dir = str(sys.argv[2])
    else:
        build_template_prompt()

    build_template()


if __name__ == "__main__":
    main()
