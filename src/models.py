# Installed imoports
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

from flask_migrate import Migrate


# Custom imports
from src import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)


@dataclass
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False, unique=True)
    type_1 = db.Column(db.String(100), nullable=True)
    type_2 = db.Column(db.String(100), nullable=True)
    total = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    sp_atk = db.Column(db.Integer)
    sp_def = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    generation = db.Column(db.Integer)
    legendary = db.Column(db.Boolean)


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
