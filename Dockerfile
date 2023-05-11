FROM python:3.11-bullseye

WORKDIR /home/ruicore/flask_server

COPY . /home/ruicore/flask_server

RUN pip3 install --upgrade pip && pip3 install  -r requirements.txt

LABEL ruicore="hrui835@gmail.com" version="v1.1.0"
