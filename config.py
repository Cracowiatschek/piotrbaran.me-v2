import os

class Config:
    MONGO_URI: str = os.getenv("MONGO_DB_URI")
    MONGO_DB: str = os.getenv("MONGO_DB")

