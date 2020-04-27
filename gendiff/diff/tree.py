# -*- coding:utf-8 -*-

"""Module with functions for generate diff AST."""

from gendiff.diff.constants import (
    ADDED,
    CHILDREN,
    NOT_CHANGED,
    PARENT,
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
    return {
        TYPE: UPDATED,
        VALUE: item_value2,
        PREV_VALUE: item_value1,
    }


def make_parent_node(item_value1, item_value2):
    """Build AST-node for items that have child items.

    Parameters:
        item_value1 (any): first item value
        item_value2 (any): second item value

    Returns:
        dict
    """
    return {
        TYPE: PARENT,
        CHILDREN: make_diff_tree(item_value1, item_value2),
    }


def make_diff_tree(config1, config2):
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
            if config1[key] == config2[key]:
                tree[key] = make_not_changed_node(config1[key])
            else:
                tree[key] = make_updated_node(config1[key], config2[key])

            if isinstance(config1[key], dict) and isinstance(config2[key], dict):
                tree[key] = make_parent_node(config1[key], config2[key])

        if key in keys1 - keys2:
            tree[key] = make_removed_node(config1[key])

        if key in keys2 - keys1:
            tree[key] = make_added_node(config2[key])

    return tree
