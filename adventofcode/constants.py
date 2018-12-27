import os

PROJECT_ROOT = os.path.dirname(__file__)
TESTS_ROOT = os.path.join(PROJECT_ROOT, 'tests')

COMMAND_RUN_SOLUTION = 'run_solution'
COMMAND_MAKE_NEW_YEAR = 'make_new_year'

# constants used when initializing a new year directory and loading input/solutions
SOLUTIONS_DIR_NAME = 'solutions'
YEAR_PREFIX = 'y'
DAY_PREFIX = 'd'
SOLUTION_FILE_NAME = 'solution.py'
INPUT_FILE_NAME = 'input'

SOLUTION_FILE_TEMPLATE = \
"""'''
Solution for day {{day}} of the {{year}} Advent of Code calendar.
Run it with the command `python -m adventofcode {} -y {{year}} {{day}}` from the project root.
'''
from typing import Any, Tuple
Solution = Tuple[Any, Any]

def run(input: str) -> Solution:
  # not yet implemented!
  return (None, None)
""".format(COMMAND_RUN_SOLUTION)

TEST_FILE_TEMPLATE = \
"""'''
Test for year {{year}}, day {{day}} solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
Run this particular test from project root with `PYTHONPATH=$(pwd) py.test {{test_file_path}}`.
'''
from adventofcode.{}.{}{{year}}.{}{{zero_padded_day}}.solution import run

def test_run() -> None:
  # not yet implemented!
  assert run('') == (None, None)
""".format(SOLUTIONS_DIR_NAME, YEAR_PREFIX, DAY_PREFIX)

# for highlighting answers
MARK = '\033[1;32m'
END_MARK = '\033[0m'
