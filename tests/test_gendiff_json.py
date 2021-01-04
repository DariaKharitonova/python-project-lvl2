from gendiff.get_tree_diff import get_diff
from gendiff.formatters.json import get_json_format
from tests.helpers import read_json, read_yaml
import pytest
import json


def test_recursive_diff_json_format():
    first_file = read_json('tests/fixtures/complex/before.json')
    second_file = read_json('tests/fixtures/complex/after.json')
    correct = read_json('tests/fixtures/complex/complex_json.json')
    result_json = get_json_format(get_diff(first_file, second_file))
    assert json.loads(result_json) == correct


@pytest.mark.parametrize(
    'read_file, first_file_path, second_file_path, correct_file_path',
    [
     (
         read_json,
         'simple_before_json',
         'simple_after_json',
         'result_simple_json'
     ),
     (
         read_yaml,
         'simple_before_yaml',
         'simple_after_yaml',
         'result_simple_json'
     ),
     (
         read_json,
         'complex_before_json',
         'complex_after_json',
         'result_complex_json'
     ),
     (
         read_yaml,
         'complex_before_yaml',
         'complex_after_yaml',
         'result_complex_json'
     )
    ])
def test_generate_diff_json_format(read_file, first_file_path,
                                   second_file_path, correct_file_path,
                                   request):
    first_file = read_file(request.getfixturevalue(first_file_path))
    second_file = read_file(request.getfixturevalue(second_file_path))
    correct = read_json(request.getfixturevalue(correct_file_path))

    result_json = get_json_format(get_diff(first_file, second_file))
    json.loads(result_json)
    assert isinstance(json.loads(result_json), dict)
    assert json.loads(result_json) == correct
