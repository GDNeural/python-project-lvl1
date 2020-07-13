import random
import math

description = "Find the greatest common divisor of given numbers."

def gcd(a,b): #For those who seek an algorythm
    while b > 0:
        a, b = b, a % b
    return a

def find_gcd():
    random_number_1 = random.randint(1,100)
    random_number_2 = random.randint(1,100)
    question = (random_number_1,random_number_2)
    answer = math.gcd(random_number_1, random_number_2)
    return (question, answer)
