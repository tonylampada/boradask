FROM python:2.7
RUN apt-get update
RUN apt-get install nano
RUN pip install dask[complete] bokeh

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY . /usr/src/app
