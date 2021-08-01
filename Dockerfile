FROM python:3.9-alpine3.13
LABEL maintainer="piek.ru"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade -pip && \
    /py/bin/install -r /requirements.txt && \ 
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app