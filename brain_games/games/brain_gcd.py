import random
import prompt
import math
from brain_games.game_engine import go_input_whrum_whrum

def launch_gcd():
    random_number_1 = random.randint(1,100)
    random_number_2 = random.randint(1,100)
    right_answer = math.gcd(random_number_1, random_number_2)
    print("Question:{} {}\n".format(random_number_1,random_number_2))
    user_answ = int(go_input_whrum_whrum())
    return user_answ == right_answer
