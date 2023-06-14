from src.models import db


def update_pokemon_attributes(pokemon, data):
    existing_attributes = {
        "name": pokemon.name,
        "type_1": pokemon.type_1,
        "type_2": pokemon.type_2,
        "total": pokemon.total,
        "hp": pokemon.hp,
        "attack": pokemon.attack,
        "sp_atk": pokemon.sp_atk,
        "sp_def": pokemon.sp_def,
        "speed": pokemon.speed,
        "generation": pokemon.generation,
        "legendary": pokemon.legendary,
    }
    for attribute in existing_attributes:
        if attribute in data:
            setattr(pokemon, attribute, existing_attributes[attribute])

    db.session.add(pokemon)
    db.session.commit()
