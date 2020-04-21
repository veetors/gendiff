# -*- coding:utf-8 -*-

"""Module with functions for transform diff tree to string."""

from gendiff.diff.constants import (
    ADDED,
    CHILDREN,
    PREV_VALUE,
    REMOVED,
    TYPE,
    UPDATED,
    VALUE,
)


def stringify_updated_node(node_key, node_value, ancestors):
    """Build string representation for updated AST-node.

    Parameters:
        node_key (any): node key
        node_value (dict): node value
        ancestors (list): ancestors keys

    Returns:
        str
    """
    if 'children' in node_value:
        return stringify_tree(
            node_value.get(CHILDREN),
            [*ancestors, node_key],
        )

    return (
        "Property '{key}' was changed. "
        "From '{prev_value}' to '{value}'\n"  # noqa WPS326
    ).format(
        key='.'.join([*ancestors, node_key]),
        prev_value=node_value.get(PREV_VALUE),
        value=node_value.get(VALUE),
    )


def stringify_removed_node(node_key, node_value, ancestors):
    """Build string representation for removed AST-node.

    Parameters:
        node_key (any): node key
        node_value (dict): node value
        ancestors (list): ancestors keys

    Returns:
        str
    """
    return "Property '{key}' was removed\n".format(
        key='.'.join([*ancestors, node_key]),
    )


def stringify_added_node(node_key, node_value, ancestors):
    """Build string representation for added AST-node.

    Parameters:
        node_key (any): node key
        node_value (dict): node value
        ancestors (list): ancestors keys

    Returns:
        str
    """
    result_key = '.'.join([*ancestors, node_key])
    if isinstance(node_value.get(VALUE), dict):
        result_value = 'complex_value'
    else:
        result_value = node_value.get(VALUE)

    return "Property '{key}' was added with value: '{value}'\n".format(
        key=result_key,
        value=result_value,
    )


stringify_node_funcs = {
    UPDATED: stringify_updated_node,
    REMOVED: stringify_removed_node,
    ADDED: stringify_added_node,
}


def stringify_tree(tree, ancestors):
    """Transform AST to string.

    Parameters:
        tree (dict): AST
        ancestors (list): ancestors keys

    Returns:
        str
    """
    output = ''
    nodes = list(tree.items())
    nodes.sort()

    for node_key, node_value in nodes:
        if node_value.get(TYPE) not in stringify_node_funcs:
            continue
        stringify_node = stringify_node_funcs[node_value[TYPE]]
        output += stringify_node(node_key, node_value, ancestors)

    return'{output}'.format(output=output)


def stringify(tree):
    """Transform AST to string and trimm last symbol.

    Parameters:
        tree (dict): AST

    Returns:
        str
    """
    output = stringify_tree(tree, [])
    return output[:-1]
