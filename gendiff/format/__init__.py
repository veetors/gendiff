# -*- coding:utf-8 -*-

"""Transform AST to string."""

from gendiff.format import json, nested, plain

JSON, NESTED, PLAIN = ('json', 'nested', 'plain')

get = {
    NESTED: nested.stringify,
    PLAIN: plain.stringify,
    JSON: json.stringify,
}.get


__all__ = (  # noqa: WPS410
    'get',
)
