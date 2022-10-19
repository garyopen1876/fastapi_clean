FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root --no-dev

COPY .env /app/
COPY /app /app/app/
COPY /alembic /app/app/
COPY alembic.ini /app/

CMD ["uvicorn", "app.main:app", "--reload", "--env-file=.env", "--host","0.0.0.0", "--port", "8000"]