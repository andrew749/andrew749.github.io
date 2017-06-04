FROM ubuntu:16.04
MAINTAINER Andrew Codispoti "andrew.codispoti@gmail.com"
RUN apt-get update
RUN apt-get install -y python3 python3-pip vim less grep ruby-dev build-essential
RUN gem install sass
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
ADD . /var/app

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV FLASK_APP /var/app/app.py
ENV FLASK_DEBUG False
WORKDIR /var/app
RUN ["make", "build_css"]

EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]

