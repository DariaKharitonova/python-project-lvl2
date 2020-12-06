def stylish(result, indent=2):
    result_string = '{\n'

    for x in result:
        result_string += get_format(x, indent)

    result_string += '}'
    return result_string\
        .replace("True", "true")\
        .replace("False", "false")\
        .replace("None", "null")


def get_format(x, indent=2):
    result = ""
    spaces = " " * indent

    if type(x['value']) is list:
        result += f'{spaces}{x["status"]} {x["key"]}: '
        result += '{\n'
        indent += 4
        for y in x['value']:
            result += get_format(y, indent)
        result += f'{spaces}  '
        result += '}\n'
        return result
    result += f'{spaces}{x["status"]} {x["key"]}: {x["value"]}\n'
    return result
