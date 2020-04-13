install:
	@poetry install

lint:
	@poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

publish: build
	@poetry publish -r test_pypi