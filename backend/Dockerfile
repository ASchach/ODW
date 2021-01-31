FROM python:3.9

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install Flask
RUN pip3 install Flask_mysqldb
RUN pip3 install mysql.connector


WORKDIR /service
COPY app.py /service
COPY requirements.txt /service

CMD ["python3", "./app.py"]

