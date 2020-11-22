install:
	@poetry install

lint:
	poetry run flake8 gendiff

coverage:
	poetry run coverage run gendiff/scripts/main.py gendiff/json_file1.json gendiff/json_file2.json
	poetry run coverage xml