from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, NESTED
from gendiff.formatters.format import format_json_values
from gendiff.formatters.helper import reorder

COMPLEX_VALUE = '[complex value]'
ADDED_STRING = "Property {0} was added with value: {1}"
REMOVED_STRING = "Property {0} was removed"
UPDATED_STRING = "Property {0} was updated. From {1} to {2}"


def format_plain(diff):
    sorted_diff = reorder(diff, "key")
    result_string = '\n'.join(filter(lambda x: x != '',
                                     map(lambda x: format_node(x),
                                         sorted_diff)))
    return result_string


def format_node(node, prefix=""):
    if node['status'] == NESTED:
        prefix += f'{node["key"]}.'
        return '\n'.join(filter(lambda x: x != '',
                                map(lambda x: format_node(x, prefix),
                                    node['value'])))
    return get_string(node, prefix)


def get_string(data, prefix):
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
    if isinstance(value, str):
        return f'\'{value}\''
    return format_json_values(value)
