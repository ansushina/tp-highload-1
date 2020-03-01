FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python3

COPY . /server
EXPOSE 80
WORKDIR /server 
CMD python3 ./main.py