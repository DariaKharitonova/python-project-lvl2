import json


def format_json(diff):
    return json.dumps({'data': diff}, indent=2)
