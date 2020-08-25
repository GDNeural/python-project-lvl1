from brain_games.game_engine import launch_game
import brain_games.games.brain_gcd as gcd

def main():
    launch_game(gcd.game)

if __name__ == '__main__':
    main()