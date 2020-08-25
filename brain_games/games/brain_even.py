import random

DESCRIPTION = """Answer "yes" if number even otherwise answer "no"."""

def provide_data():
    question = random.randint(1,100)
    if question % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return (question, answer)

game = (provide_data,DESCRIPTION)