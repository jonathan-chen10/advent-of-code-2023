import sys
import time
import functools

sys.path.append('..')
import logger

def solve_A(input_lines: list[str]) -> int:
  init_seeds, *maps = parse_input(input_lines)
  map_all = lambda input : functools.reduce(
    lambda x, y : y(x), [map_to_func(m) for m in maps], input)
  init_locs = [map_all(seed) for seed in init_seeds]
  return min(init_locs)

def parse_input(lines: list[str]) -> list:
  # output: output seed #'s, then map arrays
  seeds = [int(n) for n in lines[0][7:].split()]
  r = [seeds]
  cur_map = []
  for l in lines:
    if len(l) > 0 and l[0].isnumeric():
      cur_map.append([int(n) for n in l.split()])
    elif len(cur_map) > 0:
      r.append(cur_map)
      cur_map = []
  r.append(cur_map) # add final map
  return r

def map_to_func(map: list[list[int]]):
  def ret(input: int) -> int:
    for possibility in map:
      dst_start, src_start, ran = possibility
      if src_start <= input < src_start + ran:
        offset = input - src_start
        return dst_start + offset 
    return input
  #return lambda input : logger.log_func(ret, input, 'map_to_func', str(map[0]))
  return ret

# brute force was too slow, let's try reverse brute force (not guaranteed - not surjective)
def solve_B(input_lines: list[str]) -> int:
  init_seed_ranges, *maps = parse_input(input_lines)
  reverse_map_all = lambda input : functools.reduce(
    lambda x, y : y(x), reversed([reverse_map_to_func(m) for m in maps]), input)
  
  init_seed_specs = [
    (init_seed_ranges[i], init_seed_ranges[i] + init_seed_ranges[i + 1]) 
    for i in range(0, len(init_seed_ranges), 2)]

  for i in range(0, 860904829): 
    origin = reverse_map_all(i)
    if i % 1e7 == 0:
      print(i, 'yae')
    if any(lower <= origin <= upper for (lower, upper) in init_seed_specs):
      return i
  
def reverse_map_to_func(map: list[list[int]]):
  def ret(input: int) -> int:
    for possibility in map:
      dst_start, src_start, ran = possibility
      if dst_start <= input < dst_start + ran:
        offset = input - dst_start
        return src_start + offset 
    return input
  return ret

if __name__ == "__main__":
  input_lines = [line.rstrip() for line in sys.stdin]
  if len(sys.argv) == 1:
    print('Missing arg[1] (A, B)')
  elif sys.argv[1] == 'A':
    print(solve_A(input_lines))
  elif sys.argv[1] == 'B':
    start = time.process_time()
    ans = solve_B(input_lines)  
    print(time.process_time() - start, " seconds")
    print(ans)
    # Takes a minute and a half
  else:
    print('Invalid arg[1] (A, B)')