FROM python:slim

RUN apt -y update && apt -y install git
RUN apt -y install diffutils patch
RUN pip install numpy
RUN pip install math

WORKDIR /mnt

