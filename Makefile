.PHONY: install test lint format clean docs build release ollama

install:
	poetry install --no-root
	poetry run pre-commit install

test:
	PYTHONPATH=$PYTHONPATH:. poetry run pytest
	

coverage:
	PYTHONPATH=$PYTHONPATH:. poetry run pytest --cov=src tests/ --cov-report=term-missing -cov-report=html:coverage_re
	

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

clean:
	rm -rf build dist .egg *.egg-info
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -type d -name __pycache__ -exec rm -r {} \+

docs:
	poetry run mkdocs build

docs-serve:
	poetry run mkdocs serve

ollama:
	docker compose -f docker-compose-ollama.yml up

#build:
#	poetry build

#release:
#	poetry run semantic-release publish

#ci:
#	make lint
#	make test
#	make docs

update:
	poetry update