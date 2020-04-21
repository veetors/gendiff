# -*- coding:utf-8 -*-

"""Return render function for specific format."""

import json

from gendiff.diff.constants import JSON, NESTED, PLAIN
from gendiff.diff.render import nested, plain


def get_render(output_format):
    """Return render function for specific format.

    Parameters:
        output_format (str): output format

    Returns:
        callable
    """
    renders = {
        NESTED: nested.stringify,
        PLAIN: plain.stringify,
        JSON: lambda tree: json.dumps(tree, sort_keys=True),
    }

    return renders.get(output_format, nested.stringify)
