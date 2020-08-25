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
    i = 3
    description = game[1]
    print(description, end="\n") 
    while i != 0:
        q_a = game[0]()
        question, answer = q_a[0],q_a[1]
        if isinstance(question, int):
            print("Question: ",answer)
        else:
            print ("Question:",*question, sep=" ")

        a = input("Answer: ")

        if str(answer) == a:
            print("Correct!\n")
            i -= 1
        else:
            print(mistakes_that_makes[random.randint(0,5)])
    print("Congrats, %s!"%(name))