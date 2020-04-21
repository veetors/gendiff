# -*- coding:utf-8 -*-

"""Module with functions for generate diff AST."""

from gendiff.diff.constants import (
    ADDED,
    CHILDREN,
    NOT_CHANGED,
    PREV_VALUE,
    REMOVED,
    TYPE,
    UPDATED,
    VALUE,
)


def make_removed_node(item_value):
    """Build AST-node for removed items.

    Parameters:
        item_value (any): item value

    Returns:
        dict
    """
    return {
        TYPE: REMOVED,
        VALUE: item_value,
    }


def make_added_node(item_value):
    """Build AST-node for added items.

    Parameters:
        item_value (any): item value

    Returns:
        dict
    """
    return {
        TYPE: ADDED,
        VALUE: item_value,
    }


def make_not_changed_node(item_value):
    """Build AST-node for not changed items.

    Parameters:
        item_value (any): item value

    Returns:
        dict
    """
    return {
        TYPE: NOT_CHANGED,
        VALUE: item_value,
    }


def make_updated_node(item_value1, item_value2):
    """Build AST-node for updated items.

    Parameters:
        item_value1 (any): first item value
        item_value2 (any): second item value

    Returns:
        dict
    """
    if isinstance(item_value1, dict) and isinstance(item_value2, dict):
        return {
            TYPE: UPDATED,
            CHILDREN: make_diff_tree(item_value1, item_value2),
        }
    return {
        TYPE: UPDATED,
        VALUE: item_value2,
        PREV_VALUE: item_value1,
    }


def handle_shared_items(item_value1, item_value2):
    """Build AST-node for items with are in both configs.

    Parameters:
        item_value1 (any): first item value
        item_value2 (any): second item value

    Returns:
        call function
    """
    if item_value1 == item_value2:
        return make_not_changed_node(item_value1)
    return make_updated_node(item_value1, item_value2)


def make_diff_tree(config1, config2):  # rename to make_diff_tree
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

    for key in keys1 | keys2:
        if key in keys1 & keys2:
            tree[key] = handle_shared_items(config1[key], config2[key])
        if key in keys1 - keys2:
            tree[key] = make_removed_node(config1[key])
        if key in keys2 - keys1:
            tree[key] = make_added_node(config2[key])

    return tree
