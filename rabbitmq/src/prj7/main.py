import pika
import json
from fastapi import FastAPI
from pydantic import BaseModel

import config


class Student(BaseModel):
    first_name: str
    last_name: str
    age: int


app = FastAPI()


@app.post("/student/register/")
async def student_registration(student: Student):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.exchange_declare(
        exchange=config.EXCHANGE_NAME, exchange_type=config.EXCHANGE_TYPE
    )
    message = json.dumps(student.dict())
    channel.basic_publish(
        exchange=config.EXCHANGE_NAME, routing_key="show", body=message
    )

    return student
