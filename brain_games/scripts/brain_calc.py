import random
import prompt
from operator import add, sub, mul

def rules():
    print ("What is the result of the expression?\n")

def game_launch_brain_calc():
    vrbl1 = random.randint(1,10)
    vrbl2 = random.randint(1,10)
    ops = ((add,"+"), (sub,"-"), (mul, "*"))
    # (add,+) (sub, -) (mul, *)
    func, symbol = random.choice(ops)
    answer = func(vrbl1, vrbl2)
    print("Question: ",vrbl1, symbol, vrbl2)
    user_answ = prompt.integer("Answer: ")
    if user_answ == answer:
        return True
    if user_answ != answer:
        return False