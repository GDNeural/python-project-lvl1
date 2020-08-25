import random
from operator import add, sub, mul

DESCRIPTION = "What is the result of the expression?"


def get_operation_sign(op):
    mapping = {add:"+", sub:"-", mul:"*"}
    return mapping[op]


def provide_data():
    random_number_1 = random.randint(1,10)
    random_number_2 = random.randint(1,10)
    operation = random.choice([add, sub, mul])
    sign = get_operation_sign(operation)
    
    question = [random_number_1, sign, random_number_2]
    answer = operation(random_number_1, random_number_2)
    return (question, answer)

game = (provide_data,DESCRIPTION)