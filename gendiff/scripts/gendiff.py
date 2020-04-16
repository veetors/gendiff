#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""
from gendiff import diff
from gendiff.parser import get_parser


def main():
    """Run main script."""
    parser = get_parser()
    args = parser.parse_args()
    output = diff.generate(args.first_file, args.second_file)
    print(output)


if __name__ == '__main__':
    main()
