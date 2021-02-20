#!/usr/bin/env python
import pika
import sys
credentials = pika.PlainCredentials(username='reza', password='reza@123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='185.255.91.17',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

channel = connection.channel()

channel.queue_declare(queue='hi', durable=True)

channel.basic_publish(exchange='', routing_key='hi', body='Test!')
print(" [x] Sent 'Test!'")
connection.close()
