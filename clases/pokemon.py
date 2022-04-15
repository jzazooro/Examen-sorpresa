from weapon_type import WeaponType


class Pokemon():
    __list_ids = []


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        if (isinstance(pokemon_id, int)==True):
            if pokemon_id not in Pokemon.__list_ids:
                self._pokemon_id = pokemon_id
                Pokemon.__list_ids.append(self._pokemon_id)
            else:
                raise ValueError("The parameter pokemon_id should be a new id not taken by other Pokemon.")
        else:
            raise TypeError("The parameter id should be a int.")

        if isinstance(pokemon_name, str):
            self._pokemon_name = pokemon_name
        else:
            raise TypeError("The parameter pokemon_name should be a String.")

        if isinstance(weapon_type, WeaponType):
            self._weapon_type = weapon_type
        else:
            raise TypeError("The parameter weapon_type should be a WeaponType.")

        if isinstance(health_points, int):
            if 1 <= health_points <= 100:
                self._health_points = health_points
            else:
                raise ValueError("The parameter health_points should be > 0 and <= 100.")
        else:
            raise TypeError("The parameter health_points should be a int.")

        if isinstance(attack_rating, int):
            if 1 <= attack_rating <= 10:
                self._attack_rating = attack_rating
            else:
                raise ValueError("The parameter attack_rating should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating should be a int.")

        if isinstance(defense_rating, int):
            if 1 <= defense_rating <= 10:
                self._defense_rating = defense_rating
            else:
                raise ValueError("The parameter defense_rating should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating should be a int.")

    def get_id(self):
        return self._pokemon_id


    def get_pokemon_name(self):
        return self._pokemon_name


    def get_weapon_type(self):
        return self._weapon_type


    def get_health_points(self):
        return self._health_points


    def get_attack_rating(self):
        return self._attack_rating


    def get_defense_rating(self):
        return self._defense_rating


    def set_pokemon_name(self, pokemon_name_to_be_set):
        if isinstance(pokemon_name_to_be_set, str):
            self._pokemon_name = pokemon_name_to_be_set
        else:
            raise TypeError("The parameter pokemon_name_to_be_set should be a String.")


    def set_weapon_type(self, weapon_type_to_be_set):
        if isinstance(weapon_type_to_be_set, WeaponType):
            self._weapon_type = weapon_type_to_be_set
        else:
            raise TypeError("The parameter weapon_type should be a WeaponType.")


    def set_attack_rating(self, attack_rating_to_be_set):
        if isinstance(attack_rating_to_be_set, int):
            if 1 <= attack_rating_to_be_set <= 10:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")


    def set_defense_rating(self, defense_rating_to_be_set):
        if isinstance(defense_rating_to_be_set, int):
            if 1 <= defense_rating_to_be_set <= 10:
                self._defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("The parameter defense_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a int.")


    def is_alive(self):
        return not bool(self._health_points == 0)



    def fight_attack(self, pokemon_to_attack):
        points_of_damage = self._attack_rating

        print("The Pokemon " + self._pokemon_name +" hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +" with " + str(points_of_damage) + " points of damage!")

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit


    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("The parameter points_of_damage should be an int.")

        print("The Pokemon " + self._pokemon_name +
              " has received an attack of " +
              str(points_of_damage) + " points of damage.")

        if points_of_damage > self._defense_rating:
            self._health_points = (self._health_points -
                                   (points_of_damage - self._defense_rating))
            pokemon_was_hit = True
        else:
            print("No damage received.")
            pokemon_was_hit = False
        if self._health_points < 1:
            self._health_points = 0

        return pokemon_was_hit
    def fight_attack(self, pokemon_to_attack):
        points_of_damage = self._attack_rating

        print("The Pokemon " + self._pokemon_name +" hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +" with " + str(points_of_damage) + " points of damage!")

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit
        
    def elegiratque(self, movimiento):
      movimiento=input("que movimiento quieres realizar?")
      if(isinstance(movimiento,str)==True):
        self.movimiento=movimiento
        WeaponType.tipoataque(movimiento)