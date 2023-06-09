from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    return app

app = create_app()

try:
    from src import views, models
    models.db.create_all()

    app.register_blueprint(views.pokemon_api)
except Exception as e:
    import traceback
    traceback.print_exc()
