# -*- coding:utf-8 -*-

"""Generate diff tests."""

import os

import pytest

from gendiff import generate_diff


def get_fixtures_path(filename):
    """Return path to fixture.

    Parameters:
        filename (str): filename

    Returns:
        str
    """
    return os.path.join(os.getcwd(), 'tests', 'fixtures', filename)


filenames = (
    ('plain_config1.json', 'plain_config2.json', 'result_plain'),
    ('plain_config1.yml', 'plain_config2.yml', 'result_plain'),
    ('nested_config1.json', 'nested_config2.json', 'result_nested'),
    ('nested_config1.yml', 'nested_config2.yml', 'result_nested'),
)


@pytest.mark.parametrize('before, after, diff', filenames)
def test_diff(before, after, diff):
    """Check that diff generated correctly.

    Parameters:
        before (str): name of first file
        after (str): name of second file
        diff (str): name of file with expected diff
    """
    with open(get_fixtures_path(diff)) as result_file:
        expected = result_file.read()

    actual = generate_diff(
        get_fixtures_path(before),
        get_fixtures_path(after),
    )

    assert actual == expected
