from gendiff.gendiff import generate_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format


def test_generate_diff_json():
    cases = [{
        'file_before_json': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'file_after_json': {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        },
        'want': [{
            'key': 'follow',
            'value': False,
            'status': 'removed'
        }, {
            'key': "host",
            'value': "hexlet.io",
            'status': 'unchanged'
        }, {
            'key': 'proxy',
            'value': '123.234.53.22',
            'status': 'removed'
        }, {
            'key': "timeout",
            'value': {
                'old': 50,
                'new': 20
            },
            'status': 'updated'
        }, {
            'key': 'verbose',
            'value': True,
            'status': 'added'
        }],
        'description': 'get diff of two json files'
    }]
    for v in cases:
        assert generate_diff(v['file_before_json'],
                             v['file_after_json']) == v['want']
        print(v['description'])


def test_gendiff_plain():
    cases = [{
        'file_before_json': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'file_after_json': {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        },
        'want': [
            "Property 'follow' was removed",
            "Property 'proxy' was removed",
            "Property 'timeout' was updated. From 50 to 20",
            "Property 'verbose' was added with value: true"],
        'description': 'get plain diff of two simple json files'
    }]
    for v in cases:
        result_test = '\n'.join(v['want'])
        assert plain(generate_diff(v['file_before_json'],
                                   v['file_after_json'])) == result_test
        print(v['description'])


def gendiff_json():
    cases = [{
        'file_before_json': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'file_after_json': {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        },
        'want': [
            '''
            {
                "key": "follow",
                "value": false,
                "status": "removed"
            }
            ''',
            ''' 
            "key": "host",
            "value": "hexlet.io",
            "status": "unchanged"
            ''',
            '''
            "key": "timeout",
            "value": {
              "old": 50,
              "new": 20
            },
            "status": "updated"''',
            '''
            {
                "key": "verbose",
                "value": true,
                "status": "added"
            }
            '''
        ],
        'description': 'get json-format diff of two simple json files'
    }]
    for v in cases:
        result_test = '\n'.join(v['want'])
        assert get_json_format(generate_diff(v['file_before_json'],
                                             v['file_after_json'])) == result_test
        print(v['description'])
