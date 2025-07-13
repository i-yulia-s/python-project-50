import pytest
from gendiff.scripts.main import main

@pytest.fixture
def expected():
    with open('tests/test_data/expected_flat.txt') as file:
        return file.read()

def test_main(expected):
    assert main(['tests/test_data/file1_flat.json', \
                'tests/test_data/file2_flat.json']) == expected
    assert main(['tests/test_data/file1_flat.yml', \
                'tests/test_data/file2_flat.yaml']) == expected
    with pytest.raises(SystemExit):
        main(['tests/test_data/file1.json'])
