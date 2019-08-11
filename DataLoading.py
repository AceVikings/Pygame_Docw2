import pandas as pd
import os
import pygame

def getData(x):
    return pd.read_csv(x)

Pokemons = getData(r'pokemonList.csv')
Attacks = getData(r'moveset.csv')

spritelist = []
def Find_index(char,Pokemons):
    for i in range(len(Pokemons)):
        if Pokemons['name'][i] == char:
            return i

Gym_sprite = []
Trainer_sprite = []
attack_sprite = []
def animLoad(pokemon_name,Trainer,Gym):

    path, dirs, files = next(os.walk(pokemon_name+"\\"))
    file_count = len(files)
    print(file_count)
    for i in range(file_count):
        if Trainer:

            if i < 10:
                Trainer_sprite.append(0)
                Trainer_sprite[i] = pygame.image.load(pokemon_name + '\\frame_0' + str(i) + '_delay-0.03s.gif')
                Trainer_sprite[i] = pygame.transform.scale2x(Trainer_sprite[i])

            if i >= 10:
                Trainer_sprite.append(0)
                Trainer_sprite[i] = pygame.image.load(pokemon_name + '\\frame_' + str(i) + '_delay-0.03s.gif')
                Trainer_sprite[i] = pygame.transform.scale2x(Trainer_sprite[i])
        if Gym:

            if i < 10:
                Gym_sprite.append(0)
                Gym_sprite[i] = pygame.image.load(pokemon_name + '\\frame_0' + str(i) + '_delay-0.03s.gif')

            if i >= 10:
                Gym_sprite.append(0)
                Gym_sprite[i] = pygame.image.load(pokemon_name + '\\frame_' + str(i) + '_delay-0.03s.gif')

def attack_load(attack_type):

    path, dirs, files = next(os.walk(attack_type + "\\"))
    file_count = len(files)
    print(file_count)
    for i in range(file_count):
        attack_sprite.append(0)
        attack_sprite[i] = pygame.image.load(attack_type + "\\"+str(i)+".png")

def move_stats(move_name):
    move_index = Find_index(move_name,Attacks)
    power = int(Attacks.loc[move_index, 'Power'])
    move_type = Attacks.loc[move_index, 'Type']
    PP = int(Attacks.loc[move_index, 'PP'])
    return power,move_type,PP

def give_stats(pokemon_name):
    pokemon_index = Find_index(pokemon_name,Pokemons)
    attack = int(Pokemons.loc[pokemon_index, 'attack'])
    defense = int(Pokemons.loc[pokemon_index, 'defense'])
    speed = int(Pokemons.loc[pokemon_index, 'speed'])
    sp_attack = int(Pokemons.loc[pokemon_index, 'specialAttack'])
    sp_defense = int(Pokemons.loc[pokemon_index, 'specialDefence'])
    move1 = Pokemons.loc[pokemon_index, 'move1']
    move2 = Pokemons.loc[pokemon_index, 'move2']
    return attack,defense,speed,sp_attack,sp_defense,move1,move2

