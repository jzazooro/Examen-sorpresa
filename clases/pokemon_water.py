from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonWater(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = PokemonWater(id, pokemon_name, weapon_type, health_points,
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
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = PokemonWater(1, "Squirtle", WeaponType.PUNCH, 100, 7, 10)
    """


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

        Example
        -------
          >>> from pokemon import Pokemon
          >>> from weapon_type import WeaponType
          >>> obj_Pokemon = PokemonWater(1, "Squirtle", WeaponType.PUNCH, 100, 7, 10)
        """

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
        """Method to set the attribute attack_rating of the object.

        Method to set the attribute attack_rating based on a human-readable
        format of the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Pokemon.set_attack_rating( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] defense_rating_to_be_set String that contains the defense rating
                                        to assign to the Pokemon.

        Returns
        -------

        Exceptions
        ----------
          TypeError If the parameter defense_rating_to_be_set is NOT a int.
          ValueError If the parameter defense_rating_to_be_set is NOT > 0 and <= 10.
        """
        if isinstance(attack_rating_to_be_set, int):
            if 11 <= attack_rating_to_be_set <= 20:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")