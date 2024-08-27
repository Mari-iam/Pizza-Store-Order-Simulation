import json
from faker import Faker
from pizzaproducer import PizzaProvider
from kafka import KafkaProducer

fake = Faker()
fake.add_provider(PizzaProvider)

folderName = "./"
producer = KafkaProducer(
    bootstrap_servers="your-server-ID",
    security_protocol="SSL",
    ssl_cafile=folderName+"file.pem",
    ssl_certfile=folderName+"file.cert",
    ssl_keyfile=folderName+"file.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')

)

for i in range(0, 10):
    order = {
        "Customer ID": fake.customer_id(),
        "Customer Name": fake.customer_name(),
        "Phone Number": fake.customer_phone(),
        "Customer Address": fake.customer_address(),
        "Pizza Ordered": fake.pizza_name(),
        "Toppings": fake.pizza_toppings(),
        "Order Date & Time": fake.order_datetime().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Send the order data to the Kafka topic (replace 'pizza_orders' with your topic name)
    producer.send('pizza_orders', value=order)
    print(f"Sent order: {order}")

# Ensure all messages are sent before closing the producer
producer.flush()
producer.close()
