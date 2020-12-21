from gendiff.get_tree_diff import get_diff
from gendiff.formatters.json import get_json_format
from tests.helpers import read_json, read_yaml
import pytest
import json
import yaml


def test_recursive_diff_json_format():
    first_file = read_json('tests/fixtures/complex/complex_before.json')
    second_file = read_json('tests/fixtures/complex/complex_after.json')
    result_json = get_json_format(get_diff(first_file, second_file))
    try:
        json.loads(result_json)
    except ValueError:
        pytest.fail(ValueError)
    assert isinstance(json.loads(result_json), dict)


def test_recursive_diff_json_format_yaml():
    first_file = read_yaml('tests/fixtures/complex/complex_before.yaml')
    second_file = read_yaml('tests/fixtures/complex/complex_after.yaml')
    result_yaml = get_json_format(get_diff(first_file, second_file))
    try:
        yaml.load(result_yaml, Loader=yaml.FullLoader)
    except ValueError:
        pytest.fail(ValueError)
    assert isinstance(yaml.load(result_yaml, Loader=yaml.FullLoader), dict)


@pytest.fixture(params=[
    (
        read_json('tests/fixtures/simple/before.json'),
        read_json('tests/fixtures/simple/after.json'),
        read_json('tests/fixtures/simple/simple_json.json')
    ),
    (
        read_yaml('tests/fixtures/simple/before.yaml'),
        read_yaml('tests/fixtures/simple/after.yaml'),
        read_json('tests/fixtures/simple/simple_json.json')
    )
])
def parameters_test(request):
    return request.param


def test_generate_diff_json_format(parameters_test):
    first_file, second_file, correct = parameters_test
    result_json = get_json_format(get_diff(first_file, second_file))
    try:
        json.loads(result_json)
    except ValueError:
        pytest.fail("Can't load json file.")
    assert isinstance(json.loads(result_json), dict)
    assert json.loads(result_json) == correct
