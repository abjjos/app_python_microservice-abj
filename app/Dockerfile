FROM python:3.10.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc libpq-dev postgresql curl

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

COPY poetry.lock /app
COPY pyproject.toml /app

RUN poetry install
