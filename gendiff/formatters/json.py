import json
from gendiff.formatters.helper import reorder


def format_json(diff):
    return json.dumps({'data': reorder(diff, "key")}, indent=2)
