import os
import pytest
from gendiff.generate_diff import generate_diff

JSON_FILE1_PATH = os.path.join(os.path.dirname(__file__), 'fixtures', 'json_file1.json')
JSON_FILE2_PATH = os.path.join(os.path.dirname(__file__), 'fixtures', 'json_file2.json')

EXPECTED_RESULT = '''{
-  follow: false,
   host: hexlet.io,
-  proxy: 123.234.53.22,
-  timeout: 50
+  timeout: 20,
+  verbose: true
}'''

def test_generate_diff():
    result = generate_diff(JSON_FILE1_PATH, JSON_FILE2_PATH)
    cleaned_result = result.replace(" ", "").replace("\n", "")
    cleaned_expected_result = EXPECTED_RESULT.replace(" ", "").replace("\n", "")
    assert cleaned_result == cleaned_expected_result

if __name__ == '__main__':
    pytest.main()

