def plain(result):
    result_string = ""
    for x in result:
        result_string += get_format(x)
    return result_string \
        .replace("True", "true") \
        .replace("False", "false") \
        .replace("None", "null") \
        .rstrip()


def get_format(data, prefix=""):
    if isinstance(data['value'], list) and data['status'] == 'unchanged':
        result = ''
        prefix += f'{data["key"]}.'
        for v in data['value']:
            result += get_format(v, prefix)
        return result
    return get_string(data, prefix)


def get_value(value):
    if isinstance(value, list):
        return '[complex value]'
    if isinstance(value, str):
        return f'\'{value}\''
    return value


def get_string(data, prefix):
    key = f'{prefix}{data["key"]}'

    if data["status"] == 'added':
        return f'Property \'{key}\'' \
               f' was added with value: {get_value(data["value"])}\n'
    elif data["status"] == 'removed':
        return f'Property \'{key}\' was removed\n'
    elif data["status"] == 'updated':
        return f'Property \'{key}\' was updated. ' \
               f'From {get_value(data["value"]["old"])} ' \
               f'to {get_value(data["value"]["new"])}\n'
    else:
        return ''
