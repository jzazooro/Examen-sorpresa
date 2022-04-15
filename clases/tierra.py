from weapon_type import WeaponType
from pokemon import Pokemon
class PokemonEarth(Pokemon):
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, 10)

        if isinstance(defense_rating, int):
            if 11 <= defense_rating <= 20:
                self._defense_rating = defense_rating
            else:
                raise ValueError("The parameter defense_rating should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating should be a int.")


    def set_defense_rating(self, defense_rating_to_be_set):
        if isinstance(defense_rating_to_be_set, int):
            if 11 <= defense_rating_to_be_set <= 20:
                self._defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("The parameter defense_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a int.")