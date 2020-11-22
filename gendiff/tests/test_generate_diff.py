from gendiff.get_data import get_data
from gendiff.gendiff import generate_diff


def test_generate_diff():
    correct_diff = open('gendiff/tests/fixtures/correct_answer_json.txt').read()  # 1
    first_file = get_data('gendiff/tests/fixtures/test_json1.json')
    second_file = get_data('gendiff/tests/fixtures/test_json2.json')
    assert generate_diff(first_file, second_file) == correct_diff
    print("json test passed")
