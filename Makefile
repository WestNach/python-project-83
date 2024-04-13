PORT ?= 8000
dev:
	poetry run flask --app page_analyzer:app run

install:
	poetry install

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

test-coverage:
	poetry run pytest --cov=page_analyzer --cov-report xml tests/
