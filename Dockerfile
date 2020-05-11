FROM ubuntu:latest

# generate workspace
RUN mkdir /workdir

#copy app file to container
COPY app/ /workdir

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN apt-get install -y locales
RUN locale-gen ja_JP.UTF-8
RUN echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

RUN pip3 install mecab-python3
RUN pip3 install oseti

RUN pip3 install flask
RUN pip3 install jinja2