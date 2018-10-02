from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from confluent_kafka import Producer
import pymongo
import json
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

myclient = pymongo.MongoClient("mongodb://0.0.0.0:27017")
mydatabase = myclient["mydatabase"]
mycollection = mydatabase["message"]

class Kafka(Resource):

    def get(self):

        json_data = mycollection.find()

        return dumps(json_data)

    def post(self):

        data_source = request.get_json()

        p = Producer({'bootstrap.servers': '127.0.0.1:9092'})

        key = 0
        for data in data_source:
            key+=1
            value = str(json.dumps(data))
            p.poll(0)
            p.produce('mytopic', key=str(key),value=value)

        p.flush()

        mycollection.insert_many(data_source)


        return jsonify(success="ok")

api.add_resource(Kafka, '/kafka')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
