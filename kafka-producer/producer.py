from confluent_kafka import Producer
import json

# Kafka producer configuration
conf = {
    'bootstrap.servers': 'kafka:9092',  # Kafka broker address
}
producer = Producer(conf)

# Read and produce messages from data.json


with open('data.json', 'r') as file:
    data_json = []
    for line in file:
        try:
            # Parse each line as a JSON object
            json_data = json.loads(line.strip())
            data_json.append(json_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    for data in data_json:        
        message_value = json.dumps(data)
        producer.produce('input_topic', value=message_value)
        print(f"MEsaaaageee SENDDD : {message_value}")
# Flush and close the producer
producer.flush()

