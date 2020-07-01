from brain_games.game_engine import launch_game
from brain_games.games.brain_even import launch_even

def main():
    launch_game(launch_even)

if __name__ == '__main__':
    main()