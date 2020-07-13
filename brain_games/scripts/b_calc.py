from brain_games.game_engine import launch_game
from brain_games.games.brain_calc import calculate_operation
from brain_games.games.brain_calc import description

def main():
    launch_game(calculate_operation, description)

if __name__ == '__main__':
    main()