'''
Test for year 2018, day 5 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d05 import react, run, toggle_case

data = 'dabAcCaCBAcCcaDA'

def test_react() -> None:
  assert react(data) == 'dabCBAcaDA'

def test_toggle_case() -> None:
  assert toggle_case('x') == 'X'
  assert toggle_case('X') == 'x'

def test_run() -> None:
  # not yet implemented!
  assert run(data) == (10, 4)
