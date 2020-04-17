# -*- coding:utf-8 -*-

"""Generage diff function."""

from gendiff import file
from gendiff.diff.stringify import diff_stringify
from gendiff.diff.tree import get_diff_tree


def generate(filepath1, filepath2):
    """Compare two files and generate diff string.

    Parameters:
        filepath1 (str): path to first file
        filepath2 (str): path to second file

    Returns:
        str
    """
    config1 = file.load(filepath1)
    config2 = file.load(filepath2)
    diff_tree = get_diff_tree(config1, config2)

    return diff_stringify(diff_tree)
