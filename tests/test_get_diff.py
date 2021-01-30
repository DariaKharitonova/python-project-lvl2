from gendiff.get_tree_diff import get_diff
import pytest

cases = [(
    {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    },
    {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    },
    [
        {
            'key': "follow",
            'value': False,
            'status': 'removed',
        },
        {
            'key': 'host',
            'value': 'hexlet.io',
            'status': 'unchanged',
        },
        {
            'key': 'proxy',
            'value': '123.234.53.22',
            'status': 'removed',
        },
        {
            'key': "timeout",
            'value': {
                'old': 50,
                'new': 20
            },
            'status': 'updated',
        },
        {
            'key': 'verbose',
            'value': True,
            'status': 'added',
        },
    ],
)]


@pytest.mark.parametrize("data_before, data_after, want", cases)
def test_get_diff(data_before, data_after, want):
    assert sorted(get_diff(data_before, data_after), key=lambda x: x['key']) == want
