from confluent_kafka import Consumer, KafkaError
from cassandra.cluster import Cluster
import json
from decimal import Decimal
import time


# Define the VAT rates
VAT_RATES = {
    "cold food": Decimal("0.07"),
    "hot food": Decimal("0.15"),
    "beverage": Decimal("0.09"),
}

def calculate_net_merchandise_value(order):
    net_value = Decimal(0)
    for item in order["basket"]:
        product_type = item["productType"]
        gross_value = Decimal(item["grossMerchandiseValueEur"])
        vat_rate = VAT_RATES.get(product_type, Decimal("0.0"))
        net_value += gross_value / (1 + vat_rate)
    return net_value

# Kafka consumer configuration
conf = {
    'bootstrap.servers': 'kafka:9092',  # Kafka broker address
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['input_topic'])

cassandra_host = 'cassandra'
# Cassandra connection
# max_retries = 10
# delay = 10

# for i in range(max_retries):
#     try:    
#         time.sleep(delay)
#         cluster = Cluster([cassandra_host])
#         session = cluster.connect()
#         break
#     except e:
#         print(f"Error while connecting {e}")


cluster = Cluster([cassandra_host])
session = cluster.connect()
session.execute("CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.set_keyspace('my_keyspace')
session.execute("CREATE TABLE IF NOT EXISTS merchandise_data (order_id TEXT PRIMARY KEY, net_value DECIMAL)")

# Define a variable to keep track of processed messages
processed_messages = 0
max_processed_messages = 100  # Change this to your desired limit

# ETL and data storage logic
while processed_messages < max_processed_messages:
    message = consumer.poll(1.0)  # Poll for messages every 1 second (adjust as needed)
    if message is None:
        continue
    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"Error: {message.error()}")
    else:
        value = json.loads(message.value())
        print(f"Value : {value}")
        order_id = value["orderId"]
        net_value = calculate_net_merchandise_value(value)
        print(f" Received : {net_value}")
        # Insert data into Cassandra
        session.execute(
            "INSERT INTO merchandise_data (order_id, net_value) VALUES (%s, %s)",
            (order_id, net_value)
        )
        processed_messages += 1

cluster.shutdown()
