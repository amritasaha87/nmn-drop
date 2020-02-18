FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04
RUN apt-get update && yes | apt-get upgrade
RUN apt-get install vim
RUN apt-get install python3.6
RUN apt-get install python3-pip
RUN apt-get install -y git python-pip
RUN pip install --upgrade pip
RUN python --version
RUN pip --version
COPY . /nmn-drop
WORKDIR /nmn-drop
