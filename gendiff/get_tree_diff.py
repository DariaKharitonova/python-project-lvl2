ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'

# def format_json_values(value):
#     if value is True:
#         return 'true'
#     elif value is False:
#         return 'false'
#     elif value is None:
#         return 'null'
#     return value


def get_diff(data1, data2):
    deleted_keys = data1.keys() - data2.keys()
    add_keys = data2.keys() - data1.keys()
    if data2.keys() == data1.keys():
        all_keys = data1.keys()
    else:
        all_keys = list(data2.keys() | data1.keys())
        all_keys.sort()

    result = []
    for key in all_keys:
        if key in deleted_keys:
            result.append({
                'key': key,
                'value': get_diff(data1[key], data1[key])
                if isinstance(data1[key], dict) else data1[key],
                'status': REMOVED,
                'nested': isinstance(data1[key], dict)
            })
        elif key in add_keys:
            result.append({
                'key': key,
                'value': get_diff(data2[key], data2[key])
                if isinstance(data2[key], dict) else data2[key],
                'status': ADDED,
                'nested': isinstance(data2[key], dict)
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'value': get_diff(data1[key], data2[key])
                if isinstance(data1[key], dict) else data1[key],
                'status': UNCHANGED,
                'nested': isinstance(data1[key], dict)
            })
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append({
                    'key': key,
                    'value': get_diff(data1[key], data2[key]),
                    'status': UNCHANGED,
                    'nested': True
                })
            else:
                result.append({
                    'key': key,
                    'value': {
                        'old': get_diff(data1[key], data1[key])
                        if isinstance(data1[key], dict) else data1[key],
                        'new': get_diff(data2[key], data2[key])
                        if isinstance(data2[key], dict) else data2[key],
                    },
                    'status': UPDATED,
                    'nested': False
                })

    return result
