#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""

from gendiff import app, format

DEFAULT_OUTPUT_FORMAT = format.NESTED


def main():
    """Run main script."""
    parser = app.get_parser()
    args = parser.parse_args()
    output = app.generate(args.first_file, args.second_file, args.format)
    print(output)


if __name__ == '__main__':
    main()
