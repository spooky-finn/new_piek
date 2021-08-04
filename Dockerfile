# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1

# RUN apt update && apt install postgresql-dev gcc python3-dev musl-dev


WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
# CMD ["python", 'manage.py', 'migrate']
# CMD ["python", 'manage.py', 'runserver', '0.0.0.0:8000']