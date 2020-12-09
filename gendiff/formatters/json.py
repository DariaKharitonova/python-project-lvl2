import json


def get_json_format(result):
    result = json.dumps(result, indent=2)
    return result.replace('[', '{').replace(']', '}')
