install:
	@poetry install

lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest --cov=gendiff --cov-report xml tests/

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	@poetry build

publish: build
	@poetry publish -r test_pypi