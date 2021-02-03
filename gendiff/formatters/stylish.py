from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, UNCHANGED, NESTED
from gendiff.formatters.sort_diff_keys import sort_keys

INDENT_STEP = 4
NESTED_LEVEL_STEP = 6


def format_stylish(diff):
    sorted_diff = sort_keys(diff)
    stylish_diff = '\n'.join(format_diff(sorted_diff))
    return f'{{\n{stylish_diff}\n}}'


def format_dict(value, indent):
    spaces = get_spaces(indent)
    string = '\n'.join(format_dict_in_strings(value, indent))
    return f'{{\n{string}\n{spaces}  }}'


def format_value(value, indent=2):
    if isinstance(value, dict):
        return format_dict(value, indent)
    else:
        if value is True:
            return 'true'
        elif value is False:
            return 'false'
        elif value is None:
            return 'null'
        return value


def format_dict_in_lines(value, indent):
    spaces = get_spaces(indent + NESTED_LEVEL_STEP)
    strings = []
    for key, value in value.items():
        if isinstance(value, dict):
            strings.append(f'{spaces}{key}: {{')
            strings.extend(format_dict_in_lines(value, indent + INDENT_STEP))
            strings.append(f'{spaces}}}')
        else:
            strings.append(f'{spaces}{key}: {value}')
    return strings


def format_nested_value(value, indent=2):
    spaces = get_spaces(indent)
    data = '\n'.join(format_diff(value, indent + INDENT_STEP))

    return f'{{\n{data}\n{spaces + "  "}}}'


def format_diff(diff, indent=2):
    strings = []
    spaces = get_spaces(indent)
    for elem in diff:
        value = format_value(elem["value"], indent)
        status = elem['status']
        if status == ADDED:
            strings.append(f'{spaces}+ {elem["key"]}: '
                           f'{value}')
        elif status == REMOVED:
            strings.append(f'{spaces}- {elem["key"]}: '
                           f'{value}')
        elif status == UPDATED:
            strings.append(f'{spaces}- {elem["key"]}: '
                           f'{format_value(elem["value"]["old"], indent)}')
            strings.append(f'{spaces}+ {elem["key"]}: '
                           f'{format_value(elem["value"]["new"], indent)}')
        elif status == UNCHANGED:
            strings.append(f'{spaces}  {elem["key"]}: '
                           f'{value}')
        elif status == NESTED:
            strings.append(f'{spaces}  {elem["key"]}: '
                           f'{format_nested_value(value, indent)}')

    return strings


def get_spaces(indent):
    return " " * indent
