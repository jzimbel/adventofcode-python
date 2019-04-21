'''
Test for year 2018, day 14 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d14 import shared_solution

def test_shared_solution() -> None:
  assert shared_solution('9')[0] == '5158916779'
  assert shared_solution('5')[0] == '0124515891'
  assert shared_solution('18')[0] == '9251071085'
  assert shared_solution('2018')[0] == '5941429882'

  assert shared_solution('51589')[1] == 9
  assert shared_solution('01245')[1] == 5
  assert shared_solution('92510')[1] == 18
  assert shared_solution('59414')[1] == 2018
