from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish

FORMATS = {
    'stylish': format_stylish,
    'json': format_json,
    'plain': format_plain
}

DEFAULT_STYLE = 'stylish'


def format_diff(diff, style=DEFAULT_STYLE):
    if style in FORMATS:
        formatter = FORMATS.get(style)
        if formatter is None:
            raise RuntimeError(f'{style} is wrong format. '
                               f'Available formats: stylish, plain, json.')
        return formatter(diff)
