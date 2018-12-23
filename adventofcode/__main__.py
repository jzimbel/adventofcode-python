import argparse
from datetime import date
from typing import Optional
import os
import re
import importlib
from adventofcode.constants import (
  PROJECT_ROOT,
  SOLUTIONS_DIR_NAME,
  COMMAND_RUN_SOLUTION,
  COMMAND_MAKE_NEW_YEAR,
  YEAR_PREFIX,
  DAY_PREFIX,
  MARK,
  END_MARK
)
from adventofcode.util.get_input import get_input
from adventofcode.util.make_new_year import make_new_year

def run_solution(args) -> None:
  year = args.year
  day = args.day
  if year is None:
    today = date.today()
    year = today.year if today.month == 12 else (today.year - 1)
  solution_module_path = 'adventofcode.solutions.{}{}.{}{}.solution'.format(YEAR_PREFIX, year, DAY_PREFIX, str(day).zfill(2))
  solution_module = importlib.import_module(solution_module_path)
  answer1, answer2 = solution_module.run(get_input(year, day))
  print()
  print('-' * 50)
  print('-' * 50)
  print('Solutions found.')
  print()
  print('Answer to problem 1:', '{}{}{}'.format(MARK, answer1, END_MARK))
  print('Answer to problem 2:', '{}{}{}'.format(MARK, answer2, END_MARK))

def run_make_new_year(args) -> None:
  year = args.year
  if year is None:
    year = get_default_year_for_make()
  make_new_year(year)

def get_default_year_for_make() -> int:
  '''
  Search the solutions directory for the latest year, and return the one after that.
  Returns current year if directory is empty.
  '''
  solutions_dir_path = os.path.join(PROJECT_ROOT, SOLUTIONS_DIR_NAME)
  try:
    return max(
      int(entry[1:])
      for entry in os.listdir(solutions_dir_path)
      if re.fullmatch(r'y\d+', entry)
    ) + 1
  except ValueError:
    return date.today().year

if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='python -m adventofcode', description='Run Advent of Code solutions and related utilities.')
  subparsers = parser.add_subparsers()

  parser_run = subparsers.add_parser(
    COMMAND_RUN_SOLUTION,
    aliases=['run'],
    description='Run a solution.',
    help='Run a solution.'
  )
  parser_run.add_argument('--year', '-y', help='Year of the solution. If not specified, the most recent year will be used.')
  parser_run.add_argument('day', help='Day of the solution.')
  parser_run.set_defaults(func=run_solution)

  parser_init = subparsers.add_parser(
    COMMAND_MAKE_NEW_YEAR,
    aliases=['init'],
    description='Set up a directory (plus accompanying tests directory) for a new year of solutions.',
    help='Set up a directory (plus accompanying tests directory) for a new year of solutions.'
  )
  parser_init.add_argument(
    '--year',
    '-y',
    help='Year to create. If not specified, the {} directory will be inspected and a year after the latest existing year will be created.'.format(SOLUTIONS_DIR_NAME)
  )
  parser_init.set_defaults(func=run_make_new_year)

  args = parser.parse_args()
  args.func(args)