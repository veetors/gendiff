#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""
from gendiff import diff
from gendiff.parser import get_parser


def generate_diff(filepath1, filepath2):
    """Compare two files and generate diff string.

    Parameters:
        filepath1 (str): path to first file
        filepath2 (str): path to second file

    Returns:
        str
    """
    print('generate_diff')

    return diff.generate(filepath1, filepath2)


def main():
    """Run main script."""
    parser = get_parser()
    args = parser.parse_args()
    output = diff.generate(args.first_file, args.second_file)
    print(output)


if __name__ == '__main__':
    main()
