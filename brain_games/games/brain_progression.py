import random

description = "What number is missing in the progression?"

def find_missing_number():
    length = 10
    step = random.randint(1,10)
    start = random.randint(1,10)
    random_index = random.randint(0,length - 1)
    question = []
    for i in range(length):
        if i == random_index:
            answer = start + step * i
            question.append("..")
        else:
            next_step = start + step * i
            question.append(next_step)
    
    return (question, answer)