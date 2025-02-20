import time
import json
import random
from kafka import KafkaProducer

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # Assumes a Kubernetes Service named "kafka" exposes Kafka on port 9092
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_event():
    event = {
        "userId": random.randint(1, 1000),
        "eventType": random.choice(["view", "click", "purchase"]),
        "productId": random.randint(1, 100),
        "timestamp": time.time()
    }
    return event

def main():
    topic = 'user-events'
    while True:
        event = generate_event()
        print("Sending event:", event)
        producer.send(topic, event)
        producer.flush()  # Ensure the message is sent
        time.sleep(1)  # Pause before sending the next event

if __name__ == "__main__":
    main()
