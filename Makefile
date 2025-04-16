sync:
	--all-extras --dev

build:
	uv build

install:
	uv tool install --force dist/*.whl

lint:
	uv tool run ruff check gendiff/

test:
	uv run pytest -s -vvvv

test-cov:
	uv run pytest --cov

test-cov-report:
	uv run pytest --cov-report xml:coverage.xml --cov=gendiff