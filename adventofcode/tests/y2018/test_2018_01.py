'''
Test for year 2018, day 1 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d01 import solution_1, solution_2

def test_solution_1() -> None:
  assert solution_1([]) == 0
  assert solution_1([1, -2, 3, -4, 5]) == 3

def test_solution_2() -> None:
  assert solution_2([1, -1]) == 0
  assert solution_2([5, 6, -7, 2, -1]) == 5
