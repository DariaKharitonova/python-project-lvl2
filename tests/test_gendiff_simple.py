from gendiff.get_tree_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format
from tests.helpers import read_json, read_yaml
import pytest
import json

def test_generate_diff_txt_json():
    first_file = read_json('tests/fixtures/simple/before.json')
    second_file = read_json('tests/fixtures/simple/after.json')
    correct = open('tests/fixtures/simple/simple_txt.txt').read()
    assert stylish(get_diff(first_file, second_file)) == correct


def test_generate_diff_txt_yaml():
    first_file = read_yaml('tests/fixtures/simple/before.yaml')
    second_file = read_yaml('tests/fixtures/simple/after.yaml')
    correct = open('tests/fixtures/simple/simple_txt.txt').read()
    assert stylish(get_diff(first_file, second_file)) == correct


def test_generate_diff_plain_json():
    first_file = read_json('tests/fixtures/simple/before.json')
    second_file = read_json('tests/fixtures/simple/after.json')
    correct = open('tests/fixtures/simple/simple_plain.txt').read()
    assert plain(get_diff(first_file, second_file)) == correct


def test_generate_diff_plain_yaml():
    first_file = read_yaml('tests/fixtures/simple/before.yaml')
    second_file = read_yaml('tests/fixtures/simple/after.yaml')
    correct = open('tests/fixtures/simple/simple_plain.txt').read()
    assert plain(get_diff(first_file, second_file)) == correct


def test_generate_diff_json_format():
    first_file = read_json('tests/fixtures/simple/before.json')
    second_file = read_json('tests/fixtures/simple/after.json')
    correct = read_json('tests/fixtures/simple/simple_json.json')
    result_json = get_json_format(get_diff(first_file, second_file))
    try:
        json.loads(result_json)
    except ValueError:
        pytest.fail("Can't load json file.")
    assert isinstance(json.loads(result_json), dict)
    assert json.loads(result_json) == correct


def test_generate_diff_yaml_format():
    first_file = read_yaml('tests/fixtures/simple/before.yaml')
    second_file = read_yaml('tests/fixtures/simple/after.yaml')
    correct = read_json('tests/fixtures/simple/simple_json.json')

    result_json = get_json_format(get_diff(first_file, second_file))
    try:
        json.loads(result_json)
    except ValueError:
        pytest.fail("Can't load yaml file.")
    assert isinstance(json.loads(result_json), dict)
    assert json.loads(result_json) == correct
