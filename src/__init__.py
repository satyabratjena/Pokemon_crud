from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_migrate import Migrate



app = Flask(__name__)

app.config.from_pyfile("config.py")

from src import views, models
app.app_context().push()
# models.db.create_all()
app.register_blueprint(views.pokemon_api)
