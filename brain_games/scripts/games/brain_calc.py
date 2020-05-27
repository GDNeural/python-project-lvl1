import random
import prompt
from operator import add, sub, mul

def rules():
    print ("What is the result of the expression?\n")

def launch_calc():
    vrbl1 = random.randint(1,10)
    vrbl2 = random.randint(1,10)
    ops = ((add,"+"), (sub,"-"), (mul, "*"))
    # Следующим шагом одновременно присваиваем название элементам подкортежа и выбираем случайный
    func, symbol = random.choice(ops)
    answer = func(vrbl1, vrbl2)
    print("Question: ",vrbl1, symbol, vrbl2)
    user_answ = prompt.integer("Answer: ")
    return user_answ == answer