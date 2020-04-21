# -*- coding:utf-8 -*-

"""Module with functions for transform diff tree to string."""

from gendiff.diff import value
from gendiff.diff.common import build_output, get_indent
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


def stringify_not_changed_node(node_key, node_value, depth):
    """Build string representation for not changed AST-node.

    Parameters:
        node_key (any): node key
        node_value (dict): node value
        depth (int): node nesting level

    Returns:
        str
    """
    return build_output(
        item_key=node_key,
        item_value=value.build(node_value[VALUE], depth + 1),
        indent=get_indent(depth),
    )


def stringify_updated_node(node_key, node_value, depth):
    """Build string representation for updated AST-node.

    Parameters:
        node_key (any): node key
        node_value (dict): node value
        depth (int): node nesting level

    Returns:
        str
    """
    if 'children' in node_value:
        return build_output(
            item_key=node_key,
            item_value=stringify(node_value.get(CHILDREN), depth + 1),
            indent=get_indent(depth),
        )

    added = build_output(
        item_key=node_key,
        item_value=value.build(node_value[VALUE], depth + 1),
        indent=get_indent(depth),
        sign='+',
    )
    removed = build_output(
        item_key=node_key,
        item_value=value.build(node_value[PREV_VALUE], depth + 1),
        indent=get_indent(depth),
        sign='-',
    )

    return added + removed


def stringify_removed_node(node_key, node_value, depth):
    """Build string representation for removed AST-node.

    Parameters:
        node_key (any): node key
        node_value (dict): node value
        depth (int): node nesting level

    Returns:
        str
    """
    return build_output(
        item_key=node_key,
        item_value=value.build(node_value[VALUE], depth + 1),
        indent=get_indent(depth),
        sign='-',
    )


def stringify_added_node(node_key, node_value, depth):
    """Build string representation for added AST-node.

    Parameters:
        node_key (any): node key
        node_value (dict): node value
        depth (int): node nesting level

    Returns:
        str
    """
    return build_output(
        item_key=node_key,
        item_value=value.build(node_value[VALUE], depth + 1),
        indent=get_indent(depth),
        sign='+',
    )


stringify_node_funcs = {
    NOT_CHANGED: stringify_not_changed_node,
    UPDATED: stringify_updated_node,
    REMOVED: stringify_removed_node,
    ADDED: stringify_added_node,
}


def stringify(tree, depth=1):
    """Transform AST to string.

    Parameters:
        tree (dict): AST
        depth (int): nesting level

    Returns:
        str
    """
    output = ''
    nodes = list(tree.items())
    nodes.sort()

    for node_key, node_value in nodes:
        stringify_node = stringify_node_funcs[node_value[TYPE]]
        output += stringify_node(node_key, node_value, depth)

    return '{{\n{output}{s}}}'.format(
        s=get_indent(depth - 1, 2),
        output=output,
    )
