import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")


channel.basic_publish(exchange="direct_logs", routing_key="info", body="info log")
channel.basic_publish(exchange="direct_logs", routing_key="warning", body="warning log")
channel.basic_publish(exchange="direct_logs", routing_key="error", body="error log")

print(" [x] Sent severity logs")

connection.close()
