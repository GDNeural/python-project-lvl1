import prompt
import random
import sys
from brain_games.scripts.brain_calc import game_launch_brain_calc
from brain_games.scripts.brain_even import game_launch_brain_even
from brain_games.scripts.brain_gcd import game_launch_brain_gcd

# Список игр, правил к ним и исполняемой функции

game_list = [
    ("brain-games",'', None),
    ("brain-calc", "What is the result of the expression?\n", game_launch_brain_calc),
    ("brain-even", "Answer \"yes\" if number even otherwise answer \"no\".\n", game_launch_brain_even),
    ("brain-gcd","Find the greatest common divisor of given numbers.",game_launch_brain_gcd)
]


# 2 Способа запуска пакета


# №1 Как исполняемый скрипт

def module_run():
    
    # 1. Вывести список игр
    print("Game list:")
    for i in range(len(game_list)):
        print(i+1,game_list[i][0], "\n")
    
    # 2. Узнать у пользователя какая игра ему нужна
    users_input = prompt.integer("What do you want to play: ")
    game = game_list[users_input-1]
    
    # 3. Напечатать правила
    print(game[1])

    #4. Запуск основной игры
    launch_game(game)


# №2 Через poetry

def poetry_run():
    users_comand = sys.argv[0]
    game = 0
    for g in game_list:
        if users_comand == g[0]:
            print(g[1])
            game = g
    
    launch_game(game)

# Общая логика для запуска всех игр
    
def launch_game(game):
    print ("Welcome to the Brain Games!\n")

    name = prompt.string('May I have your name? ')
    
    print('\nHello, %s!\n'%(name))

    # 4. Запустить нужную игру
    counter = 0
    while counter !=3:
        if game[2] == None:
            break
        condition = game[2]()
        if condition:
            print("Correct!\n")
            counter +=1
        else:
            print("\nStop right there you criminal scum\n")

    print("Congrats, %s!\n"%(name)) 