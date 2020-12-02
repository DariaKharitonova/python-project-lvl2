def generate_diff(file1, file2):
    keys_1, keys_2 = set(file1.keys()), set(file2.keys())
    deleted_keys = keys_1 - keys_2
    add_keys = keys_2 - keys_1
    all_keys = sorted(keys_1 | keys_2)

    result = []
    for key in all_keys:
        if key in deleted_keys:
            result.append({
                'key': key,
                'value': file1[key],
                'status': '-'
            })
            continue
        elif key in add_keys:
            result.append({
                'key': key,
                'value': file2[key],
                'status': '+'
            })
            continue
        if file1[key] == file2[key]:
            result.append({
                'key': key,
                'value': file1[key],
                'status': ' '
            })
        elif type(file1[key]) is dict \
                and type(file2[key]) is dict and file1[key] != file2[key]:
            res = generate_diff(file1[key], file2[key])
            result.append({
                'key': key,
                'value': res,
                'status': ' '
            })
        else:
            result.append({
                'key': key,
                'value': file1[key],
                'status': '-'
            })
            result.append({
                'key': key,
                'value': file2[key],
                'status': '+'
            })

    return result
