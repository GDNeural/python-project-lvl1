import random

def launch_even():
    rules = "Answer \"Yes\" if number even otherwise answer \"No\".\n"
    question = random.randint(1,100)
    if question % 2 == 0:
        answer = "Yes"
    else:
        answer = "No"
    return (rules, question, answer)