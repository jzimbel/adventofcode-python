'''
Test for year 2018, day 8 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d08 import Tree, solution_1, solution_2

#       C M C M m  m  m  C M C M m  m m m m
data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
#       A----------------------------------
#       C M                           m m m
#           B----------- C-----------
#           C M m  m  m  C M        m
#                            D-----
#                            C M m

tree = Tree.from_list([int(n) for n in data.split()])

def test_solution_1() -> None:
  assert solution_1(tree) == 138

def test_solution_2() -> None:
  assert solution_2(tree) == 66
