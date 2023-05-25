import pika
import sys
import json

import config

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(
    exchange=config.EXCHANGE_NAME, exchange_type=config.EXCHANGE_TYPE
)


queue_name = "show_queue"
routing_key = "show"

result = channel.queue_declare(queue=queue_name)
channel.queue_bind(
    exchange=config.EXCHANGE_NAME, queue=queue_name, routing_key=routing_key
)


def show_info(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, json.loads(body)))


print(" [*] Waiting for data. To exit press CTRL+C")s
channel.basic_consume(queue=queue_name, on_message_callback=show_info, auto_ack=True)
channel.start_consuming()
