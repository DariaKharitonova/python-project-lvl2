from gendiff.gendiff import generate_diff


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


def test_generate_diff_yaml():
    cases = [{
        'file_before_yaml': {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        'file_after_yaml': {
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
        'description': 'get diff of two simple yaml files'
    }]
    for v in cases:
        assert generate_diff(v['file_before_yaml'],
                             v['file_after_yaml']) == v['want']
        print(v['description'])
