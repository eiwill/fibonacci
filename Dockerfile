FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python python-dev python-distribute python-pip python-virtualenv
ADD . /srv/fibonacci

WORKDIR /srv/fibonacci

RUN virtualenv env
RUN env/bin/pip install -r requirements.txt

RUN mkdir -p /var/run

ENV CONFIG_PATH fibonacci.config.Production

ENTRYPOINT env/bin/uwsgi --ini conf.d/fibonacci.ini