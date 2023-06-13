#Ejercicio 2
from collections import deque
avengers = [
    {'nombre_superheroe': 'Star Lord', 'nombre_personaje': 'Peter Quill', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1976},
    {'nombre_superheroe': 'Capitana Marvel', 'nombre_personaje': 'Carol Danvers', 'grupo': '', 'anio_aparicion': 2012},
    {'nombre_superheroe': 'Iron Man', 'nombre_personaje': 'Tony Stark', 'grupo': '', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Vlanck Widow', 'nombre_personaje': 'Natasha Romanoff', 'grupo': '', 'anio_aparicion': 1964},
    {'nombre_superheroe': 'Captain America', 'nombre_personaje': 'Steve Rogers', 'grupo': '', 'anio_aparicion': 1941},
    {'nombre_superheroe': 'Thor', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Hulk', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Invisible Woman', 'nombre_personaje': 'Susan Storm', 'grupo': 'Los cuatro fantásticos', 'anio_aparicion': 1961},
    {'nombre_superheroe': 'Hawkeye', 'nombre_personaje': 'Clint Barton', 'grupo': '', 'anio_aparicion': 1964},
    {'nombre_superheroe': 'Black Panther', 'nombre_personaje': 'T\'Challa', 'grupo': '', 'anio_aparicion': 1966},
    {'nombre_superheroe': 'Scarlet Witch', 'nombre_personaje': 'Wanda Maximoff', 'grupo': '', 'anio_aparicion': 1964}
]
#a)
capitana_marvel = next((hero['nombre_personaje'] for hero in avengers if hero['nombre_superheroe'] == 'Capitana Marvel'), None)
if capitana_marvel:
    print(f"El personaje de Capitana Marvel esta en la lista y su nombre es: {capitana_marvel}")
else:
    print("Capitana Marvel no está en la lista.")

#b)
guardians_queue = deque()
guardians_count = sum(1 for hero in avengers if hero['grupo'] == 'Guardianes de la galaxia')
print(f"La cantidad de superhéroes que pertenecen al grupo 'Guardianes de la galaxia' es: {guardians_count}")

#c)
fantastic_four_and_guardians = sorted([hero['nombre_superheroe'] for hero in avengers if hero['grupo'] in ['Los cuatro fantásticos', 'Guardianes de la galaxia']], reverse=True)
print("Superhéroes de 'Los cuatro fantásticos' y 'Guardianes de la galaxia' en orden descendente:")
for hero in fantastic_four_and_guardians:
    print(hero)

#d)
heroes_after_1960 = [hero['nombre_superheroe'] for hero in avengers if hero['nombre_personaje'] != '' and hero['anio_aparicion'] > 1960]
print("Lista de superhéroes con nombre de personaje cuyo año de aparición es posterior a 1960:")
for hero in heroes_after_1960:
    print(hero)

#e)
for hero in avengers:
    if hero['nombre_superheroe'] == 'Vlanck Widow':
        hero['nombre_superheroe'] = 'Black Widow'
print("Lista de superhéroes actualizada:")
for hero in avengers:
    print(hero)
    
#f)
aux_characters = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki']

for character in aux_characters:
    if not any(hero['nombre_superheroe'].lower() == character.lower() for hero in avengers):
        avengers.append({'nombre_superheroe': character, 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': ''})

#g)
characters_cps = [hero['nombre_superheroe'] for hero in avengers if hero['nombre_superheroe'][0] in ['C', 'P', 'S']]
print("Personajes que comienzan con C, P o S:")
for character in characters_cps:
    print(character)

#h)
additional_heroes = [
    {'nombre_superheroe': 'Spider-Man', 'nombre_personaje': 'Peter Parker', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Doctor Strange', 'nombre_personaje': 'Stephen Strange', 'grupo': '', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Wolverine', 'nombre_personaje': 'Logan', 'grupo': '', 'anio_aparicion': 1974},
    {'nombre_superheroe': 'Vision', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1968},
    {'nombre_superheroe': 'Falcon', 'nombre_personaje': 'Sam Wilson', 'grupo': '', 'anio_aparicion': 1969},
    {'nombre_superheroe': 'Ant-Man', 'nombre_personaje': 'Scott Lang', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Winter Soldier', 'nombre_personaje': 'Bucky Barnes', 'grupo': '', 'anio_aparicion': 2005},
    {'nombre_superheroe': 'Gamora', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1975},
    {'nombre_superheroe': 'Groot', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1960},
    {'nombre_superheroe': 'Rocket Raccoon', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1976},
    {'nombre_superheroe': 'Mantis', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1973},
    {'nombre_superheroe': 'Silver Surfer', 'nombre_personaje': '', 'grupo': 'Los cuatro fantásticos', 'anio_aparicion': 1966},
    {'nombre_superheroe': 'Crystal', 'nombre_personaje': 'Crystalia Amaquelin', 'grupo': 'Los cuatro fantásticos', 'anio_aparicion': 1961},
    {'nombre_superheroe': 'Mr. Fantastic', 'nombre_personaje': 'Reed Richards', 'grupo': 'Los cuatro fantásticos', 'anio_aparicion': 1961},
    {'nombre_superheroe': 'Thing', 'nombre_personaje': 'Ben Grimm', 'grupo': 'Los Inhumanos', 'anio_aparicion': 1965},
    {'nombre_superheroe': 'Deadpool', 'nombre_personaje': 'Wade Wilson', 'grupo': '', 'anio_aparicion': 1991},
    {'nombre_superheroe': 'Cyclops', 'nombre_personaje': 'Scott Summers', 'grupo': 'X-Men', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Jean Grey', 'nombre_personaje': '', 'grupo': 'X-Men', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Storm', 'nombre_personaje': 'Ororo Munroe', 'grupo': 'X-Men', 'anio_aparicion': 1975},
    {'nombre_superheroe': 'Beast', 'nombre_personaje': 'Hank McCoy', 'grupo': 'X-Men', 'anio_aparicion': 1963}
]
avengers.extend(additional_heroes)
print("Lista completa de superhéroes:")
for hero in avengers:
    print(hero)
