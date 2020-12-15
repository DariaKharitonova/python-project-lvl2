from gendiff.get_tree_diff import get_diff


def est_get_diff():
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
        'description': 'get diff of two simple files'
    }]
    for v in cases:
        assert get_diff(v['file_before_json'],
                        v['file_after_json']) == v['want']
        print(v['description'])
