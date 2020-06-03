import sys

from brain_games.games.brain_calc import launch_calc
from brain_games.games.brain_even import launch_even
from brain_games.games.brain_gcd import launch_gcd
from brain_games.games.brain_progression import launch_progression
from brain_games.games.brain_prime import launch_prime
from brain_games.game_engine import launch_game
# Список игр, правил к ним и исполняемой функции

game_list = [
    ("brain-games",'', None),
    ("brain-calc", "What is the result of the expression?\n", launch_calc),
    ("brain-even", "Answer \"Yes\" if number even otherwise answer \"No\".\n", launch_even),
    ("brain-gcd","Find the greatest common divisor of given numbers.", launch_gcd),
    ("brain-progression","What number is missing in the progression?", launch_progression),
    ("brain-prime","Answer \"Yes\" if given number is prime. Otherwise answer \"No\".", launch_prime)
]


def get_comand():
    arg = sys.argv[0]
    for a in range(len(arg)-1,0,-1):
        if arg[a] == "/":
            return arg[a+1:]
    return arg

# Запуск игрового процесса

def poetry_run():
    users_comand = get_comand()
    game = game_list[0]
    for g in game_list:
        if users_comand == g[0]:
            print(g[1])
            print()
            game = g
    launch_game(game)
