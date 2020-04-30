# -*- coding:utf-8 -*-

"""Package with functions for generate diff."""

from gendiff import file
from gendiff.diff import render, tree

ADDED = 'added'
NOT_CHANGED = 'not_changed'
REMOVED = 'removed'
UPDATED = 'updated'
CHILDREN = 'children'
PARENT = 'patent'
TYPE = 'type'
VALUE = 'value'
PREV_VALUE = 'prev_value'


def generate(filepath1, filepath2, output_format='nested'):
    """Compare two files and generate diff string.

    Parameters:
        filepath1 (str): path to first file
        filepath2 (str): path to second file
        output_format (str): output format

    Returns:
        str
    """
    config1 = file.load(filepath1)
    config2 = file.load(filepath2)
    diff_tree = tree.make_diff(config1, config2)

    stringify = render.get_(output_format)

    return stringify(diff_tree)


__all__ = (  # noqa: WPS410
    'generate',
)
