import sys

sys.path.append('..')

def solve_A(input_lines: list[str]) -> int:
  return sum([lotto_points(line) for line in input_lines])

def lotto_points(lotto_line: str) -> int:
  num_matches = lotto_match_count(lotto_line)
  return 1 << (num_matches - 1) if num_matches > 0 else 0

def lotto_match_count(lotto_line: str) -> int:
  winning_nums, my_nums = parse_lotto(lotto_line)
  return len(set(winning_nums).intersection(set(my_nums)))

def parse_lotto(lotto_line: str) -> list[list[int]]:
  # Input of the form '''Card N: N ... | N ...'''
  lotto_line = lotto_line.split(':')[1]
  return [[int(n) for n in part.split()] for part in lotto_line.split('|')]

def solve_B(input_lines: list[str]) -> int:
  num_lotto_cards = [1 for _ in range(len(input_lines))]
  for line_num, lotto_line in enumerate(input_lines):
    num_matches = lotto_match_count(lotto_line)
    for offset in range(1, num_matches + 1):
      num_lotto_cards[line_num + offset] += num_lotto_cards[line_num]
  
  return sum(num_lotto_cards)


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