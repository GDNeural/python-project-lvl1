import random

def launch_even():
    guess_num = random.randint(1,100)
    question = guess_num
    if guess_num % 2 == 0:
        answer = "Yes"
    else:
        answer = "No"
    return (question, answer)