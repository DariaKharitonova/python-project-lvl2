import pytest


@pytest.fixture()
def simple_before_json():
    return 'tests/fixtures/simple/before.json'


@pytest.fixture()
def simple_after_json():
    return 'tests/fixtures/simple/after.json'


@pytest.fixture()
def simple_before_yaml():
    return 'tests/fixtures/simple/before.yaml'


@pytest.fixture()
def simple_after_yaml():
    return 'tests/fixtures/simple/after.yaml'


@pytest.fixture()
def complex_before_json():
    return 'tests/fixtures/complex/before.json'


@pytest.fixture()
def complex_after_json():
    return 'tests/fixtures/complex/after.json'


@pytest.fixture()
def complex_before_yaml():
    return 'tests/fixtures/complex/before.yaml'


@pytest.fixture()
def complex_after_yaml():
    return 'tests/fixtures/complex/after.yaml'


@pytest.fixture()
def result_complex_json():
    return 'tests/fixtures/complex/complex_json.json'


@pytest.fixture()
def result_complex_plain():
    return 'tests/fixtures/complex/complex_plain.txt'


@pytest.fixture()
def result_complex_stylish():
    return 'tests/fixtures/complex/complex_stylish.txt'


@pytest.fixture()
def result_simple_json():
    return 'tests/fixtures/simple/simple_json.json'


@pytest.fixture()
def result_simple_plain():
    return 'tests/fixtures/simple/simple_plain.txt'


@pytest.fixture()
def result_simple_stylish():
    return 'tests/fixtures/simple/simple_stylish.txt'
