import re
import sys

def calibration_value(line: str) -> int:
  # concat first and last digit
  # assumes there is at least one digit
  nums_only = re.sub('\D', '', line)
  return int(str(nums_only[0]) + str(nums_only[-1]))

def calibration_value_v2(line: str) -> int:
  # also looks at whether strings representing numbers
  english_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

  first = ''
  last = ''

  for i, c in enumerate(line):
    brk = False
    if c.isdigit():
      first = c
      break
    slc = line[i:]
    for eng_i, word in enumerate(english_numbers, 1):
      if slc.startswith(word):
        first = eng_i
        brk = True 
    if brk:
      break

  for i, c in reversed(list(enumerate(line))):
    brk = False
    if c.isdigit():
      last = c
      break
    slc = line[i:]
    for eng_i, word in enumerate(english_numbers, 1):
      if slc.startswith(word):
        last = eng_i
        brk = True 
    if brk:
      break

  return int(str(first)+str(last))


def solve_A() -> int:
  return sum(calibration_value(line) for line in sys.stdin)

def solve_B():
  return sum(calibration_value_v2(line) for line in sys.stdin)

if __name__ == "__main__":
  if len(sys.argv) == 1:
    print('Missing arg[1] (A, B)')
  elif sys.argv[1] == 'A':
    print(solve_A())
  elif sys.argv[1] == 'B':
    print(solve_B())
  else:
    print('Invalid arg[1] (A, B)')