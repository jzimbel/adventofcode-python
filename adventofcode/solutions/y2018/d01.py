'''
Solution for day 1 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 1` from the project root.
'''
from functools import reduce
from operator import add
from typing import List
from adventofcode.types import Solution

def solution_1(changes: List[int]) -> int:
  return reduce(add, changes, 0)

def solution_2(changes: List[int]) -> int:
  seen = {0}
  frequency = 0
  done = False

  while not done:
    for change in changes:
      frequency += change
      if frequency in seen:
        done = True
        break
      seen.add(frequency)
  return frequency

def run(data: str) -> Solution:
  changes = [int(change) for change in data.split('\n')]
  return (solution_1(changes), solution_2(changes))
