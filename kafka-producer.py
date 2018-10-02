from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from confluent_kafka import Producer
import json

app = Flask(__name__)
api = Api(app)

class Kafka(Resource):

    def post(self):

        data_source = request.get_json()

        p = Producer({'bootstrap.servers': '127.0.0.1:9092'})

        def delivery_report(err, msg):

            if err is not None:
                print('Message delivery failed: {}'.format(err))
            else:
                print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

        key = 0
        for data in data_source:
            key+=1
            value = str(json.dumps(data))
            p.poll(0)
            p.produce('mytopic', key=str(key),value=value, callback=delivery_report)

        p.flush()

        return jsonify(data_source)

api.add_resource(Kafka, '/kafka')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
