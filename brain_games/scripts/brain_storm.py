import prompt
import random
from brain_games.scripts.brain_calc import game_launch_brain_calc
from brain_games.scripts.brain_even import game_launch_brain_even

# Список игр, правил к ним и исполняемой функции

game_list = [
    ("Brain_games",'',),
    ("Brain_calc", "What is the result of the expression?", game_launch_brain_calc),
    ("Brain_even", "Answer \"yes\" if number even otherwise answer \"no\".", game_launch_brain_even)
]

def mass_do():

    print ("Welcome to the Brain Games!\n")

    name = prompt.string('May I have your name? ')
    
    print('\nHello, %s!\n'%(name))

    # 1. Вывести список игр
    print("Game list:")
    for i in range(len(game_list)):
        print(i+1,game_list[i][0], "\n")
    # 2. Узнать у пользователя какая игра ему нужна
    users_input = prompt.integer("What do you want to play: ")
    right_index = users_input - 1
    # 3. Напечатать правила
    print(game_list[right_index][1])
    # 4. Запустить нужную игру
    counter = 0
    while counter !=3:
        condition = game_list[right_index][2]()
        if condition:
            print("Correct!\n")
            counter +=1
        else:
            print("\nStop right there you criminal scum")

    print("Congrats, %s!\n"%(name))     
