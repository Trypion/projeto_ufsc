import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "NMgh\x98\x87zrqj\xde\x8b\x81\xf8c|u\x84\x119v\xb4}\xc1")
CONNECTION_URI = os.getenv("CONNECTION_URI", "mongodb://localhost:27017/")
DATABASE = os.getenv("DATABASE", "pinga")