FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app
COPY send_email.py  /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD python3 send_email.py