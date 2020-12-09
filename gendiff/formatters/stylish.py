STATUSES = {
    'added': '+',
    'removed': '-',
    'unchanged': ' ',
    'updated': ' '
}


def stylish(result, indent=2):
    result_string = '{\n'

    for x in result:
        result_string += get_format(x, indent)

    result_string += '}'
    return result_string\
        .replace("True", "true")\
        .replace("False", "false")\
        .replace("None", "null")


def format_nested(result, x, indent=2):
    spaces = " " * indent

    result += f'{spaces}{STATUSES[x["status"]]} {x["key"]}: '
    result += '{\n'
    indent += 4
    for y in x['value']:
        result += get_format(y, indent)
    result += f'{spaces}  '
    result += '}\n'
    return result


def format_updated(data, indent):
    result = ''
    spaces = " " * indent
    old_value = data["value"]["old"]
    new_value = data["value"]["new"]
    if isinstance(old_value, list):
        result += format_nested(result, {"key": data["key"],
                                         "value": old_value,
                                         "status": "removed"}, indent)
    else:
        result += f'{spaces}- {data["key"]}: {old_value}\n'

    if isinstance(new_value, list):
        result += format_nested(result, {"key": data["key"],
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
        return format_nested(result, x, indent)

    result += f'{spaces}{STATUSES[x["status"]]} {x["key"]}: {x["value"]}\n'
    return result
