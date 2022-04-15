from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonWater(Pokemon):
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         10, defense_rating)

        if isinstance(attack_rating, int):
            if 11 <= attack_rating <= 20:
                self._attack_rating = attack_rating
            else:
                raise ValueError("The parameter attack_rating should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter attack_rating should be a int.")

    def set_attack_rating(self, attack_rating_to_be_set):
        if isinstance(attack_rating_to_be_set, int):
            if 11 <= attack_rating_to_be_set <= 20:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")
