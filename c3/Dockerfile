FROM python:3.8-alpine

RUN apk add --no-cache --virtual .for-build gcc libc-dev && \
    pip install regex && \
    apk del --purge .for-build
