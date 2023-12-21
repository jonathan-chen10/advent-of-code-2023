import sys

import math
import re

sys.path.append('..')
import logger

class LabelledGraph:
  def __init__(self):
    self.nodes = {}

  def add(self, label: str, next: list[str]):
    self.nodes[label] = next 

  def next_node(self, cur_node: str, idx: int = 0) -> str:
    return self.nodes[cur_node][idx]
  
  def all_labels(self) -> list[str]:
    return list(self.nodes.keys())


def solve_A(input_lines: list[str]):
  graph = LabelledGraph()
  instructions = input_lines[0]
  for node_line in input_lines[2:]:
    cleaned_line = re.sub(r'[=\(\),]', '', node_line)
    label, left, right = cleaned_line.split()
    graph.add(label, [left, right])
  
  return path_length(graph, instructions, 'AAA', lambda n : n == 'ZZZ') 

def solve_B_naive(input_lines: list[str]):
  graph = LabelledGraph()
  instructions = input_lines[0]
  for node_line in input_lines[2:]:
    cleaned_line = re.sub(r'[=\(\),]', '', node_line)
    label, left, right = cleaned_line.split()
    graph.add(label, [left, right])
  
  cur_nodes = [label for label in graph.all_labels() if label[-1] == 'A']
  step_no = 0
  while True:
    if all(label[-1] == 'Z' for label in cur_nodes):
      return step_no
    else:
      for i, node in enumerate(cur_nodes):
        which_way = 1 if instructions[step_no % len(instructions)] == 'R' else 0
        cur_nodes[i] = graph.next_node(node, which_way)
      step_no += 1

# let's try doing it individually and getting the LCM
def solve_B(input_lines: list[str]):
  graph = LabelledGraph()
  instructions = input_lines[0]
  for node_line in input_lines[2:]:
    cleaned_line = re.sub(r'[=\(\),]', '', node_line)
    label, left, right = cleaned_line.split()
    graph.add(label, [left, right])
  
  start_nodes = [label for label in graph.all_labels() if label[-1] == 'A']
  path_lengths = [path_length(graph, instructions, node, lambda n : n[-1] == 'Z') 
                  for node in start_nodes]
  
  return math.lcm(*path_lengths)
  
def path_length(graph: LabelledGraph, instructions: str, start_node: str, stop_cond) -> int:
  cur_node = start_node
  step_no = 0
  while True:
    if stop_cond(cur_node):
      #logger.log('COMPLETED', step_no)
      return step_no
    else:
      which_way = 1 if instructions[step_no % len(instructions)] == 'R' else 0
      cur_node = graph.next_node(cur_node, which_way)
      step_no += 1
  

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