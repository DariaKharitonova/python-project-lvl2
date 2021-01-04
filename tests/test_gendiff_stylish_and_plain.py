from gendiff.get_tree_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from tests.helpers import read_json, read_yaml
import pytest


@pytest.mark.parametrize(
    'formatter, read_file, first_file_path, second_file_path, correct_file_path', # noqa E501
    [
        (
            stylish,
            read_json,
            'simple_before_json',
            'simple_after_json',
            'result_simple_stylish'
        ),
        (
            stylish,
            read_yaml,
            'simple_before_yaml',
            'simple_after_yaml',
            'result_simple_stylish'
        ),
        (
            plain,
            read_json,
            'simple_before_json',
            'simple_after_json',
            'result_simple_plain'
        ),
        (
            plain,
            read_yaml,
            'simple_before_yaml',
            'simple_after_yaml',
            'result_simple_plain'
        ),
        (
            stylish,
            read_json,
            'complex_before_json',
            'complex_after_json',
            'result_complex_stylish'
        ),
        (
            stylish,
            read_yaml,
            'complex_before_yaml',
            'complex_after_yaml',
            'result_complex_stylish'
        ),
        (
            plain,
            read_json,
            'complex_before_json',
            'complex_after_json',
            'result_complex_plain'

        ),
        (
            plain,
            read_yaml,
            'complex_before_yaml',
            'complex_after_yaml',
            'result_complex_plain'
        )
    ])
def test_diff(formatter, read_file, first_file_path,
              second_file_path, correct_file_path, request):
    first_file = read_file(request.getfixturevalue(first_file_path))
    second_file = read_file(request.getfixturevalue(second_file_path))
    correct = open(request.getfixturevalue(correct_file_path)).read()
    assert formatter(get_diff(first_file, second_file)) == correct
