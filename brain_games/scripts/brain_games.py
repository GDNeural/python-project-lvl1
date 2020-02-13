
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import game_process

__name__ = '__main__'

def greet():
    welcome_user()
    print ("Welcome to the Brain Games!")
    print ("Answer \"yes\" if number even otherwise answer \"no\".\n")

def main():
    greet()
    game_process()
    exit()

main()
