from brain_games.game_engine import launch_game
from brain_games.games.brain_prime import guess_prime_number
from brain_games.games.brain_prime import description

def main():
    launch_game(guess_prime_number, description)

if __name__ == '__main__':
    main()