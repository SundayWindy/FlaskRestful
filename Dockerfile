FROM python:3.8.6-buster

WORKDIR /home/ruicore/flask_server

COPY . /home/ruicore/flask_server

RUN pip3 install --upgrade pip && pip3 install  -r requirements.txt -i  https://pypi.douban.com/simple/

RUN chmod +x ./scripts

ENTRYPOINT ["bash","./scripts/entrypoint.sh"]

LABEL ruicore="hrui835@gmail.com" version="v.0.0.1"
