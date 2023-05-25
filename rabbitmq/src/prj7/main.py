import pika
import json
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


exchange_name = "student"
exchange_type = "direct"


class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    mail: EmailStr


app = FastAPI()


@app.post("/student/register/")
async def student_registration(student: Student):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)
    data = json.dumps(student.dict())
    channel.basic_publish(exchange=exchange_name, routing_key="send_mail", body=data)

    return student
