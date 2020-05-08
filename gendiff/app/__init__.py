# -*- coding:utf-8 -*-

"""Package with functions for generate diff."""

from gendiff import diff, format
from gendiff.app import file


def generate(filepath1, filepath2, output_format=format.NESTED):
    """Compare two files and generate diff string.

    Parameters:
        filepath1 (str): path to first file
        filepath2 (str): path to second file
        output_format (str): output format

    Returns:
        str
    """
    tree1 = file.load(filepath1)
    tree2 = file.load(filepath2)
    diff_tree = diff.compare(tree1, tree2)

    stringify = format.get(output_format)

    return stringify(diff_tree)


__all__ = (  # noqa: WPS410
    'get_parser',
    'generate',
)
