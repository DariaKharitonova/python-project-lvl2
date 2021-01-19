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


def form_dict_value(data, indent=2):
    spaces = get_spaces(indent)
    return f'{{\n{data}{spaces}  }}'


def format_nested(x, indent=2):
    data_string = ''.join(get_format(y, indent + 4) for y in x['value'])
    result = format_string(x['status'], x['key'],
                           form_dict_value(data_string, indent), indent)
    return result


def format_inner_properties(key, value, indent=2):
    if isinstance(value, dict):
        return format_dict({"key": key,
                            "value": value,
                            "status": UNCHANGED}, indent + 4)

    return format_string(UNCHANGED, key, value, indent + 4)


def format_dict(x, indent=2):
    data_string = "".join(format_inner_properties(key, value, indent)
                          for key, value in x['value'].items())
    result = format_string(x["status"], x['key'],
                           form_dict_value(data_string, indent), indent)
    return result


def form_dict(key, value, status):
    return {"key": key, "value": value, "status": status}


def format_updated(data, indent):
    old_value = data["value"]["old"]
    new_value = data["value"]["new"]
    old_value_string = format_dict(form_dict(data["key"], old_value, REMOVED), indent) \
        if isinstance(old_value, dict) else format_string(REMOVED, data["key"], old_value, indent)  # noqa: E501
    new_value_string = format_dict(form_dict(data["key"], new_value, ADDED), indent) \
        if isinstance(new_value, dict) else format_string(ADDED, data["key"], new_value, indent)  # noqa: E501

    result = f'{old_value_string}{new_value_string}'
    return result


def format_string(status, key, value, indent=2):
    spaces = get_spaces(indent)
    status_symbol = STATUSES[status]

    return f'{spaces}{status_symbol} {key}: {format_json_values(value)}\n'


def get_format(x, indent=2):
    if x['status'] == UPDATED:
        return format_updated(x, indent)

    if x['nested'] is True:
        return format_nested(x, indent)

    if isinstance(x["value"], dict):
        return format_dict(x, indent)

    result = format_string(x['status'], x['key'], x['value'], indent)

    return result


def get_spaces(indent):
    return " " * indent
