import sys

from collections import Counter

sys.path.append('..')
import logger

def solve_A(input_lines: list) -> int:
  hands = [parse_hand(line) for line in input_lines]
  #logger.log(hands)
  hands.sort(key = lambda hand : pair_strength(hand[0]))
  hands.sort(key = lambda hand : type_strength(hand[0]))
  winnings = [hand[1] * rank for rank, hand in enumerate(hands, start=1)]
  return sum(winnings)

def parse_hand(line: str) -> list:
  # ret[0] is the 5-character string containing the cards
  # ret[1] is the bid of the hand
  r = line.split()
  r[1] = int(r[1])
  return r

def pair_strength(hand: str, cards_order: list=['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']) -> int:
  values = {label : i for i, label in enumerate(cards_order)}
  #logger.log(values)

  last_digit_value = values[hand[-1]]

  if len(hand) == 1:
    return last_digit_value
  else:
    # sneaky bug: forgot to add cards_order to recursion
    return pair_strength(hand[:-1], cards_order) * 13 + last_digit_value

def hand_type(hand: str) -> str:
  repeats = tuple(sorted(Counter(hand).values(), reverse=True))
  types = {
    (1, 1, 1, 1, 1) : 'High card',
    (2, 1, 1, 1) : 'One pair',
    (2, 2, 1) : 'Two pair',
    (3, 1, 1) : 'Three of a kind',
    (3, 2) : 'Full house',
    (4, 1) : 'Four of a kind',
    (5,) : 'Five of a kind'
  }

  return types[repeats]

def type_strength(hand: str, hand_type_calculation=hand_type) -> int:
  type_values = {
    'High card' : 0,
    'One pair' : 1,
    'Two pair' : 2,
    'Three of a kind' : 3,
    'Full house' : 4,
    'Four of a kind' : 5,
    'Five of a kind' : 6
  }

  return type_values[hand_type_calculation(hand)]

def solve_B(input_lines: list):
  hands = [parse_hand(line) for line in input_lines]
  #logger.log(hands)
  hands.sort(key = lambda hand : pair_strength(hand[0], cards_order=['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']))
  hands.sort(key = lambda hand : type_strength(hand[0], hand_type_calculation=hand_type_joker))
  winnings = [hand[1] * rank for rank, hand in enumerate(hands, start=1)]
  return sum(winnings)

def hand_type_joker(hand: str) -> str:
  # FIXED: JJJJX will not produce XXXXX
  if hand == 'JJJJJ':
    return hand_type(hand)
  
  most_common_label = Counter(hand.replace('J', '')).most_common(1)[0][0]
  #logger.log(hand, hand.replace('J', most_common_label))
  return hand_type(hand.replace('J', most_common_label))

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