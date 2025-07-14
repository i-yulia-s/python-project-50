import pytest
from gendiff.scripts.main import main

@pytest.fixture
def expected_flat():
    with open('tests/test_data/expected_flat.txt') as file:
        return file.read()


@pytest.fixture
def expected():
    with open('tests/test_data/expected.txt') as file:
        return file.read()
    

def test_main(expected_flat, expected):
    assert main(['tests/test_data/file1_flat.json', \
                'tests/test_data/file2_flat.json']) == expected_flat
    assert main(['tests/test_data/file1_flat.yml', \
                'tests/test_data/file2_flat.yaml']) == expected_flat
    assert main(['tests/test_data/file1.json', \
                'tests/test_data/file2.json', \
                '--format', 'stylish']) == expected
    assert main(['tests/test_data/file1.yaml', \
                'tests/test_data/file2.yaml', \
                '--format', 'stylish']) == expected
    with pytest.raises(SystemExit):
        main(['tests/test_data/file1.json'])
