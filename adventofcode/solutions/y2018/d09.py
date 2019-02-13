'''
Solution for day 9 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 9` from the project root.
'''
from adventofcode.types import Solution
from collections import deque
import re

game_scenario_pattern = re.compile(r'(\d+) players; last marble is worth (\d+)')

def solution(num_players: int, max_marble_value: int) -> int:
  scores = [0] * num_players
  circle = deque([0])
  for marble in range(1, max_marble_value + 1):
    if marble % 23 == 0:
      circle.rotate(7)
      scores[(marble - 1) % num_players] += marble + circle.pop()
      circle.rotate(-1)
    else:
      circle.rotate(-1)
      circle.append(marble)
  return max(scores)

def run(data: str) -> Solution:
  parameters = [int(parameter) for parameter in game_scenario_pattern.match(data).groups()]
  return (solution(*parameters), solution(parameters[0], parameters[1] * 100))
