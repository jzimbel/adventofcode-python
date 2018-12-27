import os
import shutil
import subprocess
from datetime import date
from adventofcode.constants import (
  INPUTS_ROOT,
  SOLUTIONS_ROOT,
  TESTS_ROOT,
  SOLUTION_FILE_TEMPLATE,
  TEST_FILE_TEMPLATE
)
from adventofcode.util import (
  get_latest_year,
  get_year_id,
  get_day_id,
  pad_day,
  highlight
)

def make_new_year(year: int) -> None:
  '''
  Sets up input, solution, and test directories for a new year of puzzle solutions.
  Only fails if the files already exist. Pre-existing directories are A-OK.
  '''

  year_id = get_year_id(year)
  inputs_year_dir_path = os.path.join(INPUTS_ROOT, str(year))
  solutions_year_dir_path = os.path.join(SOLUTIONS_ROOT, year_id)
  tests_year_dir_path = os.path.join(TESTS_ROOT, year_id)
  os.makedirs(inputs_year_dir_path, exist_ok=True)
  os.makedirs(solutions_year_dir_path, exist_ok=True)
  os.makedirs(tests_year_dir_path, exist_ok=True)

  for day in range(1, 26):
    day_id = get_day_id(day)
    solution_file_path = os.path.join(solutions_year_dir_path, '{}.py'.format(day_id))
    with open(solution_file_path, 'x') as solution_file:
      solution_file.write(SOLUTION_FILE_TEMPLATE.format(day=day, year=year))

    # test file names must be unique for pytest to run them correctly
    test_file_path = os.path.join(tests_year_dir_path, 'test_{}_{}.py'.format(year, pad_day(day)))
    with open(test_file_path, 'x') as test_file:
      test_file.write(
        TEST_FILE_TEMPLATE.format(day=day, year=year, zero_padded_day=pad_day(day))
      )
  return (inputs_year_dir_path, solutions_year_dir_path, tests_year_dir_path)

def run_make_new_year(args) -> None:
  year = args.year
  if year is None:
    latest_year = get_latest_year()
    year = date.today().year if latest_year is None else (latest_year + 1)
  elif year < 2000:
    raise ValueError('Year must not be shorthand. E.g. "2018", not "18".')

  paths = make_new_year(year)

  print(highlight('Success.'))
  if shutil.which('tree') is not None:
    trees = '\n'.join(
      subprocess.check_output(['tree', '-C', '--noreport', path]).decode('utf8')
      for path in paths
    )
    print('Created the following directories and files:')
    print(trees)
  else:
    inputs_year_dir_path, solutions_year_dir_path, tests_year_dir_path = paths
    print('Created input directory {}.'.format(highlight(inputs_year_dir_path)))
    print('Created solution directory {} and starter solution files.'.format(highlight(solutions_year_dir_path)))
    print('Created test directory {} and starter test files.'.format(highlight(tests_year_dir_path)))
