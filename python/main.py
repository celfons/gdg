from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from bson.json_util import dumps
from mongo import Mongo
from kafka import Kafka

app = Flask(__name__)
api = Api(app)

class Kafka(Resource):

    def get(self):

        json_data = Mongo().findAll()

        return dumps(json_data)

    def post(self):

        data_source = request.get_json()

        Kafka().producer(data_source)

        Mongo().save(data_source)

        return jsonify(success="ok")

api.add_resource(Kafka, '/kafka')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
