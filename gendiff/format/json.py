# -*- coding:utf-8 -*-

"""Module for transform diff tree to json."""

import json


def stringify(tree):
    """Transform AST to json.

    Parameters:
        tree (dict): AST

    Returns:
        str
    """
    return json.dumps(tree, sort_keys=True)
