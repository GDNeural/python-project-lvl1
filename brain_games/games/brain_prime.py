import random
import prompt
import math
from brain_games.game_engine import go_input_whrum_whrum

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
  number = random.randint(1,10000)
  prime_list = get_primes(number)
  print("Question: ", number)
  user_answer = go_input_whrum_whrum()
  user_yes = user_answer == "Yes"
  user_no = user_answer == "No"
  return ((number in prime_list) and user_yes) or ((number not in prime_list) and user_no)