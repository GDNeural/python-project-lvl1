import random
import prompt
from brain_games.cli import name


def wrong_answer_yes():
    print(f"\n\'yes\' is wrong answer ;(. Correct answer was \'no\'.\n Let\'s try again, {name} !\n")

def wrong_answer_no():
    print(f"\n\'no\' is wrong answer ;(. Correct answer was \'yes\'.\n Let\'s try again, {name} !\n")

def correct_answer():
    print("Correct!\n")
   

def random_number():
    number = random.randint(1,100)
    return number

def invalid_input():
    print("\nYou can type only 'yes' or 'no'!\n")    

def game_process():
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
            print(f"Congratulations, {name}!")
            break