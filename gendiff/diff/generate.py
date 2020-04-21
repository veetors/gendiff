# -*- coding:utf-8 -*-

"""Generage diff function."""

from gendiff import file
from gendiff.diff.render import get_render
from gendiff.diff.tree import make_diff_tree


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
    diff_tree = make_diff_tree(config1, config2)

    render = get_render(output_format)

    return render(diff_tree)
