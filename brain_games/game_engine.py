import prompt
import random
import sys

# Ввод пользователя

def go_input_whrum_whrum():
    i = input("Answer: ")
    return i

def launch_game(game):
    print ("Welcome to the Brain Games!\n")
    name = prompt.string('May I have your name? ')
    print('\nHello, %s!\n'%(name))
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