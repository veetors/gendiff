# -*- coding:utf-8 -*-

"""Generate diff tests."""

import os

from gendiff import generate_diff


def get_fixtures_path(filename):
    """Return path to fixture.

    Parameters:
        filename (str): filename

    Returns:
        str
    """
    return os.path.join(os.getcwd(), 'tests', 'fixtures', filename)


def test_generate_diff():
    """Check that diff generated correctly."""
    with open(get_fixtures_path('plain_json')) as result_file:
        expected = result_file.read()

    actual = generate_diff(
        get_fixtures_path('config1.json'),
        get_fixtures_path('config2.json'),
    )

    assert actual == expected
