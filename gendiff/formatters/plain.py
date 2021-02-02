from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, NESTED
from gendiff.formatters.sort_diff_keys import sort_keys

COMPLEX_VALUE = '[complex value]'
ADDED_STRING = "Property {0} was added with value: {1}"
REMOVED_STRING = "Property {0} was removed"
UPDATED_STRING = "Property {0} was updated. From {1} to {2}"


def format_plain(diff):
    sorted_diff = sort_keys(diff)
    result_string = to_string(sorted_diff)
    return result_string


def to_string(diff, prefix=""):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: format_node(x, prefix),
                                diff)))


def format_node(node, prefix=""):
    if node['status'] == NESTED:
        prefix += f'{node["key"]}.'
        return to_string(node['value'], prefix)
    return get_diff_line(node, prefix)


def get_diff_line(data, prefix):
    key = f'\'{prefix}{data["key"]}\''

    if data["status"] == ADDED:
        return ADDED_STRING.format(key, format_value(data["value"]))
    elif data["status"] == REMOVED:
        return REMOVED_STRING.format(key)
    elif data["status"] == UPDATED:
        return UPDATED_STRING.format(key,
                                     format_value(data["value"]["old"]),
                                     format_value(data["value"]["new"]))
    else:
        return ''


def format_value(value):
    if isinstance(value, list) or isinstance(value, dict):
        return COMPLEX_VALUE
    elif isinstance(value, str):
        return f'\'{value}\''
    else:
        if value is True:
            return 'true'
        elif value is False:
            return 'false'
        elif value is None:
            return 'null'
        return value
