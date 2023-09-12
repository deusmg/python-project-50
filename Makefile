install:
		python3 -m pip install .

build:
		poetry build

lint:
		poetry run flake8