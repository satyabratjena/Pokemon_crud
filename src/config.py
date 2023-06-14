import os
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "serverbase.cfg"))

DEBUG = config.getboolean("FLASK", "DEBUG")
BASE_URL = config.get("FLASK", "BASE_URL")
SECRET_KEY = config.get("FLASK", "SECRET_KEY")
MAX_PAGE_LIMIT = config.getint("FLASK", "MAX_PAGE_LIMIT")
SQLALCHEMY_TRACK_MODIFICATIONS = config.get("FLASK", "SQLALCHEMY_TRACK_MODIFICATIONS")
SQLALCHEMY_DATABASE_URI = config.get("FLASK", "SQLALCHEMY_DATABASE_URI")
