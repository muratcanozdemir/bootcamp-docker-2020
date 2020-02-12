FROM python:3.7-slim-stretch

COPY Pipfile .
RUN apt-get update --fix-missing \
    && apt-get -y install --no-install-recommends \
        bash \
        jq \
        curl \
        git \
        software-properties-common \
        build-essential \
        groff \
        zip \
        unzip \
    && python -m pip install \
        pipenv==2018.11.26

RUN pipenv install && pipenv install --system

COPY files/profile /etc/
COPY files/*.sh /etc/profile.d/

COPY app /app

WORKDIR /app
