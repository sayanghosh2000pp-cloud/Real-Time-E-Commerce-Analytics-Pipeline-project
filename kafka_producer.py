from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    transaction = {
        "order_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 100),
        "amount": round(random.uniform(10.0, 500.0), 2),
        "category": random.choice(["Electronics", "Clothing", "Books", "Groceries"]),
        "timestamp": time.time()
    }
    producer.send('transactions', value=transaction)
    print(f"Sent: {transaction}")
    time.sleep(2)
