import pymongo

class Mongo:

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://mongodb:27017")
        self.mydatabase = self.myclient["mydatabase"]
        self.mycollection = self.mydatabase["message"]

    def findAll(self):
        return self.mycollection.find()

    def save(self, data):
        return self.mycollection.insert_many(data)