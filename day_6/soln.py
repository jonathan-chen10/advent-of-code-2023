import sys
import math
import re

sys.path.append('..')
import logger

def solve_A(input_lines: list) -> int:
  times = [int(n) for n in input_lines[0][5:].split()]
  goals = [int(n) for n in input_lines[1][9:].split()]
  #print([logger.log_func(possible_wins, *pair) for pair in zip(times, goals)])
  return math.prod([possible_wins(*pair) for pair in zip(times, goals)])

def possible_wins(race_time: int, target: int) -> int:
  # quick quadratic formula solve
  algebraic_soln = 2 * math.sqrt(race_time * race_time / 4 - target)
  #logger.log(algebraic_soln)
  if race_time % 2 == 0:
    return round_down_to_next_odd(algebraic_soln + 0.999)
  else:
    return round_down_to_next_even(algebraic_soln + 0.999)
  
def round_down_to_next_even(n: float) -> int:
  # assuming n is positive
  n = int(n) # round down
  return n if n % 2 == 0 else n - 1

def round_down_to_next_odd(n: float) -> int:
  # assuming n is positive
  n = int(n) # round down
  return n if n % 2 != 0 else n - 1

def solve_B(input_lines: list):
  time = int(re.sub('[^0-9]', '', input_lines[0])) # remove all non-numbers
  goal = int(re.sub('[^0-9]', '', input_lines[1]))
  return possible_wins(time, goal)

if __name__ == "__main__":
  input_lines = [line.rstrip() for line in sys.stdin]
  if len(sys.argv) == 1:
    print('Missing arg[1] (A, B)')
  elif sys.argv[1] == 'A':
    print(solve_A(input_lines))
  elif sys.argv[1] == 'B':
    print(solve_B(input_lines))
  else:
    print('Invalid arg[1] (A, B)')