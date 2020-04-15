# -*- coding:utf-8 -*-

"""Generate diff functions."""

import json

NOT_CHANGED = 'not_changed'
UPDATED = 'updated'
REMOVED = 'removed'
ADDED = 'added'
TYPE = 'type'
VALUE = 'value'


def get_not_changed_items(config1, config2):
    """Compare two configs and generate diff for not changed keys.

    Parameters:
        config1 (obj): first config
        config2 (obj): second config

    Returns:
        obj
    """
    keys1 = set(config1.keys())
    keys2 = set(config2.keys())
    not_changed_items = {}
    for key in keys1 & keys2:
        if config1[key] != config2[key]:
            continue
        not_changed_items[key] = {
            TYPE: NOT_CHANGED,
            VALUE: config1[key],
        }
    return not_changed_items


def get_updated_items(config1, config2):
    """Compare two configs and generate diff for updated keys.

    Parameters:
        config1 (obj): first config
        config2 (obj): second config

    Returns:
        obj
    """
    keys1 = set(config1.keys())
    keys2 = set(config2.keys())
    updated_items = {}
    for key in keys1 & keys2:
        if config1[key] == config2[key]:
            continue
        updated_items[key] = {
            TYPE: UPDATED,
            VALUE: config2[key],
            'prev_value': config1[key],
        }
    return updated_items


def get_removed_items(config1, config2):
    """Compare two configs and generate diff for removed keys.

    Parameters:
        config1 (obj): first config
        config2 (obj): second config

    Returns:
        obj
    """
    keys1 = set(config1.keys())
    keys2 = set(config2.keys())
    removed_items = {}
    for key in keys1 - keys2:
        removed_items[key] = {
            TYPE: REMOVED,
            VALUE: config1[key],
        }
    return removed_items


def get_added_itmes(config1, config2):
    """Compare two configs and generate diff for added keys.

    Parameters:
        config1 (obj): first config
        config2 (obj): second config

    Returns:
        obj
    """
    keys1 = set(config1.keys())
    keys2 = set(config2.keys())
    added_items = {}
    for key in keys2 - keys1:
        added_items[key] = {
            TYPE: ADDED,
            VALUE: config2[key],
        }
    return added_items


def get_diff_tree(config1, config2):
    """Compare two configs and generate diff object.

    Parameters:
        config1 (obj): first config
        config2 (obj): second config

    Returns:
        obj
    """
    return {
        **get_not_changed_items(config1, config2),
        **get_updated_items(config1, config2),
        **get_removed_items(config1, config2),
        **get_added_itmes(config1, config2),
    }


def diff_stringify(tree):
    """Transform diff object to string.

    Parameters:
        tree (obj): diff object

    Returns:
        str
    """
    output = ''

    for key, item_value in tree.items():
        if item_value[TYPE] == NOT_CHANGED:
            output += '    {k}: {v}\n'.format(k=key, v=item_value[VALUE])

        if item_value[TYPE] == UPDATED:
            added = '  + {k}: {v}\n'.format(k=key, v=item_value[VALUE])
            removed = '  - {k}: {v}\n'.format(k=key, v=item_value['prev_value'])
            output += added + removed

        if item_value[TYPE] == REMOVED:
            output += '  - {k}: {v}\n'.format(k=key, v=item_value[VALUE])

        if item_value[TYPE] == ADDED:
            output += '  + {k}: {v}\n'.format(k=key, v=item_value[VALUE])

    return '{{\n{output}}}'.format(output=output)


def generate(filepath1, filepath2):
    """Compare two files and generate diff string.

    Parameters:
        filepath1 (str): path to first file
        filepath2 (str): path to second file

    Returns:
        str
    """
    with open(filepath1) as input_file1:
        config1 = json.load(input_file1)

    with open(filepath2) as input_file2:
        config2 = json.load(input_file2)

    diff_tree = get_diff_tree(config1, config2)

    return diff_stringify(diff_tree)
