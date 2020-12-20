from gendiff.get_tree_diff import ADDED, REMOVED, UPDATED, UNCHANGED

STATUSES = {
    ADDED: '+',
    REMOVED: '-',
    UNCHANGED: ' ',
    UPDATED: ' '
}


def stylish(result, indent=2):

    data_string = ''.join(get_format(x, indent) for x in result)
    result_string = f'{{\n{data_string}}}'

    return result_string\
        .replace("True", "true")\
        .replace("False", "false")\
        .replace("None", "null")


def format_nested(x, indent=2):
    spaces = " " * indent
    indent += 4
    data_string = ''.join(get_format(y, indent) for y in x['value'])
    result = f'{spaces}{STATUSES[x["status"]]} ' \
             f'{x["key"]}: {{\n{data_string}{spaces}  }}\n'
    return result


def format_updated(data, indent):
    result = ''
    spaces = " " * indent
    old_value = data["value"]["old"]
    new_value = data["value"]["new"]
    if isinstance(old_value, list):
        result += format_nested({"key": data["key"],
                                 "value": old_value,
                                 "status": "removed"}, indent)
    else:
        result += f'{spaces}- {data["key"]}: {old_value}\n'
    if isinstance(new_value, list):
        result += format_nested({"key": data["key"],
                                 "value": new_value,
                                 "status": "added"}, indent)
    else:
        result += f'{spaces}+ {data["key"]}: {new_value}\n'

    return result


def get_format(x, indent=2):
    result = ""
    spaces = " " * indent

    if x['status'] == 'updated':
        return format_updated(x, indent)

    if type(x['value']) is list:
        return format_nested(x, indent)

    result += f'{spaces}{STATUSES[x["status"]]} {x["key"]}: {x["value"]}\n'
    return result
