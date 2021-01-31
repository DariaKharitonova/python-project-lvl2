def reorder(data, sort_by):
    data = sorted(data, key=lambda x: x[sort_by])
    for item in data:
        if item["status"] == 'nested':
            item["value"] = reorder(item["value"], sort_by)
    return data
