install:
	@poetry install

lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest gendiff tests

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	@poetry build

publish: build
	@poetry publish -r test_pypi