import sys

sys.path.append('..')
#import day_1.soln as day_1

def solve_A() -> int:
  pass

def solve_B():
  pass

if __name__ == "__main__":
  if len(sys.argv) == 1:
    print('Missing arg[1] (A, B)')
  elif sys.argv[1] == 'A':
    print(solve_A())
  elif sys.argv[1] == 'B':
    print(solve_B())
  else:
    print('Invalid arg[1] (A, B)')