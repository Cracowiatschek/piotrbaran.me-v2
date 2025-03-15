import os
import secrets

class Config:
    MONGO_URI: str = os.getenv("MONGO_DB_URI")
    MONGO_DB: str = os.getenv("MONGO_DB")
    SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY")
    SENDER_EMAIL: str = "kontakt@piotrbaran.me"
    SECRET_KEY: str = secrets.token_hex(32)
