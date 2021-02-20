#!/usr/bin/env python
import pika
import sys



credentials = pika.PlainCredentials(username='reza', password='reza@123')
connection = pika.BlockingConnection(
pika.ConnectionParameters(host='185.255.91.17',credentials=credentials))
channel = connection.channel()

channel    = connection.channel()
exchange_name = 'user_updates'
routing_key   = 'user.profile.update'

channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
