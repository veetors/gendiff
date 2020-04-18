# -*- coding:utf-8 -*-

"""Module with functions for transform diff tree to string."""

from gendiff.diff.constants import (
    NOT_CHANGED,
    UPDATED,
    REMOVED,
    ADDED,
    TYPE,
    VALUE,
)


def get_indent(level, correction=0):
    return ' ' * (4 * level - correction)


def get_indent_(level, correction=0):  # correction???
    return ' ' * (4 * level - 2 - correction)


def get_output(item_key, item_value, indent, sign=None):
    return '{indent}{sign} {key}: {value}\n'.format(
        indent=indent,
        sign=sign if sign else ' ',
        key=item_key,
        value=item_value,
    )


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


def stringify_obj(target_obj, level=1):
    output = ''
    for item_key, item_value in target_obj.items():
        if isinstance(item_value, dict):
            output += stringify_obj(item_value, level + 1)
        else:
            output += get_output(
                item_key=item_key,
                item_value=normalize_value(item_value),
                indent=get_indent_(level),
            )
            # output += '{spaces}{key}: {value}\n'.format(
            #     spaces=get_indent(level),
            #     key=key,
            #     value=normalize_value(item_value),
            # )
    return '{{\n{output}{spaces}}}'.format(
        output=output,
        spaces=get_indent(level - 1),
    )


def build_value(item_value, level):
    if isinstance(item_value, dict):
        return stringify_obj(item_value, level)
    return normalize_value(item_value)


def make_not_changed_item(item_key, item_value, level):
    return get_output(
        item_key=item_key,
        item_value=build_value(item_value[VALUE], level + 1),
        indent=get_indent_(level),
    )
    # return '{spaces}{key}: {value}\n'.format(
    #     spaces=get_indent(level),
    #     key=item_key,
    #     value=build_value(item_value[VALUE], level + 1),
    # )


def make_updated_item(item_key, item_value, level):
    if 'children' in item_value:
        return get_output(
            item_key=item_key,
            item_value=diff_stringify(item_value['children'], level + 1),
            indent=get_indent_(level),
        )
        # return '{spaces}{key}: {value}\n'.format(
        #     spaces=get_indent(level),
        #     key=item_key,
        #     value=diff_stringify(item_value['children'], level + 1)
        # )

    added = get_output(
        item_key=item_key,
        item_value=build_value(item_value[VALUE], level + 1),
        indent=get_indent_(level),
        sign='+',
    )
    # added = '{spaces}+ {key}: {value}\n'.format(
    #     spaces=get_indent(level, 2),
    #     key=item_key,
    #     value=build_value(item_value[VALUE], level + 1),
    # )
    removed = get_output(
        item_key=item_key,
        item_value=build_value(item_value['prev_value'], level + 1),
        indent=get_indent_(level),
        sign='-',
    )
    # removed = '{spaces}- {key}: {value}\n'.format(
    #     spaces=get_indent(level, 2),
    #     key=item_key,
    #     value=build_value(item_value['prev_value'], level + 1),
    # )
    return added + removed


def make_removed_item(item_key, item_value, level):
    return get_output(
        item_key=item_key,
        item_value=build_value(item_value[VALUE], level + 1),
        indent=get_indent_(level),
        sign='-',
    )
    # return '{spaces}- {key}: {value}\n'.format(
    #     spaces=get_indent(level, 2),
    #     key=item_key,
    #     value=build_value(item_value[VALUE], level + 1),
    # )


def make_added_item(item_key, item_value, level):
    return get_output(
        item_key=item_key,
        item_value=build_value(item_value[VALUE], level + 1),
        indent=get_indent_(level),
        sign='+',
    )
    # return '{spaces}+ {key}: {value}\n'.format(
    #     spaces=get_indent(level, 2),
    #     key=item_key,
    #     value=build_value(item_value[VALUE], level + 1),
    # )


items_actions = {
    NOT_CHANGED: make_not_changed_item,
    UPDATED: make_updated_item,
    REMOVED: make_removed_item,
    ADDED: make_added_item,
}


def diff_stringify(tree, level=1):
    output = ''
    keys = list(tree.keys())
    keys.sort()

    for key in keys:
        item_value = tree[key]

        make_item_func = items_actions[item_value[TYPE]]
        output += make_item_func(key, item_value, level)

    return '{{\n{output}{s}}}'.format(
        s=get_indent(level - 1),
        output=output,
    )
