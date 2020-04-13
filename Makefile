install:
	@poetry install

lint:
	@poetry run flake8 gendiff

build:
	@poetry build

publish:
	@poetry publish -r test_pypi