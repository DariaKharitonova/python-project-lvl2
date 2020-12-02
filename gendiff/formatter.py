def format_dict(x, indent):
    result = ""
    spaces = ""
    for i in range(indent):
        spaces += " "
    if type(x['value']) is list:
        result += f'  {spaces}{x["key"]}: '
        result += '{\n'
        indent += 4
        for y in x['value']:
        result += format_dict(y, indent)
        result += f'{spaces}'
        result += '  }\n'
        return result
    result += f'{spaces}{x["status"]} {x["key"]}: {x["value"]}\n'
    return result


def formatter(result):
    result_string = '{\n'
    indent = 2
    for x in result:
        print(type(x['value']))
        result_string += f'  {x["status"]} {x["key"]}: {x["value"]}\n'
        result_string += format_dict(x, indent)
        result_string += '}'
        result_string = result_string\
            .replace("True", "true")\
            .replace("False", "false")\
            .replace("None", "null")
    return result_string
