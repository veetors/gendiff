# -*- coding:utf-8 -*-

"""Module with functions for generate diff AST."""

ADDED = 'added'
NOT_CHANGED = 'not_changed'
REMOVED = 'removed'
UPDATED = 'updated'
CHILDREN = 'children'
PARENT = 'patent'
TYPE = 'type'
VALUE = 'value'
PREV_VALUE = 'prev_value'


def make_node(node_type, node_value, extra=None):  # noqa: D103
    node = {TYPE: node_type, VALUE: node_value}
    if extra:
        node.update(extra)
    return node


def compare(old, new):  # noqa: WPS210
    """Compare two configs and generate diff object.

    Parameters:
        old (obj): old structure
        new (obj): new structure

    Returns:
        dict: diff AST
    """
    tree = {}
    keys1 = old.keys()
    keys2 = new.keys()

    for removed_key in keys1 - keys2:
        tree[removed_key] = make_node(REMOVED, old[removed_key])

    for added_key in keys2 - keys1:
        tree[added_key] = make_node(ADDED, new[added_key])

    for shared_key in keys1 & keys2:
        item_value1 = old[shared_key]
        item_value2 = new[shared_key]

        if isinstance(item_value1, dict) and isinstance(item_value2, dict):
            children = compare(item_value1, item_value2)
            tree[shared_key] = make_node(PARENT, children)

        elif item_value1 == item_value2:
            tree[shared_key] = make_node(NOT_CHANGED, item_value2)

        else:
            tree[shared_key] = make_node(UPDATED, item_value2, {
                PREV_VALUE: item_value1,
            })

    return tree
