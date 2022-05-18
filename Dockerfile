# syntax=docker/dockerfile:1
FROM python:3.9.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -Ur /project/requirements.txt
COPY ./project /project
