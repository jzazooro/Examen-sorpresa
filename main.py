from clases.weapon_type import *
from clases.pokemon import *
from clases.agua import *
from clases.tierra import *
from clases.electricidad import *
from clases.aire import *
from csv import *

def entrenadoruno(entrenador):
    try:
        with open('coach_1_pokemons.csv' , newline='') as csv_file:
            leer= csv.reader('coach_1_pokemons.csv')
            info=list(leer)
            for temp_pokemon_csv in info:
                pokemon_csv_a_la_lista = Pokemon(int(temp_pokemon_csv[0]) , temp_pokemon_csv[1]) , WeaponType(temp_pokemon_csv [2]) , int(temp_pokemon_csv[3]) , int(temp_pokemon_csv[4]) , int(temp_pokemon_csv[5]))
                entrenador.append(pokemon_csv_a_la_lista)
    except:
        print("ha habido un error")
    return entrenador

def entrenadordos(entrenador):
    try:
        with open('coach_2_pokemons.csv' , newline='') as csv_file:
            leer= csv.reader('coach_2_pokemons.csv')
            infodos=list(leer)
            for temp_pokemon_csv in infodos:
                pokemon_csv_a_la_lista = Pokemon(int(temp_pokemon_csv[0]) , temp_pokemon_csv[1]) , WeaponType(temp_pokemon_csv [2]) , int(temp_pokemon_csv[3]) , int(temp_pokemon_csv[4]) , int(temp_pokemon_csv[5]))
                entrenador.append(pokemon_csv_a_la_lista)
    except:
        print("ha habido un error")
    return entrenador

def main():
    coach1=[]
    coach2=[]
    entrenadoruno(coach1)
    entrenadordos(coach2)
    print (coach1)
    print(coach2)
if __name__=="__main__":
    main()

