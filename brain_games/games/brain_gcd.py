import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."

def get_gcd(a,b): #For those who seek an algorythm
    while b > 0:
        a, b = b, a % b
    return a

def provide_data():
    random_number_1 = random.randint(1,100)
    random_number_2 = random.randint(1,100)
    question = (random_number_1,random_number_2)
    answer = math.gcd(random_number_1, random_number_2)
    return (question, answer)

game = (provide_data,DESCRIPTION)
