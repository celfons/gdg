from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from bson.json_util import dumps
from services.kafka import KafkaService
from services.crud_service import Service

app = Flask(__name__)
api = Api(app)


class Kafka(Resource):

    def get(self):

        json_data = Service().get()

        return dumps(json_data)

    def post(self):

        data_source = request.get_json()

        Service.save(data_source)

        KafkaService().producer(data_source)

        return jsonify(success="ok")


api.add_resource(Kafka, '/kafka')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
