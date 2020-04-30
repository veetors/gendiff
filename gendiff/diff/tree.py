# -*- coding:utf-8 -*-

"""Module with functions for generate diff AST."""

from gendiff import diff


def make_removed_node(item_value):  # noqa: D103
    return {
        diff.TYPE: diff.REMOVED,
        diff.VALUE: item_value,
    }


def make_added_node(item_value):  # noqa: D103
    return {
        diff.TYPE: diff.ADDED,
        diff.VALUE: item_value,
    }


def make_parent_node(item_value1, item_value2):  # noqa: D103
    return {
        diff.TYPE: diff.PARENT,
        diff.CHILDREN: make_diff(item_value1, item_value2),
    }


def make_not_changed_node(item_value):  # noqa: D103
    return {
        diff.TYPE: diff.NOT_CHANGED,
        diff.VALUE: item_value,
    }


def make_updated_node(item_value1, item_value2):  # noqa: D103
    return {
        diff.TYPE: diff.UPDATED,
        diff.VALUE: item_value2,
        diff.PREV_VALUE: item_value1,
    }


def make_diff(config1, config2):  # noqa: WPS210
    """Compare two configs and generate diff object.

    Parameters:
        config1 (obj): first config
        config2 (obj): second config

    Returns:
        dict: diff AST
    """
    tree = {}
    keys1 = set(config1.keys())
    keys2 = set(config2.keys())

    for removed_key in keys1 - keys2:
        tree[removed_key] = make_removed_node(config1.get(removed_key))

    for added_key in keys2 - keys1:
        tree[added_key] = make_added_node(config2.get(added_key))

    for shared_key in keys1 & keys2:
        item_value1 = config1.get(shared_key)
        item_value2 = config2.get(shared_key)

        if isinstance(item_value1, dict) and isinstance(item_value2, dict):
            tree[shared_key] = make_parent_node(item_value1, item_value2)
        elif item_value1 == item_value2:
            tree[shared_key] = make_not_changed_node(item_value2)
        else:
            tree[shared_key] = make_updated_node(item_value1, item_value2)

    return tree
