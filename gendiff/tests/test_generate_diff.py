from gendiff.get_data.get_data import get_data
from gendiff.gendiff import generate_diff


def test_get_data():
    cases = [{
        'filePath': 'gendiff/tests/fixtures/json/test1.json',
        'want': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'description': 'json file 1'
    }, {
        'filePath': 'gendiff/tests/fixtures/json/test2.json',
        'want': {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        },
        'description': 'json file 2'
    }, {
        'filePath': 'gendiff/tests/fixtures/yaml/test1.yaml',
        'want': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'description': 'yaml file 1'
    }, {
        'filePath': 'gendiff/tests/fixtures/yaml/test2.yaml',
        'want': {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        },
        'description': 'yaml file 2'
    }]
    for v in cases:
        assert get_data(v['filePath']) == v['want']
        print(v['description'])


def test_generate_diff_json():
    cases = [{
        'fileObj1': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'fileObj2': {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        },
        'want': [{
            'key': 'follow',
            'value': False,
            'status': '-'
        }, {
            'key': "host",
            'value': "hexlet.io",
            'status': ' '
        }, {
            'key': 'proxy',
            'value': '123.234.53.22',
            'status': '-'
        }, {
            'key': "timeout",
            'value': 50,
            'status': '-'
        }, {
            'key': 'timeout',
            'value': 20,
            'status': '+'
        },  {
            'key': 'verbose',
            'value': True,
            'status': '+'
        }],
        'description': 'get diff of two json files'
    }]
    for v in cases:
        assert generate_diff(v['fileObj1'], v['fileObj2']) == v['want']
        print(v['description'])


def test_generate_diff_yaml():
    cases = [{
        'fileObj1': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'fileObj2': {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        },
        'want': [{
            'key': 'follow',
            'value': False,
            'status': '-'
        }, {
            'key': "host",
            'value': "hexlet.io",
            'status': ' '
        }, {
            'key': 'proxy',
            'value': '123.234.53.22',
            'status': '-'
        }, {
            'key': "timeout",
            'value': 50,
            'status': '-'
        }, {
            'key': 'timeout',
            'value': 20,
            'status': '+'
        },  {
            'key': 'verbose',
            'value': True,
            'status': '+'
        }],
        'description': 'get diff of two json files'
    }]
    for v in cases:
        assert generate_diff(v['fileObj1'], v['fileObj2']) == v['want']
        print(v['description'])


def test_formatter():
    return True