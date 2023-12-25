import sys
import itertools

sys.path.append('..')
from utils import manhattan_distance
import logger

def solve_A(input_lines: list) -> int:
  return solve_general(input_lines, 2)

def solve_general(input_lines: list, space_between: int) -> int:
  stars = locate_stars(input_lines)
  star_cols, star_rows = [set(locs) for locs in zip(*stars)]

  # prefix maps
  col_map = star_coords(star_cols, len(input_lines), space_between)
  row_map = star_coords(star_rows, len(input_lines[0]), space_between)

  stars = [(col_map[star[0]], row_map[star[1]]) for star in stars]

  return sum(manhattan_distance(star1, star2) \
             for star1, star2 in itertools.product(stars, stars)) / 2
  
def locate_stars(input_lines: list[str]) -> list[tuple[int]]:
  stars = []
  for i, row in enumerate(input_lines):
    for j, item in enumerate(row):
      if item == '#':
        stars.append((i, j))
  return stars
    
def star_coords(star_locs: list[tuple[int]], size: int, space_between: int):
  pos_real = [0]
  for i in range(1, size):
    if i - 1 in star_locs:
      pos_real.append(pos_real[-1] + 1)
    else:
      pos_real.append(pos_real[-1] + space_between)
  return pos_real

def solve_B(input_lines: list):
  return solve_general(input_lines, 1e6)

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