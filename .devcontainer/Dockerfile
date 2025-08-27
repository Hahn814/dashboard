FROM python:3-bookworm

ARG DEBIAN_FRONTEND=noninteractive
ARG ENV=development

WORKDIR /usr/src/app
COPY ./requirements ./requirements

RUN pip install --no-cache-dir -r requirements/${ENV}.txt
