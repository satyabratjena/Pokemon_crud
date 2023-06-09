# Installed imports
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

from flask_migrate import Migrate


# Custom imports
from src import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

app.app_context().push()

migrate = Migrate(app, db)


@dataclass
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False, unique=True)
    type_1 = db.Column(db.String(100), nullable=True)
    type_2 = db.Column(db.String(100), nullable=True)
    total = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    sp_atk = db.Column(db.Integer, nullable=False)
    sp_def = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    generation = db.Column(db.Integer, nullable=False)
    legendary = db.Column(db.Boolean, nullable=False)


class PokemonSchema(ma.Schema):
    class Meta:
        fields = (
            "rank",
            "name",
            "type_1",
            "type_2",
            "total",
            "hp",
            "attack",
            "defense",
            "sp_atk",
            "sp_def",
            "speed",
            "generation",
            "legendary",
        )


pokemon_schema = PokemonSchema()
