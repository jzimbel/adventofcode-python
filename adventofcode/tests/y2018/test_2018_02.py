'''
Test for year 2018, day 2 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d02 import solution_1, solution_2

puzzle_1_data = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
puzzle_2_data = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

def test_solution_1() -> None:
  assert solution_1(puzzle_1_data) == 12

def test_solution_2() -> None:
  assert solution_2(puzzle_2_data) == 'fgij'
