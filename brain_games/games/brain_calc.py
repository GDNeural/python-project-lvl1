import random
from operator import add, sub, mul

description = "What is the result of the expression?"

def calculate_operation():
    random_number_1 = random.randint(1,10)
    random_number_2 = random.randint(1,10)
    operators = ((add,"+"), (sub,"-"), (mul, "*"))
    # Следующим шагом одновременно присваиваем название элементам подкортежа и выбираем случайный
    func, symbol = random.choice(operators)
    question = [random_number_1, symbol, random_number_2]
    answer = func(random_number_1, random_number_2)
    return (question, answer)