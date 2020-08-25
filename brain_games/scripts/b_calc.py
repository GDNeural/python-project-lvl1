from brain_games.game_engine import launch_game
import brain_games.games.brain_calc as calc

def main():
    launch_game(calc.game)

if __name__ == '__main__':
    main()