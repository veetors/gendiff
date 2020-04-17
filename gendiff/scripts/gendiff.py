#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""

import argparse

from gendiff import diff


def main():
    """Run main script."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    output = diff.generate(args.first_file, args.second_file)
    print(output)


if __name__ == '__main__':
    main()
