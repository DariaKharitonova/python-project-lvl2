from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, UNCHANGED
from gendiff.helpers.format import format_json_values

COMPLEX_VALUE = '[complex value]'
ADDED_STRING = "Property {0} was added with value: {1}\n"
REMOVED_STRING = "Property {0} was removed\n"
UPDATED_STRING = "Property {0} was updated. From {1} to {2}\n"


def plain(result):
    result_string = ''.join(get_format(x) for x in result)
    return result_string.rstrip()


def get_format(data, prefix=""):
    if isinstance(data['value'], list) and data['status'] == UNCHANGED:
        prefix += f'{data["key"]}.'
        return ''.join(get_format(x, prefix) for x in data['value'])
    return get_string(data, prefix)


def get_string(data, prefix):
    key = f'\'{prefix}{data["key"]}\''

    if data["status"] == ADDED:
        return ADDED_STRING.format(key, get_value(data["value"]))
    elif data["status"] == REMOVED:
        return REMOVED_STRING.format(key)
    elif data["status"] == UPDATED:
        return UPDATED_STRING.format(key,
                                     get_value(data["value"]["old"]),
                                     get_value(data["value"]["new"]))
    else:
        return ''


def get_value(value):
    if isinstance(value, list):
        return COMPLEX_VALUE
    if isinstance(value, str):
        return f'\'{value}\''
    return format_json_values(value)
