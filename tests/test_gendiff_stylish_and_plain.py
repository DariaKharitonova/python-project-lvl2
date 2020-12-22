from gendiff.get_tree_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from tests.helpers import read_json, read_yaml
import pytest


@pytest.fixture(params=[
    (
        stylish,
        read_json('tests/fixtures/complex/complex_before.json'),
        read_json('tests/fixtures/complex/complex_after.json'),
        open('tests/fixtures/complex/txt.txt').read()
    ),
    (
        stylish,
        read_yaml('tests/fixtures/complex/complex_before.yaml'),
        read_yaml('tests/fixtures/complex/complex_after.yaml'),
        open('tests/fixtures/complex//txt.txt').read()
    ),
    (
        plain,
        read_json('tests/fixtures/complex/complex_before.json'),
        read_json('tests/fixtures/complex/complex_after.json'),
        open('tests/fixtures/complex//plain.txt').read()
    ),
    (
        plain,
        read_yaml('tests/fixtures/complex/complex_before.yaml'),
        read_yaml('tests/fixtures/complex/complex_after.yaml'),
        open('tests/fixtures/complex//plain.txt').read()
    ),
    (
        stylish,
        read_json('tests/fixtures/simple/before.json'),
        read_json('tests/fixtures/simple/after.json'),
        open('tests/fixtures/simple/simple_txt.txt').read()
    ),
    (
        stylish,
        read_json('tests/fixtures/simple/before.json'),
        read_json('tests/fixtures/simple/bool_and_null_in_keys.json'),
        open('tests/fixtures/simple/bool_and_null_in_keys_result.txt').read()
    ),
    (
        stylish,
        read_yaml('tests/fixtures/simple/before.yaml'),
        read_yaml('tests/fixtures/simple/after.yaml'),
        open('tests/fixtures/simple/simple_txt.txt').read()
    ),
    (
        plain,
        read_json('tests/fixtures/simple/before.json'),
        read_json('tests/fixtures/simple/after.json'),
        open('tests/fixtures/simple/simple_plain.txt').read()
    ),
    (
        plain,
        read_yaml('tests/fixtures/simple/before.yaml'),
        read_yaml('tests/fixtures/simple/after.yaml'),
        open('tests/fixtures/simple/simple_plain.txt').read()
    )
])
def parameters_test(request):
    return request.param


def test_diff(parameters_test):
    formatter, first_file, second_file, correct = parameters_test
    assert formatter(get_diff(first_file, second_file)) == correct
