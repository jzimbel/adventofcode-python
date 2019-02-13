'''
Test for year 2018, day 9 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d09 import solution

parameters_and_expectations = [
  ((9, 25), 32),
  ((10, 1618), 8317),
  ((13, 7999), 146373),
  ((17, 1104), 2764),
  ((21, 6111), 54718),
  ((30, 5807), 37305)
]

def test_solution_1() -> None:
  for parameters, expectation in parameters_and_expectations:
    assert solution(*parameters) == expectation
