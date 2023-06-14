from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    return app


app = create_app()

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

try:
    from src import views, models

    app.register_blueprint(views.pokemon_api)
    app.app_context().push()
except Exception as e:
    import traceback

    traceback.print_exc()
