from brain_games.game_engine import launch_game
from brain_games.games.brain_even import guess_even_number
from brain_games.games.brain_even import description

def main():
    launch_game(guess_even_number, description)

if __name__ == '__main__':
    main()