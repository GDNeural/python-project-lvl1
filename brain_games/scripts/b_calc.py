from brain_games.game_engine import launch_game
from brain_games.games.brain_calc import launch_calc

def main():
    launch_game(launch_calc)

if __name__ == '__main__':
    main()