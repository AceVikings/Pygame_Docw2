import pygame
import pandas as pd
from Texts import *
from DataLoading import *
from images import *


pygame.init()



clock = pygame.time.Clock()
timer1 = 0
timer2 = 0
attack_timer_trainer = 0
attack_timer_gym = 0

move_counter = 3
gym_special = False
hurt_gym = [False,0]
hurt_trainer = [False,0]

gym_turn = False
global i,j
i,j = 0,0
win = pygame.display.set_mode((350,600))
pygame.display.set_caption("DOCW GAME")
G_attack_cordinate = [220,80]
T_attack_cordinate = [150, 140]

#GAME VARIABLES

x = 220
y = 80

Gym_pokemons = ['Charmander','Squirtle','Pikachu','Mew','Venusaur','Snorlax']  #Enter Gym's Pokemon
Trainer_pokemons = ['Charmander','Charmander',0,0,0,0]
Trainer_goes_first = False
T_Level = [0, 0, 0, 0, 0, 0]
G_Level = [20,25,28,27,23,24]

special_attack = False


class Pokemon(object): #POKEMON CLASS
    def __init__(self,pokemon_name,level,trainer_bool,gym_bool):
        stats = give_stats(pokemon_name)
        self.name = pokemon_name
        self.pokemon_name = pokemon_name
        self.hp = 100
        self.level = level
        self.attack = stats[0]
        self.defense = stats[1]
        self.speed = stats[2]
        self.sp_attack = stats[3]
        self.sp_defense = stats[4]
        #self.pokemon_index = pokemon_index
        self.move1 = stats[5]
        self.move2 = stats[6]
        self.x = 240
        self.x1 = 60
        self.y1 = 130
        self.y = 80
        animLoad(self.pokemon_name,trainer_bool,gym_bool)



class attack():
    def __init__(self,move_name):
        stats = move_stats(move_name)
        self.power = stats[0]
        self.type = stats[1]
        self.PP = stats[2]
        self.name = move_name

def redrawWindow():

    global timer1,timer2,Fire,attack_timer_trainer,special_attack,is_hurt, hurt_gym,hurt_trainer,gym_turn,gym_special\
        ,move_counter,attack_timer_gym
    global T_pokemon,G_pokemon

    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    win.blit(text_bar, (0, 265))


    if hurt_gym[0]:

        if hurt_gym[1] < 15:
            if hurt_gym[1] % 2 == 0:
                win.blit(Gym_sprite[timer1], (G_pokemon.x + 2, G_pokemon.y))
            if hurt_gym[1] % 2 != 0:
                win.blit(Gym_sprite[timer1], (G_pokemon.x - 2, G_pokemon.y))
            hurt_gym[1] += 1
        else:
            is_hurt = False
            hurt_gym[0] = False
            hurt_gym[1] = 0
    else:
        win.blit(Gym_sprite[timer1], (G_pokemon.x, G_pokemon.y))
        is_hurt = False

    if gym_turn:
        if gym_special and attack_timer_gym <15:
            if move_counter%3 == 0:
                attack_load(current_attack.type)

                win.blit(attack_sprite[attack_timer_gym // 5], (G_attack_cordinate[0], G_attack_cordinate[1]))

                attack_timer_gym += 1
                G_attack_cordinate[0] -= 4
                G_attack_cordinate[1] += 3
                text = text_bar_font.render(G_pokemon.name + ' used ' + current_attack.name, True, (0, 0, 0))
                win.blit(text, (15, 280))
        elif attack_timer_gym > 14:

            hurt_trainer[0] = True
            gym_special = False
            attack_timer_gym = 0
            G_attack_cordinate[0] = 220
            G_attack_cordinate[1] = 80
            gym_turn = False





    if special_attack and attack_timer_trainer < 15:

        attack_load(current_attack.type)

        win.blit(attack_sprite[attack_timer_trainer // 5], (T_attack_cordinate[0], T_attack_cordinate[1]))
        text = text_bar_font.render(T_pokemon.name+' used '+current_attack.name,True,(0,0,0))
        win.blit(text,(15,280))
        attack_timer_trainer += 1
        T_attack_cordinate[0] += 4
        T_attack_cordinate[1] -= 3

    elif attack_timer_trainer > 14:
        is_hurt = True
        hurt_gym[0] = True
        special_attack = False
        T_attack_cordinate[0] = 150
        T_attack_cordinate[1] = 140

        attack_timer_trainer = 0

    if hurt_trainer[0]:

        if hurt_trainer[1] < 15:
            if hurt_trainer[1] % 2 == 0:
                win.blit(Trainer_sprite[timer2], (T_pokemon.x1 + 2, T_pokemon.y1))
            if hurt_trainer[1] % 2 != 0:
                win.blit(Trainer_sprite[timer2], (T_pokemon.x1 - 2, T_pokemon.y1))
            hurt_trainer[1] += 1
        else:
            is_hurt = False
            hurt_trainer[0] = False
            hurt_trainer[1] = 0
    else:
        win.blit(Trainer_sprite[timer2], (T_pokemon.x1, T_pokemon.y1))
        is_hurt = False

    timer1 += 1
    timer2 += 1

    if timer1 >= len(Gym_sprite):
        timer1 = 0
    if timer2 >= len(Trainer_sprite):
        timer2 = 0


    pygame.display.update()

#PLAYER ENTERS HIS POKEMONS

# for i in range(2):
#     Trainer_pokemons[i], T_Level[i] =input('Enter ' + str(i + 1) + ' Pokemon and level').split(' ')

T_pokemon = Pokemon('Charmander', 20, True, False)
G_pokemon = Pokemon('Bulbasaur', 20, False, True)

run = True
while run:
    clock.tick(15)


    if T_pokemon.speed > G_pokemon.speed:
        Trainer_goes_first = True
    else:
        Trainer_goes_first = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                special_attack = True
                current_attack = attack(T_pokemon.move2)
            if event.key == pygame.K_LEFT:
                normal_attack = True
                current_attack = attack(T_pokemon.move1)
            if event.key == pygame.K_UP:
                gym_turn = True
                gym_special = True
                current_attack = attack(G_pokemon.move2)


    if T_pokemon.hp == 0:

        pass
    else:
        T_pokemon.hp -= 50
        print(T_pokemon.hp)
    redrawWindow()
pygame.quit()