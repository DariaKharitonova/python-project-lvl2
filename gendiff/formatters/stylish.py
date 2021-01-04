from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, UNCHANGED
from gendiff.helpers.format import format_json_values

STATUSES = {
    ADDED: '+',
    REMOVED: '-',
    UNCHANGED: ' ',
    UPDATED: ' '
}


def stylish(result, indent=2):
    data_string = ''.join(get_format(x, indent) for x in result)
    result_string = f'{{\n{data_string}}}'

    return result_string


def format_nested(x, indent=2):
    spaces = get_spaces(indent)
    indent += 4
    data_string = ''.join(get_format(y, indent) for y in x['value'])
    result = f'{spaces}{STATUSES[x["status"]]} ' \
             f'{x["key"]}: {{\n{data_string}{spaces}  }}\n'
    return result


def format_updated(data, indent):
    result = ''
    spaces = get_spaces(indent)
    old_value = data["value"]["old"]
    new_value = data["value"]["new"]
    if isinstance(old_value, list) and len(old_value) != 0 \
            and isinstance(old_value[0], dict):
        result += format_nested({"key": data["key"],
                                 "value": old_value,
                                 "status": REMOVED}, indent)
    else:
        result += f'{spaces}- {data["key"]}: {format_json_values(old_value)}\n'

    if isinstance(new_value, list) and len(new_value) != 0 \
            and isinstance(new_value[0], dict):
        result += format_nested({"key": data["key"],
                                 "value": new_value,
                                 "status": ADDED}, indent)
    else:
        result += f'{spaces}+ {data["key"]}: {format_json_values(new_value)}\n'

    return result


def get_format(x, indent=2):
    spaces = get_spaces(indent)

    if x['status'] == UPDATED:
        return format_updated(x, indent)

    if x['nested'] is True:
        return format_nested(x, indent)

    result = f'{spaces}{STATUSES[x["status"]]} ' \
             f'{x["key"]}: {format_json_values(x["value"])}\n'
    return result


def get_spaces(indent):
    return " " * indent
