'''
Test for year 2018, day 6 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d06 import solution_1, solution_2
from adventofcode.types import Point, with_id

IDPoint = with_id(Point)

data = \
'''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''

seeds = [
  IDPoint(
    index,
    *(int(scalar) for scalar in line.split(', '))
  )
  for index, line in enumerate(data.split('\n'))
]

def test_solution_1() -> None:
  assert solution_1(seeds) == 17

def test_solution_2() -> None:
  assert solution_2(seeds, max_distance=32) == 16
