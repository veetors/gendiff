# -*- coding:utf-8 -*-

"""Module with functions for transform diff tree to string."""

from gendiff import diff


def get_indent(depth, extra_indent=0):
    """Return specific indent.

    Parameters:
        depth (int): element nesting level
        extra_indent (int): extra indent

    Returns:
        str
    """
    return ' ' * (4 * depth - 2 + extra_indent)


def stringify_dict(target_dict, depth):
    """Build string representations for dict.

    Parameters:
        target_dict (dict): dict to transform
        depth (int): element nesting level

    Returns:
        str
    """
    output_parts = []
    for item_key, item_value in target_dict.items():
        output_parts.append('{indent}  {key}: {value}\n'.format(
            indent=(get_indent(depth)),
            key=item_key,
            value=item_value,
        ))

    return '{{\n{output}{spaces}}}'.format(
        output=''.join(output_parts),
        spaces=get_indent(depth - 1, 2),
    )


def build_value(item_value, depth):
    """Build specific string representation for value.

    Parameters:
        item_value (any): value to transform
        depth (int): element nesting level

    Returns:
        call function
    """
    if isinstance(item_value, dict):
        return stringify_dict(item_value, depth)
    elif isinstance(item_value, bool):
        return str(item_value).lower()
    return str(item_value)


def stringify(tree, depth=1):  # noqa: C901 WPS210 WPS231k
    """Transform AST to string.

    Parameters:
        tree (dict): AST
        depth (int): nesting level

    Returns:
        str
    """
    output_parts = []

    for node_key, node_value in sorted(tree.items()):
        node_type = node_value.get(diff.TYPE)
        processed_value = build_value(node_value.get(diff.VALUE), depth + 1)

        if node_type == diff.REMOVED:  # noqa: WPS223
            output_data = [('-', processed_value)]
        elif node_type == diff.ADDED:
            output_data = [('+', processed_value)]
        elif node_type == diff.NOT_CHANGED:
            output_data = [(' ', processed_value)]
        elif node_type == diff.PARENT:
            output_data = [
                (' ', stringify(node_value.get(diff.CHILDREN), depth + 1)),
            ]
        elif node_type == diff.UPDATED:
            output_data = [
                ('+', processed_value),
                ('-', build_value(node_value.get(diff.PREV_VALUE), depth + 1)),
            ]

        for sign, output_value in output_data:
            output_parts.append(
                '{indent}{sign} {key}: {value}\n'.format(
                    indent=get_indent(depth),
                    sign=sign,
                    key=node_key,
                    value=output_value,
                ),
            )

    return '{{\n{output}{s}}}'.format(
        s=get_indent(depth - 1, 2),
        output=''.join(output_parts),
    )
