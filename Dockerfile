FROM python:3.12.4-slim-bookworm

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
