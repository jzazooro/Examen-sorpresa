from enum import Enum


class WeaponType(Enum):
    PUNCH = 2
    KICK = 4
    ELBOW = 6
    HEADBUTT = 10

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(str_weapon_type):
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