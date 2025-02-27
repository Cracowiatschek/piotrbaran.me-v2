

class CacheConfig:
    @staticmethod
    def get_config(mongo):
        cursor = mongo.db.get_collection("config")
        configuration = cursor.find_one({"name": "base.html"})

        return configuration
