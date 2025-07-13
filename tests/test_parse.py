from gendiff.parse import parse_args, get_format, open_file
import pytest


@pytest.fixture
def dict1():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

def test_parse_args():
    args1 = parse_args(['tests/test_data/file1.json', \
                       'tests/test_data/file2.json'])
    assert args1.first_file == 'tests/test_data/file1.json'
    assert args1.second_file == 'tests/test_data/file2.json'
    with pytest.raises(Exception):
        args2 = parse_args(['tests/test_data/file1.json'])


def test_get_format():
    assert get_format('myfile.json') == 'json'
    assert get_format('my.file.json') == 'json'
    with pytest.raises(Exception):
        get_format('myfilejson')
    assert get_format('myfile.yaml') == 'yaml'
    assert get_format('myfile.yml') == 'yaml'
    with pytest.raises(Exception):
        get_format('myfile.txt')

def test_open_file(dict1):
    assert open_file('tests/test_data/file1_flat.json') == dict1
    assert open_file('tests/test_data/file1_flat.yml') == dict1
    with pytest.raises(SystemExit):
        open_file('tests/test_data/file3.json')
    with pytest.raises(SystemExit):
        open_file('tests/test_data/file3.yml')
    with pytest.raises(SystemExit):
        open_file('tests/test_data/file1json')
