import random
import prompt

def rules():
    print ("Answer \"yes\" if number even otherwise answer \"no\".\n")

def game_launch_brain_even():
    guess_num = random.randint(1,100)
    print("Question: %s\n"%(guess_num))
    user_answ = prompt.string("Answer: ")
    guess_even = guess_num % 2 == 0
    users_yes = user_answ == "Yes"
    guess_not_even = guess_num % 2 == 1
    user_no = user_answ == "No"

    if guess_even  and users_yes:
        return True
    elif guess_not_even and user_no:
        return True
    else:
        return False
