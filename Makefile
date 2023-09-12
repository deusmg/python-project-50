install:
		python3 -m pip install .

build:
		poetry build

lint:
		poetry run flake8

test: 
		pytest tests/test_generate_diff.py

test-coverage:
		coverage run -m pytest

