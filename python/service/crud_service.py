from repository.mongo import Mongo


class Service:

    def __init__(self):
        pass

    def save(self):
        Mongo().save(self)

    def get(self):
        return Mongo().findAll()
