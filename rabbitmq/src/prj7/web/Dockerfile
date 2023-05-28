FROM python:3.10-slim

WORKDIR /web

COPY main.py /web
COPY requirements.txt /web

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD uvicorn main:app --reload --host 0.0.0.0