'''
Solution for day 1 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 1` from the project root.
'''
from functools import reduce
from operator import add
from adventofcode.types import Solution

def solution_1(changes: list) -> int:
  return reduce(add, changes, 0)

def solution_2(changes: list) -> int:
  seen = set([0])
  frequency = 0
  repeated = []

  while len(repeated) == 0:
    for change in changes:
      new_frequency = frequency + change
      frequency += change
      if new_frequency in seen:
        repeated.append(new_frequency)
        break
      seen.add(new_frequency)
  return repeated[0]

def run(data: str) -> Solution:
  changes = [int(change) for change in data.split('\n')]
  return (solution_1(changes), solution_2(changes))
