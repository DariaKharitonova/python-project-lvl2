from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format
from gendiff.formatters.stylish import stylish

VIEW_STYLES = {
    'stylish': stylish,
    'json': get_json_format,
    'plain': plain
}

DEFAULT_STYLE = 'stylish'


def view_format(result, style=DEFAULT_STYLE):
    if style in VIEW_STYLES.keys():
        return VIEW_STYLES.get(style)(result)
    RuntimeError('Wrong format')
