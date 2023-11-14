.PHONY: init
init:
	poetry install --no-root

.PHONY: lint
lint:
	poetry run mypy . && poetry run ruff .

.PHONY: pre-commit
pre-commit:
	poetry run pre-commit install && poetry run pre-commit run
