'''
Solution for day 5 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 5` from the project root.
'''
import re
from string import ascii_lowercase
from adventofcode.types import Solution

def toggle_case(char: str) -> str:
  return char.lower() if char.isupper() else char.upper()

def react(polymer: str) -> str:
  reduced = []
  for char in polymer:
    if len(reduced) == 0 or toggle_case(char) != reduced[-1]:
      reduced.append(char)
    else:
      reduced.pop()
  return ''.join(reduced)

def solution_1(polymer: str) -> int:
  return len(react(polymer))

def solution_2(polymer: str) -> int:
  return min(
    len(react(re.sub(char, '', polymer, flags=re.IGNORECASE)))
    for char in ascii_lowercase
  )

def run(data: str) -> Solution:
  return (solution_1(data), solution_2(data))
