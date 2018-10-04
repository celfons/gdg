import pymongo


class Mongo:

    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb://mongodb:27017")
        self.database = self.connection["mydatabase"]
        self.collection = self.database["message"]

    def findAll(self):
        return self.collection.find()

    def save(self, data):
        return self.collection.insert_many(data)
