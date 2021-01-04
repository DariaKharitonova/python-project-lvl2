from gendiff.get_data import get_data
import pytest


cases = [
    (
        'tests/fixtures/simple/before.json',
        {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False,
            "foo": [1, 2, 3],
            "bar": ["one", "two"]
        },
    ),
    (
        'tests/fixtures/simple/after.json',
        {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io",
            "foo": [1, 2, 3],
            "bar": ["one", "two", "three"]
        }
    ),
    (
        'tests/fixtures/simple/before.yaml', {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False,
            "foo": [1, 2, 3],
            "bar": ["one", "two"]
        }
    ),
    (
        'tests/fixtures/simple/after.yaml',
        {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io",
            "foo": [1, 2, 3],
            "bar": ["one", "two", "three"]
        }
    ),
    (
        'tests/fixtures/simple/separator.test.json',
        {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        }
    )
]


@pytest.mark.parametrize("file_path, want", cases)
def test_get_data(file_path, want):
    assert get_data(file_path) == want
