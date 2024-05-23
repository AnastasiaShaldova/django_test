FROM python:3.10
WORKDIR /usr/src/app

COPY backend/ ./backend
COPY pyproject.toml poetry.lock .env .

RUN pip install -U --pre pip poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
