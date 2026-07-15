.PHONY: test run lint format clean compile

run:
	uvicorn backend.app.main:app --reload

test:
	pytest tests/unit -v

compile:
	python -m compileall backend

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:
	ruff check .

format:
	black .