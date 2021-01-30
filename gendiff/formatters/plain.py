from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, NESTED
from gendiff.formatters.format import format_json_values

COMPLEX_VALUE = '[complex value]'
ADDED_STRING = "Property {0} was added with value: {1}"
REMOVED_STRING = "Property {0} was removed"
UPDATED_STRING = "Property {0} was updated. From {1} to {2}"


def format_plain(diff):
    sorted_diff = sorted(diff, key=lambda x: x['key'])
    result_string = '\n'.join(filter(lambda x: x != '', map(lambda x: get_format(x), sorted_diff)))
    return result_string


def get_format(data, prefix=""):
    if data['status'] == NESTED:
        prefix += f'{data["key"]}.'
        value = sorted(data['value'], key=lambda x: x['key'])
        # return '\n'.join(format_string for x in value
        #                  if (format_string := get_format(x, prefix)))
        return '\n'.join(filter(lambda x: x != '', map(lambda x: get_format(x, prefix), value)))
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
    if isinstance(value, list) or isinstance(value, dict):
        return COMPLEX_VALUE
    if isinstance(value, str):
        return f'\'{value}\''
    return format_json_values(value)
