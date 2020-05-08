# -*- coding:utf-8 -*-

"""Module for args parser."""

import argparse

DEFAULT_OUTPUT_FORMAT = 'nested'


def get():
    """Return an argument parser.

    Returns:
        obj
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default=DEFAULT_OUTPUT_FORMAT,
        choices=['nested', 'plain', 'json'],
        help='set format of output (default: {default})'.format(
            default=DEFAULT_OUTPUT_FORMAT,
        ),
    )

    return parser
