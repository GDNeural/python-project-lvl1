import prompt
import random
import sys
from brain_games.scripts.games.brain_calc import launch_calc
from brain_games.scripts.games.brain_even import launch_even
from brain_games.scripts.games.brain_gcd import launch_gcd
from brain_games.scripts.games.brain_progression import launch_progression
from brain_games.scripts.games.brain_prime import launch_prime

# Список игр, правил к ним и исполняемой функции

game_list = [
    ("brain-games",'', None),
    ("brain-calc", "What is the result of the expression?\n", launch_calc),
    ("brain-even", "Answer \"yes\" if number even otherwise answer \"no\".\n", launch_even),
    ("brain-gcd","Find the greatest common divisor of given numbers.", launch_gcd),
    ("brain-progression","What number is missing in the progression?", launch_progression),
    ("brain-prime","Answer \"yes\" if given number is prime. Otherwise answer \"no\".", launch_prime)
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

# Получение команды пользователя при установке пакета

def get_comand():
    arg = sys.argv[0]
    for a in range(len(arg)-1,0,-1):
        if arg[a] == "/":
            return arg[a+1:]
    return arg

# Запуск игрового процесса

def poetry_run():
    users_comand = get_comand()
    print(users_comand)
    game = game_list[0]
    for g in game_list:
        if users_comand == g[0]:
            print(g[1])
            print()
            game = g
    launch_game(game)

# Взять ввод пользователя
# Найти первый слеш с конца:
# Просмотерть элементы с конца до первого слеша
# Взять срез до этого элемента



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