import random
import math

DESCRIPTION = """Answer "yes" if given number is prime. Otherwise answer "no"."""

# Сокращённый алгоритм Эратосфена

def get_list_of_primes(number):
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

def provide_data():
    question = random.randint(1,10000)
    prime_list = get_list_of_primes(question)
    if question in prime_list:
        answer = "yes"
    else:
        answer = "no"
    return (question,answer)

game = (provide_data,DESCRIPTION)