from brain_games.game_engine import launch_game
from brain_games.games.brain_progression import find_missing_number
from brain_games.games.brain_progression import description

def main():
    launch_game(find_missing_number,description)

if __name__ == '__main__':
    main()