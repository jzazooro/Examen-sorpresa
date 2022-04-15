import random

from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonElectricity(Pokemon):
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating)

    def fight_attack(self, pokemon_to_attack):
        points_of_damage = self._attack_rating

        print("The Pokemon " + self._pokemon_name +
              " hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +
              " with " + str(points_of_damage) + " points of damage!")

        hit_probability = random.randrange(0, 2)

        if hit_probability == 0:
            points_of_damage = self._attack_rating
        else:
            points_of_damage = 2 * self._attack_rating

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit
