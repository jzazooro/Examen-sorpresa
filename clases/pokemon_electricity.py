import random
from clases.pokemon_earth import PokemonEarth

from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonElectricity(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = PokemonElectricity(id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)

    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------

    Example
    -------
"""
from pokemon import Pokemon
from weapon_type import WeaponType
obj_Pokemon = PokemonElectricity(1, "Pikachu", WeaponType.PUNCH, 100, 7, 10)


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        """Constructor of the class.

        This special method is executed when an object of this class is
        created.

        Syntax
        ------
          [ ] = __init__(self, id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_id ID of Pokemon.
          [in] pokemon_name Name of the Pokemon.
          [in] weapon_type Type of weapon that carries out the Pokemon.
          [in] health_points Points of health that the Pokemon has.
          [in] attack_rating Attack rating of the Pokemon.
          [in] defense_rating Defense rating of the Pokemon.

        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Pokemon.

        Exceptions
        ----------
          TypeError:
            If the parameter id is NOT a int.
            If the parameter pokemon_name is NOT a String.
            If the parameter weapon_type is NOT a enum WeaponType.
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.

          ValueError:
            If the parameter id is already found in other Pokemon.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
        """

        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)


    def fight_attack(self, pokemon_to_attack):
        """Method to attack using a hit to other Pokemon.

        Method that implements the attack of the Pokemon using a hit over other
        Pokemon.

        Syntax
        ------
          [ ] = obj_Pokemon.fight_attack(pokemon_to_attack)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] Pokemon pokemon_to_attack Pokemon to hit to.

        Returns
        -------

        Exceptions
        ----------
        TypeError If the parameter pokemon_to_attack is NOT a Pokemon.
        """

        points_of_damage = self._attack_rating

        print("The Pokemon " + self._pokemon_name +
              " hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +
              " with " + str(points_of_damage) + " points of damage!")

        hit_probability = random.randrange(0, 2)

        if hit_probability == 0:  # Normal attack applied.
            points_of_damage = self._attack_rating
        else:  # Special attack applied.
            points_of_damage = 2 * self._attack_rating

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit