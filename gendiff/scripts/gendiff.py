#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""

import argparse


def main():
    """Run main script."""

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()


if __name__ == '__main__':
    main()
