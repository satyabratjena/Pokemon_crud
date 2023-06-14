# Installed imports

from dataclasses import dataclass


# Custom imports
from src import app
from src import db, ma


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


@dataclass
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False, unique=True)
    department = db.Column(db.String(100), nullable=True)
    client_source = db.Column(db.String(100), nullable=True)


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
