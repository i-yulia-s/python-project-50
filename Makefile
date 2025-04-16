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