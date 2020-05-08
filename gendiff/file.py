# -*- coding:utf-8 -*-

"""Module with cli-arguments parser."""

import json
import os

import yaml

get_parser = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}.get


def load(filepath):
    """Read file and decoding to object.

    Parameters:
        filepath (str): path to file

    Returns:
        obj

    Raises:
        ValueError: file with current extension is not supported
    """
    _, extension = os.path.splitext(filepath)

    parse = get_parser(extension)

    if not parse:
        raise ValueError('File type is not supported')

    with open(filepath) as input_file:
        output = parse(input_file)

    return output
