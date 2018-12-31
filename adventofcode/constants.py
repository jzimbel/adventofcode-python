from collections import defaultdict
import os

# for downloading puzzle inputs
AOC_URL = 'https://adventofcode.com'
USER_AGENT = 'advent_of_code_input_downloader_jzimbel'

# base directories and other file names
SOLUTIONS_DIR_NAME = 'solutions'
PROJECT_ROOT = os.path.dirname(__file__)
TESTS_ROOT = os.path.join(PROJECT_ROOT, 'tests')
SOLUTIONS_ROOT = os.path.join(PROJECT_ROOT, SOLUTIONS_DIR_NAME)
INPUTS_ROOT = os.path.join(PROJECT_ROOT, 'inputs')
USER_SESSION_ID_FILE_PATH = os.path.join(PROJECT_ROOT, '.USER_SESSION_ID')

# command names
COMMAND_RUN_SOLUTION = 'run_solution'
COMMAND_MAKE_NEW_YEAR = 'make_new_year'

# constants used when initializing a new year directory and loading inputs/solutions
YEAR_PREFIX = 'y'
DAY_PREFIX = 'd'

# starter file templates
SOLUTION_FILE_TEMPLATE = \
"""'''
Solution for day {{day}} of the {{year}} Advent of Code calendar.
Run it with the command `python -m adventofcode {} -y {{year}} {{day}}` from the project root.
'''
from adventofcode.types import Solution

def run(data: str) -> Solution:
  # not yet implemented!
  return (None, None)
""".format(COMMAND_RUN_SOLUTION)

TEST_FILE_TEMPLATE = \
"""'''
Test for year {{year}}, day {{day}} solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.{}.{}{{year}}.{}{{zero_padded_day}} import run

def test_run() -> None:
  # not yet implemented!
  assert run('') == (None, None)
""".format(SOLUTIONS_DIR_NAME, YEAR_PREFIX, DAY_PREFIX)

# for highlighting sections of printed text
MARKS = defaultdict(lambda: '\033[1;34m', {
  'b': '\033[1;34m',
  'g': '\033[1;32m',
  'y': '\033[1;33m',
  'r': '\033[1;31m'
})
END_MARK = '\033[0m'
