#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""

import argparse

from gendiff import diff

DEFAULT_OUTPUT_FORMAT = 'nested'


def main():
    """Run main script."""
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
    args = parser.parse_args()
    output = diff.generate(args.first_file, args.second_file, args.format)
    print(output)


if __name__ == '__main__':
    main()
