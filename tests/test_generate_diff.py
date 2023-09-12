import os
import pytest
from gendiff.generate_diff import generate_diff

J_F1_P = os.path.join(os.path.dirname(__file__), 'fixtures', 'json_file1.json')
J_F2_P = os.path.join(os.path.dirname(__file__), 'fixtures', 'json_file2.json')

EXPECTED_RESULT = '''{
-  follow: false,
   host: hexlet.io,
-  proxy: 123.234.53.22,
-  timeout: 50
+  timeout: 20,
+  verbose: true
}'''


def test_generate_diff():
    result = generate_diff(J_F1_P, J_F2_P)
    cleaned_result = result.replace(" ", "").replace("\n", "")
    cleaned_expected_result = EXPECTED_RESULT.replace(" ", "").replace("\n", "")
    assert cleaned_result == cleaned_expected_result


if __name__ == '__main__':
    pytest.main()
