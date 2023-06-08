import os

SECRET_KEY = "secret_cheat"
SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://postgres:password@localhost:5432/pokemon_db"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
BASE_URL = "http://127.0.0.1:5000"
PAGE_LIMIT = 10000
