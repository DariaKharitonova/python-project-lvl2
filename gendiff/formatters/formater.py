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
    if style in VIEW_STYLES:
        return VIEW_STYLES.get(style)(result)
    RuntimeError(f'{style} is wrong format. '
                 f'Available formats: stylish, plain, json.')
