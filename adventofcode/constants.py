import os
import sys

PROJECT_ROOT = sys.path[0]
TESTS_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, '..', 'tests'))

COMMAND_RUN_SOLUTION = 'run_solution'
COMMAND_MAKE_NEW_YEAR = 'make_new_year'

# constants used when initializing a new year directory and loading input/solutions
SOLUTIONS_DIR_NAME = 'solutions'
YEAR_PREFIX = 'y'
DAY_PREFIX = 'd'
SOLUTION_FILE_NAME = 'solution.py'
INPUT_FILE_NAME = 'input.txt'

SOLUTION_FILE_TEMPLATE = \
"""'''
Solution for day {{day}} of the {{year}} Advent of Code calendar.
Run it with the command `python -m adventofcode {} {{year}} {{day}}` from the project root.
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
'''
from context.adventofcode.{}.{}{{year}}.{}{{day}} import solution

def test_run() -> None:
  # not yet implemented!
  pass
""".format(SOLUTIONS_DIR_NAME, YEAR_PREFIX, DAY_PREFIX)
