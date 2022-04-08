import random
from clases.pokemon_earth import PokemonEarth

from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonAir(Pokemon):
    obj_Pokemon = PokemonEarth(1, "Pidgey", WeaponType.PUNCH, 100, 7, 10)

    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating)
    
    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("The parameter points_of_damage should be an int.")

        print("The Pokemon " + self._pokemon_name +
              " has received an attack of " +
              str(points_of_damage) + " points of damage.")

        failure_probability = random.randrange(0, 2)

        if failure_probability == 0:  # Normal defense applied.
            if points_of_damage > self._defense_rating:
                self._health_points = (self._health_points -
                                       (points_of_damage - self._defense_rating))
                pokemon_was_hit = True
            else:
                print("No damage received.")
                pokemon_was_hit = False
        else:
            print("No damage received.")
            pokemon_was_hit = False
        if self._health_points < 1:
            self._health_points = 0

        return pokemon_was_hit