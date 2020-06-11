import random
import math

def launch_gcd():
    random_number_1 = random.randint(1,100)
    random_number_2 = random.randint(1,100)
    question = (random_number_1,random_number_2)
    answer = math.gcd(random_number_1, random_number_2)
    return (question, answer)
