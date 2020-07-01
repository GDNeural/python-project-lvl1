import prompt
import random
import sys
#from brain_games.scripts.launch_script import game_list


mistakes_that_makes = [
    "\nYou are going to pay for that with another round\n",
    "\nKiss my shiny metal right answer\n",
    "\nEnglish, do you speak it?!\n",
    "\nStop right there you criminal scum\n",
    "\nYour right answer is wrong. Try again\n",
    "\nWash your mouse after that\n"
]

def launch_game(game):
    print ("Welcome to the Brain Games!\n")
    name = prompt.string('May I have your name? ')
    print('Hello, %s!\n'%(name))
    rounds = 0
    rules = game()[0]
    print(rules) 
    while rounds !=3:
        q_a = game()
        if isinstance(q_a[1], int):
            print("Question: ",q_a[1])
        else:
            print ("Question:",*q_a[1], sep=" ")

        i = input("Answer: ")

        if str(q_a[2]) == i:
            print("Correct!\n")
            rounds +=1
        else:
            print(mistakes_that_makes[random.randint(0,5)])
    print("Congrats, %s!"%(name))