import random
import prompt
import math

def launch_gcd():
    random_number_1 = random.randint(1,100)
    random_number_2 = random.randint(1,100)
    right_answer = math.gcd(random_number_1, random_number_2)
    print("Question:{} {}\n".format(random_number_1,random_number_2))
    user_answ = prompt.integer("Answer: ")
    return user_answ == right_answer
