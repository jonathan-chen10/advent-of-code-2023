import sys

sys.path.append('..')
import logger

def solve_A(input_lines: list):
  start_pos = find_start(input_lines)
  # loop must have even length - checkerboard argument
  # so there is a single farthest point
  llen = traversal_len(input_lines, start_pos)
  return llen / 2

def find_start(grid: list[str]) -> tuple[int]:
  for i, row in enumerate(grid):
    loc = row.find('S')
    if loc != -1:
      return (i, loc)
  return (-1, -1)

def traversal_len(grid: list[str], start: tuple[int])-> int:
  # we can assume there are only 2 pipes away from S
  first_pipe = find_pipe_from_unknown(grid, start)
  cur = start
  next = first_pipe
  cur_len = 0
  while next != start:
    options = connected_pipes(grid, next)
    two_ahead = options[0] if options[0] != cur else options[1]

    cur = next
    next = two_ahead 
    cur_len += 1
  return cur_len + 1

def find_pipe_from_unknown(grid: list[str], coords: tuple[int]) -> tuple[int]:
  # search the 4 adjacent pipes
  row, col = coords
  if row > 0 and coords in connected_pipes(grid, (row-1, col)):
    return (row-1, col)
  elif col > 0 and coords in connected_pipes(grid, (row, col - 1)):
    return (row, col-1)
  else:
    return (row+1, col)
  
def connected_pipes(grid: list[str], coords: tuple[int]) -> list[tuple[int]]:
  row, col = coords
  shape = grid[row][col]
  if shape == '|':
    return [(row-1, col), (row+1, col)]
  elif shape == '-':
    return [(row, col-1), (row, col+1)]
  elif shape == 'L':
    return [(row-1, col), (row, col+1)]
  elif shape == 'J':
    return [(row-1, col), (row, col-1)]
  elif shape == '7':
    return [(row, col-1), (row+1, col)]
  elif shape == 'F':
    return [(row, col+1), (row+1, col)]
  elif shape == 'S':
    return [(row, col+1), (row+1, col), (row-1, col), (row, col-1)]
  else:
    # will run into this for initial search in find_pipe_from_unknown
    logger.log('illegal state:', coords, shape)
    return[row, col]

def solve_B(input_lines: list) -> int:
  grid = purge_extra_cells(input_lines)
  # logger.log_grid(grid)
  # Jordan curve theorem
  return sum(count_interior(line) for line in grid)

def purge_extra_cells(input_lines: list) -> list[str]:
  start_pos = find_start(input_lines)
  loop = loop_coords(input_lines, start_pos)
  #logger.log(loop)
  ret = []
  for i, line in enumerate(input_lines):
    cur_line = ''
    for j, spot in enumerate(line):
      if (i, j) not in loop:
        #logger.log(i, spot, loop)
        cur_line += '.'
      else:
        cur_line += spot
    #logger.log(line, cur_line, i, loop)
    ret.append(cur_line)
  return replace_start(ret, start_pos)

def replace_start(grid: list[str], start: tuple[int]) -> list[str]:
  row, col = start
  grid = [list(s) for s in grid]
  #logger.log(grid)
  if start == (0, 0) or (start in connected_pipes(grid, (row, col+1)) 
                         and start in connected_pipes(grid, (row+1, col))):
    grid[row][col] = 'F'
  elif start == (0, len(grid[0]) - 1) or (
    start in connected_pipes(grid, (row, col-1)) and 
    start in connected_pipes(grid, (row+1, col))):
    grid[row][col] = '7'
  elif start == (len(grid) - 1, 0) or (
    start in connected_pipes(grid, (row, col+1)) and 
    start in connected_pipes(grid, (row-1, col))):
    grid[row][col] = 'L'
  elif start == (len(grid) - 1, len(grid[0]) - 1) or (
    start in connected_pipes(grid, (row, col-1)) and 
    start in connected_pipes(grid, (row-1, col))):
    grid[row][col] = 'J'
  elif col == 0 or col == len(grid[0]) - 1 or (
    start in connected_pipes(grid, (row+1, col)) and 
    start in connected_pipes(grid, (row-1, col))):
    grid[row][col] = '|'
  elif row == 0 or row == len(grid) - 1 or (
    start in connected_pipes(grid, (row, col-1)) and 
    start in connected_pipes(grid, (row, col+1))):
    grid[row][col] = '-'
  else:
    logger.log('Unsure what to do with this start position')
  
  return [''.join(row) for row in grid]
  
def loop_coords(grid: list[str], start: tuple[int])-> int:
  # we can assume there are only 2 pipes away from S
  first_pipe = find_pipe_from_unknown(grid, start)
  cur = start
  next = first_pipe
  loop = [start]
  while next != start:
    options = connected_pipes(grid, next)
    two_ahead = options[0] if options[0] != cur else options[1]

    cur = next
    next = two_ahead 
    loop.append(cur)
  return loop

def count_interior(line: str) -> int:
  # states: (for the border between this cell and the next)
  # 0 if outside
  # 1 if top half inside
  # 2 if botton half inside
  # 3 if inside
  state = 0
  count = 0
  for cell in line:
    if cell == '.':
      if state == 3:
        count += 1
    elif cell == '|':
      state = 3 - state
    elif cell == '-':
      pass
    elif cell == 'L':
      if state == 3:
        state = 2
      else:
        state = 1
    elif cell == 'J':
      if state == 2:
        state = 3
      else:
        state = 0
    elif cell == '7':
      if state == 1:
        state = 3
      else:
        state = 0
    elif cell == 'F':
      if state == 3:
        state = 1
      else:
        state = 2
    else:
      # will run into this for initial search in find_pipe_from_unknown
      logger.log('illegal state:', cell)
  
  return count

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