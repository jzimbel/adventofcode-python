import argparse
from adventofcode.constants import (
  SOLUTIONS_DIR_NAME,
  COMMAND_RUN_SOLUTION,
  COMMAND_MAKE_NEW_YEAR
)
from adventofcode.run_solution import run_solution
from adventofcode.run_make_new_year import run_make_new_year

parser = argparse.ArgumentParser(prog='python -m adventofcode', description='Run Advent of Code solutions and related utilities.')
subparsers = parser.add_subparsers()

parser_run = subparsers.add_parser(
  COMMAND_RUN_SOLUTION,
  aliases=['run'],
  description='Run a solution.',
  help='Run a solution.'
)
parser_run.add_argument('--year', '-y', type=int, help='Year of the solution. If not specified, the most recent year will be used.')
parser_run.add_argument('day', type=int, help='Day of the solution.')
parser_run.set_defaults(func=run_solution)

parser_init = subparsers.add_parser(
  COMMAND_MAKE_NEW_YEAR,
  aliases=['init'],
  description='Set up input, solution, and test directories for a new year of solutions.',
  help='Set up input, solution, and test directories for a new year of solutions.'
)
parser_init.add_argument(
  '--year',
  '-y',
  type=int,
  help=f'Year to create. If not specified, the {SOLUTIONS_DIR_NAME} directory will be inspected and a year after the latest existing year will be created.'
)
parser_init.set_defaults(func=run_make_new_year)

args = parser.parse_args()
args.func(args)
