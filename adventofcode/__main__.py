import argparse
from datetime import date
import os
import re
import importlib
from adventofcode.constants import (
  PROJECT_ROOT,
  SOLUTIONS_DIR_NAME,
  COMMAND_RUN_SOLUTION,
  COMMAND_MAKE_NEW_YEAR,
  YEAR_PREFIX,
  DAY_PREFIX
)
from adventofcode.util import (
  get_day_dir,
  get_input,
  get_latest_year,
  get_year_dir,
  highlight,
  make_new_year,
  pad_day
)

def run_solution(args) -> None:
  year = args.year
  day = args.day
  if year is None:
    year = get_latest_year()
  solution_module_path = 'adventofcode.solutions.{}.{}.solution'.format(get_year_dir(year), get_day_dir(day))
  solution_module = importlib.import_module(solution_module_path)
  answer1, answer2 = solution_module.run(get_input(year, day))
  print()
  print('-' * 50)
  print('-' * 50)
  print(highlight('Solutions found.'))
  print()
  print('Answer to problem 1:', highlight(answer1))
  print('Answer to problem 2:', highlight(answer2))

def run_make_new_year(args) -> None:
  year = args.year
  if year is None:
    latest_year = get_latest_year()
    year = date.today().year if latest_year is None else (latest_year + 1)
  make_new_year(year)

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
