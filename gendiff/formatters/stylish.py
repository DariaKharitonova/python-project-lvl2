from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, UNCHANGED, NESTED
from gendiff.formatters.format import format_json_values

INDENT_STEP = 4
NESTED_LEVEL_STEP = 6


def format_stylish(diff):
    data = '\n'.join(form_diff(diff))
    return f'{{\n{data}\n}}'


def prepare_dict(value, indent):
    spaces = get_spaces(indent)
    string = '\n'.join(prepare_strings(value, indent))
    return f'{{\n{string}\n{spaces}  }}'


def get_value(value, indent=2):
    if isinstance(value, dict):
        return prepare_dict(value, indent)
    return format_json_values(value)


def prepare_strings(value, indent):
    spaces = get_spaces(indent + NESTED_LEVEL_STEP)
    strings = []
    for key, value in value.items():
        if isinstance(value, dict):
            strings.append(f'{spaces}{key}: {{')
            strings.extend(prepare_strings(value, indent + INDENT_STEP))
            strings.append(f'{spaces}}}')
        else:
            strings.append(f'{spaces}{key}: {value}')
    return strings


def get_nested_value(value, indent=2):
    spaces = get_spaces(indent)
    data = '\n'.join(form_diff(value, indent + INDENT_STEP))

    return f'{{\n{data}\n{spaces + "  "}}}'


def form_diff(result_diff, indent=2):
    strings = []
    spaces = get_spaces(indent)
    sorted_diff = sorted(result_diff, key=lambda x: x['key'])
    for elem in sorted_diff:
        value = get_value(elem["value"], indent)
        status = elem['status']
        if status == ADDED:
            strings.append(f'{spaces}+ {elem["key"]}: '
                           f'{value}')
        elif status == REMOVED:
            strings.append(f'{spaces}- {elem["key"]}: '
                           f'{value}')
        elif status == UPDATED:
            strings.append(f'{spaces}- {elem["key"]}: '
                           f'{get_value(elem["value"]["old"], indent)}')
            strings.append(f'{spaces}+ {elem["key"]}: '
                           f'{get_value(elem["value"]["new"], indent)}')
        elif status == UNCHANGED:
            strings.append(f'{spaces}  {elem["key"]}: '
                           f'{value}')
        elif status == NESTED:
            strings.append(f'{spaces}  {elem["key"]}: '
                           f'{get_nested_value(value, indent)}')

    return strings


def get_spaces(indent):
    return " " * indent
