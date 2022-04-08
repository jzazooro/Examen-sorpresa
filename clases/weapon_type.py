from enum import Enum


class WeaponType(Enum):
    """Python class to implement an enumeration for the attribute Weapon Type.

    This Python class implements an enumeration for the attribute Weapon Type.

    Syntax
    ------
      obj = WeaponType.Enum

    Parameters
    ----------

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class WeaponType.

    Attributes
    ----------

    Example
    -------
      >>> from weapon_type import WeaponType
      >>> obj_WeaponType = WeaponType.Boxer
    """
    PUNCH = 2
    KICK = 4
    ELBOW = 6
    HEADBUTT = 10

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(str_weapon_type):
        """Method to obtain a Enum from a String.

        This method is used to generate a Enum based on a String.

        Syntax
        ------
          [ ] = from_str(str_weapon_type)

        Parameters
        ----------
          str_weapon_type String String that represents a Weapon Type.

        Returns
        -------
          Null .

        Example
        -------
          >>> weapon_type.from_str("punch")
        """
        str_weapon_type = str_weapon_type.lower()
        if str_weapon_type == 'punch':
            return WeaponType.PUNCH
        elif str_weapon_type == 'kick':
            return WeaponType.KICK
        elif str_weapon_type == 'elbow':
            return WeaponType.ELBOW
        elif str_weapon_type == 'headbutt':
            return WeaponType.HEADBUTT
        else:
            raise TypeError("The str " + str_weapon_type + " does not correspond with a warrior Type")