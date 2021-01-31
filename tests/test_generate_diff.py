import pytest
from gendiff.gendiff import generate_diff


@pytest.mark.parametrize(
    'first_file_path, second_file_path, format, correct_file_path',
    [
        (
            'complex_before_json',
            'complex_after_json',
            'stylish',
            'result_complex_stylish'
        ),
        (
            'simple_before_json',
            'simple_after_json',
            'plain',
            'result_simple_plain'
        ),
        (
            'simple_before_json',
            'simple_after_json',
            'json',
            'result_simple_json'
        ),
        (
            'complex_before_json',
            'complex_after_json',
            'stylish',
            'result_complex_stylish'
        ),
        (
            'complex_before_json',
            'complex_after_json',
            'plain',
            'result_complex_plain'
        ),
        (
            'complex_before_json',
            'complex_after_json',
            'json',
            'result_complex_json'
        )
    ])
def test_generate_diff(first_file_path, second_file_path,
                       format, correct_file_path, request):
    first_file = request.getfixturevalue(first_file_path)
    second_file = request.getfixturevalue(second_file_path)
    correct = open(request.getfixturevalue(correct_file_path)).read()
    assert generate_diff(first_file, second_file, format) == correct
