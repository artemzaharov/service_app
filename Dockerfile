FROM python:3.9-alpine3.16

COPY requirements.txt /tmp/requirements.txt
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /tmp/requirements.txt 
RUN adduser --disabled-password service-user
USER service-user
COPY service /tmp/service
WORKDIR /service
EXPOSE 8000

