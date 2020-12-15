import json


def get_json_format(result):
    return json.dumps({'data': result}, indent=2)
