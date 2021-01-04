install:
	@poetry install

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest -v

coverage:
	poetry run pytest --cov=gendiff --cov-report xml
