

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
        configuration = cursor.find_one({"name": "contact.html"})

        return configuration

    @staticmethod
    def get_portfolio_details(mongo, language: str, name: str):
        cursor = mongo.db.get_collection(language)
        configuration = cursor.find_one({"name": name, "context":"details"})

        return configuration

    @staticmethod
    def get_message_content(mongo, language: str):
        cursor = mongo.db.get_collection(language)
        configuration = cursor.find_one({"name": "messageContent.html"})

        return configuration