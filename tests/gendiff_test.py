# -*- coding:utf-8 -*-

"""Generate diff tests."""

import os

import pytest

from gendiff import format, generate_diff

JSON_EXT = '.json'
YML_EXT = '.yml'


def get_fixtures_path(filename):
    """Return path to fixture.

    Parameters:
        filename (str): filename

    Returns:
        str
    """
    return os.path.join(os.getcwd(), 'tests', 'fixtures', filename)


def get_test_args(filetype, extension, output_format):
    """Generate args for test function.

    Parameters:
        filetype (str): plain or nested config
        extension (str): file extension
        output_format (str): output format

    Returns:
        tuple
    """
    filename1 = '{0}_config1{1}'.format(
        filetype,
        extension,
    )
    filename2 = '{0}_config2{1}'.format(
        filetype,
        extension,
    )
    expected_file = 'result_{0}_format_{1}{2}'.format(
        filetype,
        output_format,
        JSON_EXT if output_format == format.JSON else '',
    )

    return (
        filename1,
        filename2,
        expected_file,
        output_format,
    )


filenames = (
    get_test_args(format.PLAIN, JSON_EXT, format.NESTED),
    get_test_args(format.PLAIN, YML_EXT, format.NESTED),
    get_test_args(format.PLAIN, JSON_EXT, format.PLAIN),
    get_test_args(format.PLAIN, YML_EXT, format.PLAIN),
    get_test_args(format.NESTED, JSON_EXT, format.NESTED),
    get_test_args(format.NESTED, YML_EXT, format.NESTED),
    get_test_args(format.NESTED, JSON_EXT, format.PLAIN),
    get_test_args(format.NESTED, YML_EXT, format.PLAIN),
    get_test_args(format.NESTED, JSON_EXT, format.JSON),
    get_test_args(format.NESTED, YML_EXT, format.JSON),
)


@pytest.mark.parametrize('before, after, diff, output_format', filenames)
def test_diff(before, after, diff, output_format):
    """Check that diff generated correctly.

    Parameters:
        before (str): name of first file
        after (str): name of second file
        diff (str): name of file with expected diff
        output_format (str): output format
    """
    with open(get_fixtures_path(diff)) as result_file:
        expected = result_file.read()

    actual = generate_diff(
        get_fixtures_path(before),
        get_fixtures_path(after),
        output_format,
    )

    assert actual == expected
