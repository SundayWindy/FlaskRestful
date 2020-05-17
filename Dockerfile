FROM python:3.8.3-buster

EXPOSE 24579

EXPOSE 3306

MAINTAINER ruicore <hrui835@gmail.com>

RUN mkdir -p /home/ruicore/flask_server

WORKDIR /home/ruicore/flask_server

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt -i https://pypi.doubanio.com/simple

COPY . /home/ruicore/flask_server

CMD ["python", "server.py"]