import sys
import math

sys.path.append('..')
#import day_1.soln as day_1

def game_idx(game: str) -> int:
  return int(game[5:game.find(':')])

def game_possible(game: str, 
                  red_threshold: str, 
                  green_threshold: str, 
                  blue_threshold: str) -> bool:
  max_red, max_green, max_blue = max_marbles(game)
  fail = (max_red > red_threshold 
          or max_green > green_threshold 
          or max_blue > blue_threshold)
  return not fail

def max_marbles(game: str) -> list:
  # returns [max_red, max_green, max_blue]
  moves = game[game.find(':') + 1 :].split(';')
  r = [0, 0, 0]
  for move in moves:
    red, green, blue = marbles_in_move(move)
    r[0] = max(red, r[0])
    r[1] = max(green, r[1])
    r[2] = max(blue, r[2])
  return r

def marbles_in_move(move: str) -> list:
  # returns [red, green, blue]
  # input of the form " 3 blue, 4 red"
  counts = move.split(',')
  r = [0, 0, 0]
  for c in counts:
    n = int(c.split(' ')[1])
    color = c.split(' ')[2]
    if color == 'red':
      r[0] = n
    elif color == 'green':
      r[1] = n
    elif color == 'blue':
      r[2] = n
  return r

def set_power(game: str) -> int:
  return math.prod(max_marbles(game))

def solve_A() -> int:
  return sum([game_idx(game.rstrip()) for game in sys.stdin if game_possible(game.rstrip(), 12, 13, 14)])

def solve_B():
  return sum([set_power(game.rstrip()) for game in sys.stdin])

if __name__ == "__main__":
  if len(sys.argv) == 1:
    print('Missing arg[1] (A, B)')
  elif sys.argv[1] == 'A':
    print(solve_A())
  elif sys.argv[1] == 'B':
    print(solve_B())
  else:
    print('Invalid arg[1] (A, B)')