# -*- coding:utf-8 -*-

"""Common diff functions."""


def get_indent(depth, extra_indent=0):
    """Return specific indent.

    Parameters:
        depth (int): element nesting level
        extra_indent (int): extra indent

    Returns:
        str
    """
    return ' ' * (4 * depth - 2 + extra_indent)


def build_output(item_key, item_value, indent, sign=None):
    """Build specific string.

    Parameters:
        item_key (any): item key
        item_value (str): item value
        indent (str): indent
        sign (str): specific sign

    Returns:
        str
    """
    return '{indent}{sign} {key}: {value}\n'.format(
        indent=indent,
        sign=sign if sign else ' ',
        key=item_key,
        value=item_value,
    )
