from confluent_kafka import Producer
import json


class KafkaService:

    def __init__(self):
        pass

    def producer(self, data_source):
        p = Producer({'bootstrap.servers': 'kafka:9092'})

        for data in data_source:
            value = str(json.dumps(data))
            p.poll(0)
            p.produce('mytopic', key=str(1), value=value)

        p.flush()
