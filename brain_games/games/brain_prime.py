import random
import math

# Сокращённый алгоритм Эратосфена

def get_primes(number):
    is_prime = [True] * (number + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, number + 1):
        if is_prime[i]:
            for j in range(i ** 2, number + 1, i):  #i ** 2
                is_prime[j] = False
    primes = []
    for i in range(2, number + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

def launch_prime():
    rules = "Answer \"Yes\" if given number is prime. Otherwise answer \"No\".\n"
    question = random.randint(1,10000)
    prime_list = get_primes(question)
    if question in prime_list:
        answer = "Yes"
    else:
        answer = "No"
    return (rules,question,answer)