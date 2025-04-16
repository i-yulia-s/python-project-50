import pytest
import json
from gendiff.compare import compare_flat


@pytest.fixture
def data1():
    return json.load(open('tests/test_data/file1.json'))

@pytest.fixture
def data2():
    return json.load(open('tests/test_data/file2.json'))

@pytest.fixture
def expected():
    with open('tests/test_data/expected_flat.txt') as file:
      return file.read()
     

def test_compare_flat(data1, data2, expected):
    assert compare_flat(data1, data2) == expected        
