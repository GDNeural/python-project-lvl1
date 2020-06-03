import random
import prompt
from brain_games.game_engine import go_input_whrum_whrum

def rules():
    print ("Answer \"yes\" if number even otherwise answer \"no\".\n")

def launch_even():
    guess_num = random.randint(1,100)
    print("Question: %s\n"%(guess_num))
    user_answ = go_input_whrum_whrum()
    guess_even = guess_num % 2 == 0
    users_yes = user_answ == "Yes"
    guess_not_even = guess_num % 2 == 1
    user_no = user_answ == "No"

    return (guess_even and users_yes) or (guess_not_even and user_no)