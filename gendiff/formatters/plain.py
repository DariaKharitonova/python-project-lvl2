from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, UNCHANGED
from gendiff.helpers.format import format_json_values


def plain(result):
    result_string = ''.join(get_format(x) for x in result)
    return result_string.rstrip()


def get_format(data, prefix=""):
    if isinstance(data['value'], list) and data['status'] == UNCHANGED:
        prefix += f'{data["key"]}.'
        return ''.join(get_format(x, prefix) for x in data['value'])
    return get_string(data, prefix)


def get_value(value):
    if isinstance(value, list):
        return '[complex value]'
    if isinstance(value, str):
        return f'\'{value}\''
    return format_json_values(value)


def get_string(data, prefix):
    key = f'{prefix}{data["key"]}'

    if data["status"] == ADDED:
        return f'Property \'{key}\'' \
               f' was added with value: {get_value(data["value"])}\n'
    elif data["status"] == REMOVED:
        return f'Property \'{key}\' was removed\n'
    elif data["status"] == UPDATED:
        return f'Property \'{key}\' was updated. ' \
               f'From {get_value(data["value"]["old"])} ' \
               f'to {get_value(data["value"]["new"])}\n'
    else:
        return ''
