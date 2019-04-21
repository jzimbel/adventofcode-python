'''
Solution for day 14 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 14` from the project root.
'''
from adventofcode.types import Solution
from typing import Tuple

def shared_solution(data: str) -> Tuple[str, str]:
  num_recipes = int(data)
  score_pattern = [int(digit) for digit in data]
  scores = [3, 7]
  current_1 = 0
  current_2 = 1

  count_to_match = None
  check_index = 0

  while len(scores) < num_recipes + 10 or count_to_match is None:
    for digit in (int(digit) for digit in str(scores[current_1] + scores[current_2])):
      if len(scores) % 1000000 == 0:
        print(len(scores), 'recipes scored', end='\r', flush=True)
      scores.append(digit)
      if count_to_match is None and digit == score_pattern[check_index]:
        check_index += 1
        if check_index == len(score_pattern):
          count_to_match = len(scores) - len(score_pattern)
      elif digit == score_pattern[0]:
        check_index = 1
      else:
        check_index = 0
    current_1 = (current_1 + scores[current_1] + 1) % len(scores)
    current_2 = (current_2 + scores[current_2] + 1) % len(scores)
  print()
  return (
    ''.join(str(score) for score in scores[num_recipes:num_recipes + 10]),
    count_to_match
  )

def run(data: str) -> Solution:
  print('This one takes about 45 seconds--needs to run over 20 million iterations for my puzzle input.')
  return shared_solution(data)
