from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from confluent_kafka import Producer
import pymongo
import json
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

class Mongo:

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://mongodb:27017")
        self.mydatabase = self.myclient["mydatabase"]
        self.mycollection = self.mydatabase["message"]

    def findAll(self):
        return self.mycollection.find()

    def save(self, data):
        return self.mycollection.insert_many(data)

class Kafka(Resource):

    def get(self):

        json_data = Mongo().findAll()

        return dumps(json_data)

    def post(self):

        data_source = request.get_json()

        p = Producer({'bootstrap.servers': '127.0.0.1:9092'})

        for data in data_source:
            value = str(json.dumps(data))
            p.poll(0)
            p.produce('mytopic', key=str(1),value=value)

        p.flush()

        Mongo().save(data_source)

        return jsonify(success="ok")

api.add_resource(Kafka, '/kafka')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
