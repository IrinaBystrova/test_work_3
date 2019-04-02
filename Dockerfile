FROM python:3.7

ENV PYTHONUMBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install pipenv && pipenv install --system
