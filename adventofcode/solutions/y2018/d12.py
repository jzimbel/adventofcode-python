'''
Solution for day 12 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 12` from the project root.
'''
from adventofcode.types import Solution
from typing import Set
import re

plant_descriptor_pattern = re.compile(r'[#.]+')

class PotLine:
  def __init__(self, state: Set[int], rules: Set[str]) -> None:
    self.state = state
    self.rules = rules

  @classmethod
  def from_initial_state(cls, initial_state: str, rules: Set[str]) -> 'PotLine':
    state = {
      n
      for n, pot in enumerate(initial_state)
      if pot == '#'
    }
    return cls(state, rules)

  def nearby_pots(self, index: int) -> str:
    return ''.join('#' if n in self.state else '.' for n in range(index - 2, index + 3))

  def advance(self) -> 'PotLine':
    new_state = {
      candidate
      for candidate in range(min(self.state) - 2, max(self.state) + 3)
      if self.nearby_pots(candidate) in self.rules
    }
    return PotLine(new_state, set(self.rules))

def solution_1(pot_line: PotLine):
  for _ in range(20):
    pot_line = pot_line.advance()
  return sum(pot_line.state)

def solution_2(pot_line: PotLine):
  previous_sum = 0
  current_sum = 0
  for i in range(1000):
    previous_sum = current_sum
    pot_line = pot_line.advance()
    current_sum = sum(pot_line.state)
  return previous_sum + (current_sum - previous_sum) * (50000000000 - i)

def run(data: str) -> Solution:
  lines = data.split('\n')
  initial_state = plant_descriptor_pattern.findall(lines[0])[0]
  rules = {
    plant_descriptor_pattern.findall(line)[0]
    for line in lines[2:]
    if line.endswith('#')
  }
  pot_line = PotLine.from_initial_state(initial_state, rules)
  return (solution_1(pot_line), solution_2(pot_line))
