from gendiff.gendiff import generate_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format


def test_generate_diff_json():
    cases = [{
        'file_before_json': {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}
        },
        'file_after_json': {
  "common": {
    "follow": false,
    "setting1": "Value 1",
    "setting3": null,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "fee": 100500,
    "deep": {
      "id": {
        "number": 45
      }
    }
  }
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