'''
Solution for day 2 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 2` from the project root.
'''
from typing import List
from collections import defaultdict
from adventofcode.types import Solution

def solution_1(box_ids: List[str]) -> int:
  twos = 0
  threes = 0
  for box_id in box_ids:
    char_counts = defaultdict(lambda: 0)
    for char in box_id:
      char_counts[char] += 1
    if any(char_count == 2 for char_count in char_counts.values()):
      twos += 1
    if any(char_count == 3 for char_count in char_counts.values()):
      threes += 1
  return twos * threes

def solution_2(box_ids: List[str]) -> int:
  for list_index, id1 in enumerate(box_ids):
    for id2 in box_ids[list_index + 1:]:
      diff = [id2[char_index] != char1 for char_index, char1 in enumerate(id1)]
      if sum(diff) == 1:
        return ''.join(char for char_index, char in enumerate(id1) if not diff[char_index])

def run(data: str) -> Solution:
  box_ids = data.split('\n')
  # not yet implemented!
  return (solution_1(box_ids), solution_2(box_ids))
