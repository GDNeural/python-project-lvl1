import prompt
import random
import sys
from brain_games.scripts.launch_script import game_list


mistakes_that_makes = [
    "\nYou are going to pay for that with another round\n",
    "\nKiss my shiny metal right answer\n",
    "\nEnglish, do you speak it?!\n",
    "\nStop right there you criminal scum\n",
    "\nYour right answer is wrong. Try again\n",
    "\nWash your mouse after that\n"
]

def get_comand():
    arg = sys.argv[0]
    for a in range(len(arg)-1,0,-1):
        if arg[a] == "/":
            return arg[a+1:]
    return arg

# Запуск игрового процесса

def poetry_run():
    users_comand = get_comand()
    game = game_list[0]
    for g in game_list:
        if users_comand == g[0]:
            print(g[1])
            print()
            game = g
    launch_game(game)

def launch_game(game):
    print ("Welcome to the Brain Games!\n")
    name = prompt.string('May I have your name? ')
    print('\nHello, %s!\n'%(name))
    counter = 0
    while counter !=3:

        if game[2] == None:
            break
        q_a = game[2]()

        if isinstance(q_a[0], int):
            print("Question: ",q_a[0])
        else:
            print ("Question:",*q_a[0], sep=" ")

        i = input("Answer: ")

        if str(q_a[1]) == i:
            print("Correct!\n")
            counter +=1
        else:
            print(mistakes_that_makes[random.randint(0,5)])
    print("Congrats, %s!"%(name))