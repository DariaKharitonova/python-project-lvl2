from gendiff.gendiff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format
from gendiff.tests.helpers import read_json, read_yaml


def est_recursive_diff_txt_json():
    first_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    correct = open('gendiff/tests/fixtures/formats/recursive_txt.txt').read()
    assert stylish(generate_diff(first_file, second_file)) == correct
    print("recursive json test passed")


def est_recursive_diff_txt_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    correct = open('gendiff/tests/fixtures/formats/recursive_txt.txt').read()
    assert stylish(generate_diff(first_file, second_file)) == correct
    print("recursive yaml test passed")


def est_recursive_diff_plain_json():
    first_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    correct = open('gendiff/tests/fixtures/formats/plain.txt').read()
    assert plain(generate_diff(first_file, second_file)) == correct
    print("simple plain json test passed")


def est_recursive_diff_plain_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    correct = open('gendiff/tests/fixtures/formats/plain.txt').read()
    assert plain(generate_diff(first_file, second_file)) == correct
    print("simple plain json test passed")


def est_recursive_diff_json_format():
    first_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    second_file = read_json('gendiff/tests/fixtures/json/recursive_test1.json')
    correct = open('gendiff/tests/fixtures/formats/recursive_json.txt').read()
    assert get_json_format(generate_diff
                           (first_file, second_file)) == correct
    print("simple plain json test passed")


def est_recursive_diff_json_format_yaml():
    first_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    second_file = read_yaml('gendiff/tests/fixtures/yaml/recursive_test1.yaml')
    correct = open('gendiff/tests/fixtures/formats/recursive_json.txt').read()
    assert get_json_format(generate_diff
                           (first_file, second_file)) == correct
    print("simple plain json test passed")