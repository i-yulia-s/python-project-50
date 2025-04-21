import pytest
from gendiff.scripts.main import main

@pytest.fixture
def expected():
    with open('tests/test_data/expected_flat.txt') as file:
        return file.read()

def test_main(expected):
    assert main(['tests/test_data/file1.json', \
                'tests/test_data/file2.json']) == expected
    assert main(['tests/test_data/file1.yml', \
                'tests/test_data/file2.yaml']) == expected
    with pytest.raises(SystemExit):
        main(['tests/test_data/file1.json'])
