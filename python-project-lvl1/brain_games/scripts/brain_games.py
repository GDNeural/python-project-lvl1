
from brain_games.cli import welcome_user
from brain_games.scripts.brain-even import game_process

def greet():
    print ("Welcome to the Brain Games!")
    print ("Answer \"yes\" if number even otherwise answer \"no\".")

def main():
    greet()
    welcome_user()
    game_process()

if __name__ == '__main__':
    main()
