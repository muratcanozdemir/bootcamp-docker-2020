FROM python:3.8-slim-buster

RUN apt-get update --fix-missing \
    && apt-get -y install --no-install-recommends \
        bash \
        iputils-ping \
    && pip install --upgrade pip \
    && python -m pip install \
        boto==2.49 \
        flask==1.1.1 \
    && rm -rf /root/.cache/* \
    && rm -rf /var/lib/apt/lists/*

COPY ./dynamodb-tictactoe-example-app /app

WORKDIR /app
