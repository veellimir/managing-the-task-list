import os

from dotenv import load_dotenv

load_dotenv()

CONFIG__DATABASE_URL = os.getenv("CONFIG__DATABASE_URL")