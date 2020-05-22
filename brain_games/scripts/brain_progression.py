import random
import prompt

def launch_progression():
    length = 10
    step = random.randint(1,10)
    start = random.randint(1,10)
    counter = start
    random_index = random.randint(0,length - 1)
    random_value = 0

    print("Question:", end=" ")
    for i in range(length):
        if i == random_index:
            print("..", end=" ")
            random_value = counter
        else:
            print(counter, end=" ")
        counter += step
    print()
    

    user_answer = prompt.integer("Answer: ")
    return user_answer == random_value