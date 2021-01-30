from gendiff.get_data import get_data
from gendiff.get_tree_diff import get_diff
from gendiff.formatters.formater import format_diff, DEFAULT_STYLE


def generate_diff(first_file_path, second_file_path, format=DEFAULT_STYLE):
    first_file = get_data(first_file_path)
    second_file = get_data(second_file_path)
    diff = get_diff(first_file, second_file)
    return format_diff(diff, format)
