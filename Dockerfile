FROM python:3.7-alpine
LABEL MAINTAINER baverkacar

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# minimazing docker file with --no-cache
RUN apk add --update --no-cache postgresql-client 
# temp build dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user