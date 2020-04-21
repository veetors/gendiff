# -*- coding:utf-8 -*-

"""Functions for build specific string representation."""

from gendiff.diff.common import build_output, get_indent


def normalize_value(arg):
    """Convert arg to string and transform to lower case if arg is bool.

    Parameters:
        arg (any): function argument

    Returns:
        str
    """
    if isinstance(arg, bool):
        return str(arg).lower()
    return str(arg)


def stringify_dict(target_dict, depth):
    """Build string representations for dict.

    Parameters:
        target_dict (dict): dict to transform
        depth (int): element nesting level

    Returns:
        str
    """
    output = ''
    for item_key, item_value in target_dict.items():
        if isinstance(item_value, dict):
            output += stringify_dict(item_value, depth + 1)
        else:
            output += build_output(
                item_key=item_key,
                item_value=normalize_value(item_value),
                indent=get_indent(depth),
            )
    return '{{\n{output}{spaces}}}'.format(
        output=output,
        spaces=get_indent(depth - 1, 2),
    )


def build(item_value, depth):
    """Build specific string representation for value.

    Parameters:
        item_value (any): value to transform
        depth (int): element nesting level

    Returns:
        call function
    """
    if isinstance(item_value, dict):
        return stringify_dict(item_value, depth)
    return normalize_value(item_value)
