import pika

params = pika.URLParameters('amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml')
# params = pika.URLParameters('amqp://localhost:5672/')

try:
    connection = pika.BlockingConnection(params)
except pika.exceptions.AMQPConnectionError as e:
    print("///////////////////////////////////////////////////////////////")
    print(f"Error connecting to RabbitMQ: {e}")
    print("///////////////////////////////////////////////////////////////")
    exit()  # Exit the script if a connection error occurs

# The rest of the code will only be executed if the connection is successful

channel = connection.channel()

queue_name = 'admin'

# Declare the queue (create it if it doesn't exist)
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue=queue_name, on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()
