from gendiff.get_data.get_data import get_data
from gendiff.gendiff import generate_diff


def test_generate_diff_json():
    correct_diff = open('gendiff/tests/fixtures/json/correct_answer.txt')\
        .read()
    first_file = get_data('gendiff/tests/fixtures/json/test1.json')
    second_file = get_data('gendiff/tests/fixtures/json/test2.json')
    assert generate_diff(first_file, second_file) == correct_diff
    print("json test passed")


def test_generate_diff_yaml():
    correct_diff = open('gendiff/tests/fixtures/yaml/correct_answer.txt')\
        .read()
    first_file = get_data('gendiff/tests/fixtures/yaml/test1.yaml')
    second_file = get_data('gendiff/tests/fixtures/yaml/test2.yaml')
    assert generate_diff(first_file, second_file) == correct_diff
    print("yaml test passed")
