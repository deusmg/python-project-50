from gendiff import generate_diff
from tests import FIXTURES_PATH
import pytest


@pytest.mark.parametrize("file1, file2, expected_path, format", [
    (
        f"{FIXTURES_PATH}/json_file1.json",
        f"{FIXTURES_PATH}/json_file2.json",
        f"{FIXTURES_PATH}/expected_for_example.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/yml_file1.yml",
        f"{FIXTURES_PATH}/yml_file2.yml",
        f"{FIXTURES_PATH}/expected_for_example.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/expected_for_stylish.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/file1.yml",
        f"{FIXTURES_PATH}/file2.yml",
        f"{FIXTURES_PATH}/expected_for_stylish.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/expected_for_plain.txt",
        "plain"
    ),
    (
        f"{FIXTURES_PATH}/file1.yml",
        f"{FIXTURES_PATH}/file2.yml",
        f"{FIXTURES_PATH}/expected_for_plain.txt",
        "plain"
    )])
# ])
def test_generate_diff(file1, file2, expected_path, format):
    with open(expected_path, "r") as result:
        assert result.read().strip() == generate_diff(file1, file2, format)
