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


def test_plain_json():
    """Check that diff generated correctly."""
    with open(get_fixtures_path('result_plain')) as result_file:
        expected = result_file.read()

    actual = generate_diff(
        get_fixtures_path('plain_config1.json'),
        get_fixtures_path('plain_config2.json'),
    )

    assert actual == expected


def test_plain_yaml():
    """Check that diff generated correctly."""
    with open(get_fixtures_path('result_plain')) as result_file:
        expected = result_file.read()

    actual = generate_diff(
        get_fixtures_path('plain_config1.yml'),
        get_fixtures_path('plain_config2.yml'),
    )

    assert actual == expected


def test_nested_json():
    """Check that diff generated correctly."""
    with open(get_fixtures_path('result_nested')) as result_file:
        expected = result_file.read()

    actual = generate_diff(
        get_fixtures_path('nested_config1.json'),
        get_fixtures_path('nested_config2.json'),
    )

    assert actual == expected


def test_nested_yaml():
    """Check that diff generated correctly."""
    with open(get_fixtures_path('result_nested')) as result_file:
        expected = result_file.read()

    actual = generate_diff(
        get_fixtures_path('nested_config1.yml'),
        get_fixtures_path('nested_config2.yml'),
    )

    assert actual == expected
