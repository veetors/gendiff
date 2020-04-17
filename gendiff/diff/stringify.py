# -*- coding:utf-8 -*-

"""Module with functions for transform diff tree to string."""

from gendiff.diff import constants


def normalize_value(arg):
    """Convert arg to string and transform to lower case if arg is bool.

    Parameters:
        arg (any): function argument

    Returns:
        str
    """
    if not isinstance(arg, bool):
        return str(arg)
    return str(arg).lower()


def diff_stringify(tree):
    """Transform diff object to string.

    Parameters:
        tree (obj): diff object

    Returns:
        str
    """
    output = ''

    for key, item_value in tree.items():
        if item_value[constants.TYPE] == constants.NOT_CHANGED:
            output += '    {k}: {v}\n'.format(
                k=key,
                v=normalize_value(item_value[constants.VALUE]),
            )

        if item_value[constants.TYPE] == constants.UPDATED:
            added = '  + {k}: {v}\n'.format(
                k=key,
                v=normalize_value(item_value[constants.VALUE]),
            )
            removed = '  - {k}: {v}\n'.format(
                k=key,
                v=normalize_value(item_value['prev_value']),
            )
            output += added + removed

        if item_value[constants.TYPE] == constants.REMOVED:
            output += '  - {k}: {v}\n'.format(
                k=key,
                v=normalize_value(item_value[constants.VALUE]),
            )

        if item_value[constants.TYPE] == constants.ADDED:
            output += '  + {k}: {v}\n'.format(
                k=key,
                v=normalize_value(item_value[constants.VALUE]),
            )

    return '{{\n{output}}}'.format(output=output)
