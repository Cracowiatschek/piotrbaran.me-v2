from flask_pymongo import PyMongo

mongo = PyMongo()

class Universal:
    @staticmethod
    def get_all():
        return list(mongo.db.)