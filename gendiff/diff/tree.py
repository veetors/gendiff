# -*- coding:utf-8 -*-

"""Module with functions for generate diff tree."""

from gendiff.diff import constants


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
            constants.TYPE: constants.NOT_CHANGED,
            constants.VALUE: config1[key],
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
            constants.TYPE: constants.UPDATED,
            constants.VALUE: config2[key],
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
            constants.TYPE: constants.REMOVED,
            constants.VALUE: config1[key],
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
            constants.TYPE: constants.ADDED,
            constants.VALUE: config2[key],
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
