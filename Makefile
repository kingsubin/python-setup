.PHONY: init
init:
	poetry install --no-root

.PHONY: lint
lint:
	poetry run mypy . && poetry run ruff . --fix

.PHONY: run
run:
	make lint && poetry run uvicorn app.main:app --reload

.PHONY: migrate
migrate:
	poetry run alembic revision --autogenerate -m "migration" && poetry run alembic upgrade head

.PHONY: pre-commit
pre-commit:
	poetry run pre-commit install && poetry run pre-commit run
