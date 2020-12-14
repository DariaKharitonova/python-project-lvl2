from gendiff.get_data.get_data import get_data
from gendiff.get_tree_diff import get_diff
from gendiff.formatters.formater import view_format, DEFAULT_STYLE


def generate_diff(first_file_path, second_file_path, format=DEFAULT_STYLE):
    first_file = get_data(first_file_path) or {}
    second_file = get_data(second_file_path) or {}
    print('###FIRST_FILE')
    print(first_file)
    print('###SECOND_FILE')
    print(second_file)
    result_diff = get_diff(first_file, second_file)
    return view_format(result_diff, format)
