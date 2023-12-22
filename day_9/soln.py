import sys

import numpy as np

sys.path.append('..')
import logger

def solve_A(input_lines: list[str]) -> int:
  running_sum = 0
  for line in input_lines:
    seq = [int(n) for n in line.split()]
    xs = [i for i in range(len(seq))]
    ys = seq
    #logger.log(xs, ys)
    fit = np.polynomial.Polynomial.fit(xs, ys, len(seq) - 1)
    #logger.log(xs, ys)
    #logger.log([fit(x) for x in xs])
    running_sum += round(fit(len(seq)))
  return running_sum

def solve_B(input_lines: list):
  running_sum = 0
  for line in input_lines:
    seq = [int(n) for n in line.split()]
    xs = [i for i in range(len(seq))]
    ys = seq
    #logger.log(xs, ys)
    fit = np.polynomial.Polynomial.fit(xs, ys, len(seq) - 1)
    #logger.log(xs, ys)
    #logger.log([fit(x) for x in xs])
    running_sum += round(fit(-1))
  return running_sum

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