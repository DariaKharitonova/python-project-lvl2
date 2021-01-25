import json


def get_json_format(diff):
    return json.dumps({'data': diff}, indent=2)
