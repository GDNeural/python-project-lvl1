import random

description = """Answer "Yes" if number even otherwise answer "No"."""

def guess_even_number():
    question = random.randint(1,100)
    if question % 2 == 0:
        answer = "Yes"
    else:
        answer = "No"
    return (description, question, answer)