import random
import prompt

def launch_progression():
    length = 10
    step = random.randint(1,10)
    start = random.randint(1,10)
    question = [start,]
    random_index = random.randint(0,length - 1)
    
    for i in range(length):
        if i == random_index:
            answer = question[i]+step
            question.append("..")
        elif question[i] == "..":
            question.append(answer+step)
        else:
            next_step = int(question[i]) + step
            question.append(next_step)
    
    return (question, answer)