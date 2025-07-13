import pytest
import json
from gendiff.compare import compare_flat, compare


@pytest.fixture
def file1_flat():
    return json.load(open('tests/test_data/file1_flat.json'))

@pytest.fixture
def file2_flat():
    return json.load(open('tests/test_data/file2_flat.json'))

@pytest.fixture
def expected_flat():
    with open('tests/test_data/expected_flat.txt') as file:
      return file.read()
     

def test_compare_flat(file1_flat, file2_flat, expected_flat):
    assert compare_flat(file1_flat, file2_flat) == expected_flat        


@pytest.fixture
def file1():
    return json.load(open('tests/test_data/file1.json'))

@pytest.fixture
def file2():
    return json.load(open('tests/test_data/file2.json'))

@pytest.fixture
def expected_diff():
    with open('tests/test_data/expected_diff.txt') as file:
      return file.read()


def test_compare(file1, file2, expected_diff):
    assert compare(file1, file2) == expected_diff