import time
import json
from kafka import KafkaConsumer

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers='kafka:9092',  # Ensure this matches your Kafka service address
    auto_offset_reset='earliest',     # Start reading at the beginning of the topic
    enable_auto_commit=True,          # Automatically commit offsets
    group_id='consumer-group-1',      # Consumer group name
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def main():
    for message in consumer:
        event = message.value
        print("Received event:", event)
        # Here, you could process the event further (e.g., save to a database)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
