import pytest
import json
from gendiff.compare import compare_flat


@pytest.fixture
def data1():
    return json.load(open('file1.json'))

@pytest.fixture
def data2():
    return json.load(open('file2.json'))

def test_compare_flat(data1, data2):

    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert compare_flat(data1, data2) == expected        
