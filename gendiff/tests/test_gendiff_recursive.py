from gendiff.get_tree_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format
from gendiff.tests.helpers import read_json, read_yaml
import pytest
import json
import yaml


def test_recursive_diff_txt_json():
    first_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/recursive_test2.json')
    correct = open('gendiff/tests/fixtures/formats/recursive_txt.txt').read()
    assert stylish(get_diff(first_file, second_file)) == correct
    print("recursive json test passed")


def test_recursive_diff_txt_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test2.yaml')
    correct = open('gendiff/tests/fixtures/formats/recursive_txt.txt').read()
    assert stylish(get_diff(first_file, second_file)) == correct
    print("recursive yaml test passed")


def test_recursive_diff_plain_json():
    first_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/recursive_test2.json')
    correct = open('gendiff/tests/fixtures/formats/recursive_plain.txt').read()
    assert plain(get_diff(first_file, second_file)) == correct
    print("recursive plain json test passed")


def test_recursive_diff_plain_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test2.yaml')
    correct = open('gendiff/tests/fixtures/formats/recursive_plain.txt').read()
    assert plain(get_diff(first_file, second_file)) == correct
    print("recursive plain yaml test passed")


def test_recursive_diff_json_format():
    first_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/recursive_test2.json')
    result_json = get_json_format(get_diff(first_file, second_file))
    try:
        json.loads(result_json)
    except ValueError:
        pytest.fail(ValueError)
    assert isinstance(json.loads(result_json), dict)
    print("recursive json format test passed")


def est_recursive_diff_json_format_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test2.yaml')
    result_yaml = get_json_format(get_diff(first_file, second_file))
    try:
        yaml.load(result_yaml, Loader=yaml.FullLoader)
    except ValueError:
        pytest.fail(ValueError)
    assert isinstance(yaml.load(result_yaml, Loader=yaml.FullLoader), dict)
    print("recursive yaml test passed")
