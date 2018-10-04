FROM python:3
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN python3 -m pip install -r requirements.txt
ADD . /code/
