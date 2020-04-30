# -*- coding:utf-8 -*-

"""Transform AST to string."""

import json

from gendiff.diff.render import nested, plain

PLAIN = 'plain'
NESTED = 'nested'
JSON = 'json'

get_ = {  # noqa: WPS120
    NESTED: nested.stringify,
    PLAIN: plain.stringify,
    JSON: lambda tree: json.dumps(tree, sort_keys=True),
}.get


__all__ = (  # noqa: WPS410
    'get_',
)
