from brain_games.game_engine import launch_game
from brain_games.games.brain_prime import launch_prime

def main():
    launch_game(launch_prime)

if __name__ == '__main__':
    main()