import shutil
import subprocess
import sys
import os
import re
from typing import Optional
from adventofcode.constants import (
  DAY_PREFIX,
  END_MARK,
  INPUTS_ROOT,
  MARK,
  SOLUTION_FILE_TEMPLATE,
  SOLUTIONS_ROOT,
  TEST_FILE_TEMPLATE,
  TESTS_ROOT,
  YEAR_PREFIX
)

def pad_day(day: int) -> str:
  '''
  Pad a day value with zeros so that it sorts correctly with `ls`.
  '''
  return str(day).zfill(2)

def get_day_id(day: int) -> str:
  '''
  Gets the day identifier for a given day number.

  >>> get_day_id(5)
  'd05'
  '''
  return '{}{}'.format(DAY_PREFIX, pad_day(day))

def get_year_id(year: int) -> str:
  '''
  Gets the year identifier for a given year number.

  >>> get_year_id(2018)
  'y2018'
  '''
  return '{}{}'.format(YEAR_PREFIX, year)

def highlight(text: str) -> str:
  '''
  Surround a string in ANSI escape codes to make it stand out when printed.
  '''
  return '{}{}{}'.format(MARK, text, END_MARK)

def get_latest_year() -> Optional[int]:
  '''
  Search the solutions directory for the latest year, and return it.
  Returns None if directory is empty.
  '''
  try:
    return max(
      int(entry[1:])
      for entry in os.listdir(SOLUTIONS_ROOT)
      if re.fullmatch(r'y\d+', entry)
    )
  except ValueError:
    return None

def get_input(year: int, day: int) -> str:
  '''
  Loads an input file into a string and returns it.
  '''
  input_file_path = os.path.join(
    INPUTS_ROOT,
    get_year_id(year),
    '{}'.format(get_day_id(day))
  )
  if not os.path.isfile(input_file_path):
    raise Exception('Input file does not exist: {}'.format(input_file_path))
  with open(input_file_path, 'r') as f:
    return f.read().strip()

def make_new_year(year: int) -> None:
  '''
  Sets up input, solution, and test directories for a new year of puzzle solutions.
  Only fails if the files already exist. Pre-existing directories are A-OK.
  '''
  if year < 2000:
    raise ValueError('Year must not be shorthand. E.g. "2018", not "18".')

  year_id = get_year_id(year)
  inputs_year_dir_path = os.path.join(INPUTS_ROOT, year_id)
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

  print(highlight('Success.'))
  if shutil.which('tree') is not None:
    trees = ('\n' + '-' * 50 + '\n\n').join(
      subprocess.check_output(['tree', '-C', '--noreport', path]).decode('utf8')
      for path in (inputs_year_dir_path, solutions_year_dir_path, tests_year_dir_path)
    )
    print('Created the following directories and files:')
    print(trees)
  else:
    print('Created input directory {}.'.format(highlight(inputs_year_dir_path)))
    print('Created solution directory {} and starter solution files.'.format(highlight(solutions_year_dir_path)))
    print('Created test directory {} and starter test files.'.format(highlight(tests_year_dir_path)))
