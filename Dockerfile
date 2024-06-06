FROM python:3.11.8

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY . .

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "uvicorn", "src.main:app", "--port", "8080", "--host", "0.0.0.0"]