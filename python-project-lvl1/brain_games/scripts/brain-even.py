import random
import prompt
from brain_games.cli import name


def wrong_answer_yes():
    print(f"\'yes\' is wrong answer ;(. Correct answer was \'no\'.\n Let\'s try again, {name} !")

def wrong_answer_no():
    print(f"\'no\' is wrong answer ;(. Correct answer was \'yes\'.\n Let\'s try again, {name} !")

def correct_answer():
    print("Correct!")
   

def random_number():
    number = random.randint(1,100)
    return number

def invalid_input():
    print("You can type only 'yes' or 'no'!")    

def game_process():
    counter = 0
    quest_num = random_number()
    while counter < 3:
        print ("Question: " + str(quest_num))
        answer = prompt.string("Answer: ")
        if quest_num % 2 == 0 and answer == "yes":
            correct_answer()
            counter=+1
        elif quest_num % 2 == 1 and answer == "no":
            correct_answer()
            counter=+1
        elif quest_num % 2 == 0 and answer == "no":
            wrong_answer_no()
        elif quest_num % 2 == 1 and answer == "yes":
            wrong_answer_yes()
        else:
            invalid_input()
        if counter == 3:
            print(f"Congratulations, {name}!")
