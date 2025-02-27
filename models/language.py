

class Language:

    @staticmethod
    def get_base(mongo, language: str):
        cursor = mongo.db.get_collection(language)
        configuration = cursor.find_one({"name": "base.html"})
        return configuration

    @staticmethod
    def get_about(mongo, language: str):
        cursor = mongo.db.get_collection(language)
        configuration = cursor.find_one({"name": "about.html"})

        return configuration

    @staticmethod
    def get_portfolio(mongo, language: str):
        cursor = mongo.db.get_collection(language)
        configuration = cursor.find_one({"name": "portfolio.html"})

        return configuration

    @staticmethod
    def get_contact(mongo, language: str):
        cursor = mongo.db.get_collection(language)
        configuration = cursor.find_one({"contact": "contact.html"})

        return configuration

