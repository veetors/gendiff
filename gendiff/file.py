# -*- coding:utf-8 -*-

"""Module with cli-arguments parser."""

import json
import os

import yaml


def load(filepath):
    """Read file and decoding to object.

    Parameters:
        filepath (str): path to file

    Returns:
        obj
    """
    parsers = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }

    (_, extension) = os.path.splitext(filepath)
    parse = parsers[extension]

    with open(filepath) as input_file:
        output = parse(input_file)

    return output
