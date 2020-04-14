#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""

import argparse
import json

NOT_CHANGED = 'not_changed'
UPDATED = 'updated'
REMOVED = 'removed'
ADDED = 'added'
TYPE = 'type'
VALUE = 'value'


def get_parser():
    """Create parser with specific arguments.

    Returns:
        obj: parser
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    print(type(parser))

    return parser


def get_diff_tree(config1, config2):
    """Compare two configs and generate diff object.

    Parameters:
        config1 (obj): first config
        config2 (obj): second config

    Returns:
        obj
    """
    united_keys = [*config1.keys(), *config2.keys()]
    uniq_kyes = set(united_keys)

    diff_tree = {}

    for key in uniq_kyes:
        if key in config1 and key in config2:
            if config1[key] == config2[key]:
                diff_tree[key] = {
                    TYPE: NOT_CHANGED,
                    VALUE: config1[key],
                }
            else:
                diff_tree[key] = {
                    TYPE: UPDATED,
                    VALUE: config2[key],
                    'prev_value': config1[key],
                }
        if key in config1 and key not in config2:
            diff_tree[key] = {
                TYPE: REMOVED,
                VALUE: config1[key],
            }
        if key not in config1 and key in config2:
            diff_tree[key] = {
                TYPE: ADDED,
                VALUE: config2[key],
            }

    return diff_tree


def diff_stringify(tree):
    """Transform diff object to string.

    Parameters:
        tree (obj): diff object

    Returns:
        str
    """
    output = ''

    for key, item_value in tree.items():
        if item_value[TYPE] == NOT_CHANGED:
            output += '    {k}: {v}\n'.format(k=key, v=item_value[VALUE])
        if item_value[TYPE] == UPDATED:
            added = '  + {k}: {v}\n'.format(k=key, v=item_value[VALUE])
            removed = '  - {k}: {v}\n'.format(k=key, v=item_value['prev_value'])
            output += added + removed
        if item_value[TYPE] == REMOVED:
            output += '  - {k}: {v}\n'.format(k=key, v=item_value[VALUE])
        if item_value[TYPE] == ADDED:
            output += '  + {k}: {v}\n'.format(k=key, v=item_value[VALUE])

    return '{{\n{output}}}'.format(output=output)


def generate_diff(filepath1, filepath2):
    """Compare two files and generate diff string.

    Parameters:
        filepath1 (str): path to first file
        filepath2 (str): path to second file

    Returns:
        str
    """
    with open(filepath1) as input_file1:
        config1 = json.load(input_file1)

    with open(filepath2) as input_file2:
        config2 = json.load(input_file2)

    diff_tree = get_diff_tree(config1, config2)

    return diff_stringify(diff_tree)


def main():
    """Run main script."""
    parser = get_parser()
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
