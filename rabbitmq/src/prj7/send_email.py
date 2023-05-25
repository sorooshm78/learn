import pika
import sys
import json
import smtplib


exchange_name = "student"
exchange_type = "direct"
queue_name = "email"
routing_key = "send_mail"

sender = "user@mail.com"
password = "password"


def send_email(sender, password, receiver, message):
    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login(sender, password)
    session.sendmail(sender, receiver, message)
    session.quit()


def message_callback(ch, method, properties, body):
    data = json.loads(body)

    full_name = f'{data["first_name"]} {data["last_name"]}'
    receiver = data["mail"]
    message = f"Hello dear {full_name}"

    send_email(sender, password, receiver, message)
    print(f" [x] Send mail to {receiver}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

result = channel.queue_declare(queue=queue_name)
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

print(" [*] Waiting for data. To exit press CTRL+C")
channel.basic_consume(
    queue=queue_name,
    on_message_callback=message_callback,
)
channel.start_consuming()
