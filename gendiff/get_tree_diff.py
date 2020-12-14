ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'


def get_diff(data1, data2):
    keys_1, keys_2 = set(data1.keys()), set(data2.keys())
    deleted_keys = keys_1 - keys_2
    add_keys = keys_2 - keys_1
    all_keys = sorted(keys_1 | keys_2)

    result = []
    for key in all_keys:
        if key in deleted_keys:
            result.append({
                'key': key,
                'value': get_diff(data1[key], data1[key])
                if isinstance(data1[key], dict) else data1[key],
                'status': REMOVED
            })
        elif key in add_keys:
            result.append({
                'key': key,
                'value': get_diff(data2[key], data2[key])
                if isinstance(data2[key], dict) else data2[key],
                'status': ADDED
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'value': get_diff(data1[key], data2[key])
                if isinstance(data1[key], dict) else data1[key],
                'status': UNCHANGED
            })
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append({
                    'key': key,
                    'value': get_diff(data1[key], data2[key]),
                    'status': UNCHANGED
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
                    'status': UPDATED
                })

    return result
