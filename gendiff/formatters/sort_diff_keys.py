from gendiff.get_tree_diff import NESTED


def sort_keys(data):
    data = sorted(data, key=lambda x: x['key'])
    for item in data:
        if item["status"] == NESTED:
            item["value"] = sort_keys(item["value"])
    return data
