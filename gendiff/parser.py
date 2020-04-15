# -*- coding:utf-8 -*-

"""Module with cli-arguments parser."""

import argparse


def get_parser():
    """Create parser with specific arguments.

    Returns:
        obj: parser
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser
