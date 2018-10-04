from confluent_kafka import Producer
import json

class Kafka:

    def __init__(self, data_source):
        self.data_source = data_source

    def producer(self, data_source):

        p = Producer({'bootstrap.servers': '127.0.0.1:9092'})

        for data in data_source:
            value = str(json.dumps(data))
            p.poll(0)
            p.produce('mytopic', key=str(1),value=value)

        p.flush()

