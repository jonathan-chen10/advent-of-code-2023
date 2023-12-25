import sys

import re

sys.path.append('..')
import logger

def solve_A(input_lines: list) -> int:
  springs, broken_sets = parse_spring_records(input_lines)
  return sum(num_arrangements(spring, broken) 
             for spring, broken in zip(springs, broken_sets))

def parse_spring_records(input_lines: list[str]) -> list[list]:
  springs = []
  broken_sets = []
  for row in input_lines:
    row = row.split()
    springs.append(row[0])
    broken_sets.append([int(n) for n in row[1].split(',')])
  return [springs, broken_sets]

def num_arrangements(springs: str, broken: list[int]) -> int:
  # DP approach: build from LHS, 
  # C[n, broken] = C[n-1, broken] + C[n-#(last), all but last] if possible
  subprobs = [[0 for _ in range(len(springs) + 1)] 
              for _ in range(len(broken) + 1)]
  # base case: if broken = [] and no springs are broken so far, 
  # C[k][(no broken)] = 1
  subprobs[0][0] = 1
  for spring_idx in range(0, len(springs)):
    if springs[spring_idx] == '#':
      break
    else:
      subprobs[0][spring_idx + 1] = 1
  for broken_stop in range(1, len(broken) + 1):
    # looking at only the first (broken_size) of broken
    broken_len = broken[broken_stop - 1]
    for spring_stop in range(1, len(springs) + 1):
      state = springs[spring_stop - 1]
      if state == '.' or state == '?':
        subprobs[broken_stop][spring_stop] += subprobs[broken_stop][spring_stop - 1]
      if state == '#' or state == '?':
        can_place = (broken_len <= spring_stop and 
                     re.match(r'^[#?]+$', 
                              springs[spring_stop - broken_len : spring_stop]))
        if can_place and spring_stop > broken_len:
          can_place = can_place and springs[spring_stop - broken_len - 1] != '#'
        if can_place:
          subprobs[broken_stop][spring_stop] += \
            subprobs[broken_stop - 1][max(spring_stop - broken_len - 1, 0)]
  
  #for row in subprobs:
  #  logger.log(row)

  return subprobs[-1][-1]



def solve_B(input_lines: list[str]) -> int:
  return solve_B_naive(input_lines)

def solve_B_naive(input_lines: list[str]) -> int:
  # Let's see how long this takes...
  # Not so long after all!
  springs, broken_sets = parse_spring_records(input_lines)
  springs = ['?'.join([seq] * 5) for seq in springs]
  broken_sets = [broken * 5 for broken in broken_sets]
  return sum(num_arrangements(spring, broken) 
             for spring, broken in zip(springs, broken_sets))

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