import sys

from brain_games.games.brain_calc import launch_calc
from brain_games.games.brain_even import launch_even
from brain_games.games.brain_gcd import launch_gcd
from brain_games.games.brain_progression import launch_progression
from brain_games.games.brain_prime import launch_prime
# Список игр, правил к ним и исполняемой функции

game_list = [
    ("brain-games",'', None),
    ("brain-calc", "What is the result of the expression?", launch_calc),
    ("brain-even", "Answer \"Yes\" if number even otherwise answer \"No\".", launch_even),
    ("brain-gcd","Find the greatest common divisor of given numbers.", launch_gcd),
    ("brain-progression","What number is missing in the progression?", launch_progression),
    ("brain-prime","Answer \"Yes\" if given number is prime. Otherwise answer \"No\".", launch_prime)
]