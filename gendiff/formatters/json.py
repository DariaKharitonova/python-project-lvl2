import json
from gendiff.formatters.sort_diff_keys import sort_keys


def format_json(diff):
    return json.dumps({'data': sort_keys(diff)}, indent=2)
