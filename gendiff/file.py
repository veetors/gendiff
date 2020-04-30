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

    Raises:
        NameError: file with current extension is not supported
    """
    get_parser = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get

    (_, extension) = os.path.splitext(filepath)

    parse = get_parser(extension)

    if not parse:
        raise NameError('File type is not supported')

    with open(filepath) as input_file:
        output = parse(input_file)

    return output
