STATUSES = {
    'added': '+',
    'removed': '-',
    'unchanged': ' ',
    'updated': ' '
}


def sort_by_key(data):
    return sorted(data, key=lambda k: k['key'])


def stylish(result, indent=2):
    result_string = '{\n'

    for x in sort_by_key(result):
        result_string += get_format(x, indent)

    result_string += '}'
    return result_string\
        .replace("True", "true")\
        .replace("False", "false")\
        .replace("None", "null")


def format_nested(result, x, indent=2, sort=True):
    spaces = " " * indent
    result += f'{spaces}{STATUSES[x["status"]]} {x["key"]}: '
    result += '{\n'
    indent += 4
    data = sort_by_key(x['value']) if sort is True else x['value']
    for y in data:
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
        result += format_nested('', {"key": data["key"], "value": old_value, "status": "removed"}, indent)
    else:
        result += f'{spaces}- {data["key"]}: {old_value}\n'
    if isinstance(new_value, list):
        result += format_nested('', {"key": data["key"], "value": new_value, "status": "added"}, indent)
    else:
        result += f'{spaces}+ {data["key"]}: {new_value}\n'

    return result


def get_format(x, indent=2):
    result = ""
    spaces = " " * indent

    if x['status'] == 'updated':
        return format_updated(x, indent)

    if type(x['value']) is list:
        sort = x['status'] != 'added'
        return format_nested(result, x, indent, sort)

    result += f'{spaces}{STATUSES[x["status"]]} {x["key"]}: {x["value"]}\n'
    return result


def get_format(x, indent=2):
    result = ""
    spaces = " " * indent

    if x['status'] == 'updated':
        return format_updated(x, indent)

    if type(x['value']) is list:
        sort = x['status'] != 'added'
        return format_nested(result, x, indent, sort)

    result += f'{spaces}{STATUSES[x["status"]]} {x["key"]}: {x["value"]}\n'
    return result
