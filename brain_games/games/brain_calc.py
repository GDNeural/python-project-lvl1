import random
from operator import add, sub, mul

def launch_calc():
    vrbl1 = random.randint(1,10)
    vrbl2 = random.randint(1,10)
    ops = ((add,"+"), (sub,"-"), (mul, "*"))
    # Следующим шагом одновременно присваиваем название элементам подкортежа и выбираем случайный
    func, symbol = random.choice(ops)
    question = [vrbl1, symbol, vrbl2]
    answer = func(vrbl1, vrbl2)
    return (question, answer)