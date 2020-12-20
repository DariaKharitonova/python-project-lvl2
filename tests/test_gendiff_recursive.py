from gendiff.get_tree_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format
from tests.helpers import read_json, read_yaml
import pytest
import json
import yaml


def test_recursive_diff_txt_json():
    first_file = read_json('tests/fixtures/complex/complex_before.json')
    second_file = read_json('tests/fixtures/complex/complex_after.json')
    correct = open('tests/fixtures/complex/txt.txt').read()
    assert stylish(get_diff(first_file, second_file)) == correct


def test_recursive_diff_txt_yaml():
    first_file = read_yaml('tests/fixtures/complex/complex_before.yaml')
    second_file = read_yaml('tests/fixtures/complex/complex_after.yaml')
    correct = open('tests/fixtures/complex//txt.txt').read()
    assert stylish(get_diff(first_file, second_file)) == correct


def test_recursive_diff_plain_json():
    first_file = read_json('tests/fixtures/complex/complex_before.json')
    second_file = read_json('tests/fixtures/complex/complex_after.json')
    correct = open('tests/fixtures/complex//plain.txt').read()
    assert plain(get_diff(first_file, second_file)) == correct


def test_recursive_diff_plain_yaml():
    first_file = read_yaml('tests/fixtures/complex/complex_before.yaml')
    second_file = read_yaml('tests/fixtures/complex/complex_after.yaml')
    correct = open('tests/fixtures/complex//plain.txt').read()
    assert plain(get_diff(first_file, second_file)) == correct


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
