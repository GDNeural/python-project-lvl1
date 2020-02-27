import random
import prompt
from brain_games.cli import get_name
from brain_games.scripts.brain_games import greet
from brain_games.scripts.brain_even import game_process

__name__ = "__third__"

def rules():
    print ("What is the result of the expression?\n")

def correct_answer():
    print("Correct!\n")

def calculating_game():
    counter = 0
    ops = ['+', '-', '*']
    while counter != 3:
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        operation = random.choice(ops)
        ops_ans = eval(str(num1) + operation + str(num2))
        print ('Question: {} {} {}\n'.format(num1, operation, num2))
        user_answer = prompt.integer("Answer: ")
        if user_answer == ops_ans:
            correct_answer()
            counter+=1
        elif user_answer != ops_ans:
            print ("\n\'{}\' is wrong answer ;(. Correct answer was \'{}\'.\nLet's try again, {}!\n".format(user_answer, ops_ans, get_name.name))
        if counter == 3:
            print(f"Congratulations, {get_name.name}!")
            break
        
calculating_game()
exit()