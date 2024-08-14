# syntax=docker/dockerfile:1

FROM python:3.12
RUN pip install poetry
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

ENV POETRY_NO_INTERACTION=1 \
POETRY_VIRTUALENVS_IN_PROJECT=1 \
POETRY_VIRTUALENVS_CREATE=true \
POETRY_CACHE_DIR=/tmp/poetry_cache

ENV FLASK_APP=run.py
RUN poetry install
COPY . /app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]