import random
import prompt
from brain_games.cli import *
from brain_games.scripts.brain_games import greet

__name__ = '__second__'

def rules():
    print ("Answer \"yes\" if number even otherwise answer \"no\".\n")

def wrong_answer_yes():
    print(f"\n\'yes\' is wrong answer ;(. Correct answer was \'no\'.\n Let\'s try again, {get_name.name} !\n")

def wrong_answer_no():
    print(f"\n\'no\' is wrong answer ;(. Correct answer was \'yes\'.\n Let\'s try again, {get_name.name} !\n")

def correct_answer():
    print("Correct!\n")

def random_number():
    number = random.randint(1,100)
    return number

def invalid_input():
    print("\nYou can type only 'yes' or 'no'!\n")    

def game_process():
    greet()
    rules()
    welcome_user()

def even_func():
    counter = 0
    while counter != 3:
        quest_num = random_number()
        print ("Question: " + str(quest_num))
        answer = prompt.string("Answer: ")
        if quest_num % 2 == 0 and answer == "yes":
            correct_answer()
            counter+=1
        elif quest_num % 2 == 1 and answer == "no":
            correct_answer()
            counter+=1
        elif quest_num % 2 == 0 and answer == "no":
            wrong_answer_no()
        elif quest_num % 2 == 1 and answer == "yes":
            wrong_answer_yes()
        else:
            invalid_input()
        if counter == 3:
            print(f"Congratulations, {get_name.name}!")
            break
        
game_process()
even_func()
exit()