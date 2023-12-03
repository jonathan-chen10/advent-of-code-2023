from __future__ import annotations
import sys
import re
from itertools import chain

sys.path.append('..')

class EngineNumber:
  # row major order
  def __init__(self, value: int, row: int, col: int):
    self.value = value
    self.loc = (row, col)

  def is_part(self, engine: list) -> bool:
    return len(self.adjacent_symbols(engine)) > 0
  
  def adjacent_symbols(self, engine: list) -> set:
    # https://stackoverflow.com/a/6053606
    symbol_regex = '[^a-zA-Z\d\s.]'

    found_symbols = set()

    row_start = max(self.loc[0] - 1, 0)
    row_end = min(self.loc[0] + 1, len(engine) - 1) # inclusive
    col_start = max(self.loc[1] - 1, 0)
    col_end = min(self.loc[1] + len(str(self.value)), len(engine[0]) - 1) # inclusive

    for row in range(row_start, row_end + 1):
      for col in range(col_start, col_end + 1):
        if bool(re.search(symbol_regex, engine[row][col])):
          found_symbols.add(EngineSymbol(engine[row][col], row, col))
    
    return found_symbols
  
class EngineSymbol:
  # row major order
  def __init__(self, symb: str, row: int, col: int):
    self.symb = symb  
    self.loc = (row, col)

  def __eq__(self, other: EngineSymbol) -> bool:
    return self.loc == other.loc and self.symb == other.symb
  
  def __hash__(self):
    return hash(self.symb) + 2 * hash(self.loc)

def solve_A(input_lines: list) -> int:
  # load engine numbers
  engine_numbers = []
  for line_no, line in enumerate(input_lines):
    col = 0
    numbers = re.findall(r'\d+', line)
    for n in numbers:
      col = line.find(n, col)
      engine_numbers.append(EngineNumber(int(n), line_no, col)) 
      col += len(n)
  
  return sum([en.value for en in engine_numbers if en.is_part(input_lines)])

def solve_B(input_lines: list):
  engine_numbers = []
  for line_no, line in enumerate(input_lines):
    col = 0
    numbers = re.findall(r'\d+', line)
    for n in numbers:
      # NOTE THE BUG HERE: Should start looking after the current number ends, not just the first digit
      # See input-b-test3.txt provided graciously by https://www.reddit.com/r/adventofcode/comments/189qaez/comment/kbsrfw5/
      col = line.find(n, col)
      engine_numbers.append(EngineNumber(int(n), line_no, col)) 
      col += len(n)
  
  gear_numbers = {}
  for en in engine_numbers:
    adjacent_gears = [g for g in en.adjacent_symbols(input_lines) if g.symb == '*']
    for gear in adjacent_gears:
      if gear in gear_numbers:
        gear_numbers[gear].append(en.value)
      else:
        gear_numbers[gear] = [en.value]

  ########## DEBUGGING ##########
  # for v in gear_numbers.values():
  #   print(v)

  # Test that size of dict == # of keys
  # print(len(gear_numbers), sum([s.count('*') for s in input_lines]))

  return sum([nums[0]*nums[1] if len(nums) == 2 else 0 for nums in gear_numbers.values()])

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