from brain_games.game_engine import launch_game
from brain_games.games.brain_progression import launch_progression

def main():
    launch_game(launch_progression)

if __name__ == '__main__':
    main()