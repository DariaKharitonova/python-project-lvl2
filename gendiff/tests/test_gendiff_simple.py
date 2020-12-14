from gendiff.get_tree_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format
from gendiff.tests.helpers import read_json, read_yaml


def test_generate_diff_txt_json():
    first_file = read_json('gendiff/tests/fixtures/json/test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/test2.json')
    correct = open('gendiff/tests/fixtures/formats/simple_txt.txt').read()
    assert stylish(get_diff(first_file, second_file)) == correct
    print("simple json test passed")


def test_generate_diff_txt_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/test2.yaml')
    correct = open('gendiff/tests/fixtures/formats/simple_txt.txt').read()
    print(correct)
    assert stylish(get_diff(first_file, second_file)) == correct
    print("simple yaml test passed")


def test_generate_diff_plain_json():
    first_file = read_json('gendiff/tests/fixtures/json/test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/test2.json')
    correct = open('gendiff/tests/fixtures/formats/simple_plain.txt').read()
    assert plain(get_diff(first_file, second_file)) == correct
    print("simple plain json test passed")


def test_generate_diff_plain_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/test2.yaml')
    correct = open('gendiff/tests/fixtures/formats/simple_plain.txt').read()
    print(correct)
    assert plain(get_diff(first_file, second_file)) == correct
    print("simple plain json test passed")


def test_generate_diff_json_format():
    first_file = read_json('gendiff/tests/fixtures/json/test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/test2.json')
    correct = open('gendiff/tests/fixtures/formats/simple_json.json').read()
    print(correct)
    assert get_json_format(get_diff(first_file, second_file)) == correct
    print("simple plain json test passed")
