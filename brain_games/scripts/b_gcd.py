from brain_games.game_engine import launch_game
from brain_games.games.brain_gcd import find_gcd
from brain_games.games.brain_gcd import description

def main():
    launch_game(find_gcd,description)

if __name__ == '__main__':
    main()