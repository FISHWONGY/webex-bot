FROM python:3.9.6-slim

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.4.2

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/install.python-poetry.org/07ccfe459b6b5c3b3b8859f5cf643c62591d2ea6/install-poetry.py | python3 - ;

ENV PATH="/root/.local/bin:$PATH"
COPY ./poetry.lock pyproject.toml /usr/src/app/
RUN poetry install -nv --no-root

COPY app .
CMD ["poetry", "run", "python3", "main.py"]