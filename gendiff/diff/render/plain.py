# -*- coding:utf-8 -*-

"""Module with functions for transform diff tree to string."""

from gendiff.diff import tree


def stringify_updated_node(node_key, node_value, ancestors):  # noqa: D103
    return (
        "Property '{key}' was changed. "
        "From '{prev_value}' to '{value}'\n"  # noqa: WPS326
    ).format(
        key='.'.join([*ancestors, node_key]),
        prev_value=node_value[tree.PREV_VALUE],
        value=node_value[tree.VALUE],
    )


def stringify_removed_node(node_key, node_value, ancestors):  # noqa: D103
    return "Property '{key}' was removed\n".format(
        key='.'.join([*ancestors, node_key]),
    )


def stringify_added_node(node_key, node_value, ancestors):  # noqa: D103
    result_key = '.'.join([*ancestors, node_key])
    if isinstance(node_value[tree.VALUE], dict):
        result_value = 'complex_value'
    else:
        result_value = node_value[tree.VALUE]

    return "Property '{key}' was added with value: '{value}'\n".format(
        key=result_key,
        value=result_value,
    )


def stringify_parent_node(node_key, node_value, ancestors):  # noqa: D103
    return stringify_tree(
        node_value[tree.VALUE],
        [*ancestors, node_key],
    )


def stringify_tree(diff_tree, ancestors):  # noqa: WPS231
    """Transform AST to string.

    Parameters:
        diff_tree (dict): AST
        ancestors (list): ancestors keys

    Returns:
        str
    """
    output = ''

    for node_key, node_value in sorted(diff_tree.items()):
        node_type = node_value[tree.TYPE]

        if node_type == tree.REMOVED:
            output += stringify_removed_node(node_key, node_value, ancestors)
        elif node_type == tree.ADDED:
            output += stringify_added_node(node_key, node_value, ancestors)
        elif node_type == tree.PARENT:
            output += stringify_parent_node(node_key, node_value, ancestors)
        elif node_type == tree.UPDATED:
            output += stringify_updated_node(node_key, node_value, ancestors)

    return'{output}'.format(output=output)


def stringify(diff_tree):
    """Transform AST to string and trimm last symbol.

    Parameters:
        diff_tree (dict): AST

    Returns:
        str
    """
    output = stringify_tree(diff_tree, [])
    return output[:-1]
