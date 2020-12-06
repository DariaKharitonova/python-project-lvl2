from functools import reduce

def plain(result):
    result_string = ""
    for x in result:
        result_string += get_format(x)
    return result_string \
        .replace("True", "true") \
        .replace("False", "false") \
        .replace("None", "null")


def get_format(data, prefix=""):

    if isinstance(data['value'], list) and (data['status'] != '+' and data['status'] != '-'):
        # print(data)
        prefix += f'{data["key"]}.'
        res = ''
        for y in data['value']:
            ll = list(filter(lambda el: el['key'] == y['key'], data['value']))
            if len(ll) > 1:
                # print(ll)
                res += get_string(ll[0], prefix, ll[1])
            else:
                res += get_format(y, prefix)
        return res
    return get_string(data, prefix)


def get_value(value):
    if isinstance(value, list):
        return '[complex value]'
    return value


def get_string(data, prefix, data2=None):
    if data2 is not None:
        return f'Property \'{prefix}{data["key"]}\' was updated. From {get_value(data["value"])} to {get_value(data2["value"])}\n'

    if data["status"] == '+':
        return f'Property \'{prefix}{data["key"]}\' was added with value: {get_value(data["value"])}\n'
    elif data["status"] == '-':
        return f'Property \'{prefix}{data["key"]}\' was removed\n'
    elif data["status"] == ' ':
        return ''


def get_value_status(old_value, new_value):
    if new_value is not None and old_value is None:
        return 'was added'
    elif new_value is None and old_value is not None:
        return 'was removed'
    elif new_value is not None and old_value is not None:
        return 'was updated'


def get_status_message(before_status, after_status, path):
    diff = get_value_status(before_status, after_status)
    message = f'Property \'{path}\' was {diff}'
    if diff == 'added':
        return
