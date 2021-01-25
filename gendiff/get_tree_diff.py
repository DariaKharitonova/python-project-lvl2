ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
ROOT = 'root'


def get_diff(data1, data2):
    diff = {
        'type': ROOT,
        'nodes': add_nested_nodes(data1, data2)
    }
    return diff


def add_nested_nodes(data1, data2):
    deleted_keys = data1.keys() - data2.keys()
    add_keys = data2.keys() - data1.keys()
    all_keys = data2.keys() | data1.keys()

    diff = []
    for key in all_keys:
        if key in deleted_keys:
            diff.append({
                'key': key,
                'value': data1[key],
                'type': REMOVED,
            })
        elif key in add_keys:
            diff.append({
                'key': key,
                'value': data2[key],
                'type': ADDED,
            })
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'value': data1[key],
                'type': UNCHANGED
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'value': add_nested_nodes(data1[key], data2[key]),
                'type': UNCHANGED,
            })
        else:
            diff.append({
                'key': key,
                'value': {
                    'old': data1[key],
                    'new': data2[key],
                },
                'type': UPDATED
            })

    return sorted(diff, key=lambda x: x['key'])

# def get_diff(data1, data2):
#     deleted_keys = data1.keys() - data2.keys()
#     add_keys = data2.keys() - data1.keys()
#     all_keys = list(data2.keys() | data1.keys())
#
#     result_diff = []
#     for key in all_keys:
#         if key in deleted_keys:
#             result_diff.append({
#                 'key': key,
#                 'value': data1[key],
#                 'status': REMOVED,
#                 'nested': False
#             })
#         elif key in add_keys:
#             result_diff.append({
#                 'key': key,
#                 'value': data2[key],
#                 'status': ADDED,
#                 'nested': False
#             })
#         elif data1[key] == data2[key]:
#             result_diff.append({
#                 'key': key,
#                 'value': data1[key],
#                 'status': UNCHANGED,
#                 'nested': False
#             })
#         elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
#             result_diff.append({
#                 'key': key,
#                 'value': get_diff(data1[key], data2[key]),
#                 'status': UNCHANGED,
#                 'nested': True
#             })
#         else:
#             result_diff.append({
#                 'key': key,
#                 'value': {
#                     'old': data1[key],
#                     'new': data2[key],
#                 },
#                 'status': UPDATED,
#                 'nested': False
#             })
#
#     return sorted(result_diff, key=lambda x: x['key'])