import os
from typing import Optional
from adventofcode.constants import (
  DAY_PREFIX,
  END_MARK,
  INPUT_FILE_NAME,
  MARK,
  PROJECT_ROOT,
  SOLUTION_FILE_NAME,
  SOLUTION_FILE_TEMPLATE,
  SOLUTIONS_DIR_NAME,
  TEST_FILE_TEMPLATE,
  TESTS_ROOT,
  YEAR_PREFIX
)

def pad_day(day: int) -> str:
  '''
  Pad a day value with zeros so that it sorts correctly with `ls`.
  '''
  return str(day).zfill(2)

def get_day_dir(day: int) -> str:
  '''
  Gets the day directory name for a given day number.
  '''
  return '{}{}'.format(DAY_PREFIX, pad_day(day))

def get_year_dir(year: int) -> str:
  '''
  Gets the year directory name for a given year number.
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
  solutions_dir_path = os.path.join(PROJECT_ROOT, SOLUTIONS_DIR_NAME)
  try:
    return max(
      int(entry[1:])
      for entry in os.listdir(solutions_dir_path)
      if re.fullmatch(r'y\d+', entry)
    )
  except ValueError:
    return None

def get_input(year: int, day: int) -> str:
  '''
  Loads an input.txt file into a string and returns it.
  '''
  input_file_path = os.path.join(
    PROJECT_ROOT,
    SOLUTIONS_DIR_NAME,
    get_year_dir(year),
    get_day_dir(day),
    INPUT_FILE_NAME
  )
  if not os.path.isfile(input_file_path):
    raise Exception('Input file does not exist: {}'.format(input_file_path))
  with open(input_file_path, 'r') as f:
    return f.read().strip()

def make_new_year(year: int) -> None:
  '''
  Sets up solution and test directories for a new year of puzzle solutions.
  '''
  if year < 2000:
    raise ValueError('Year must not be shorthand. E.g. "2018", not "18".')

  year_dir = get_year_dir(year)
  year_dir_path = os.path.join(PROJECT_ROOT, SOLUTIONS_DIR_NAME, year_dir)
  os.mkdir(year_dir_path)
  tests_year_dir_path = os.path.join(TESTS_ROOT, year_dir)
  os.mkdir(tests_year_dir_path)

  for day in range(1, 26):
    day_dir = get_day_dir(day)
    day_dir_path = os.path.join(year_dir_path, day_dir)
    os.mkdir(day_dir_path)
    solution_file_path = os.path.join(day_dir_path, SOLUTION_FILE_NAME)
    with open(solution_file_path, 'x') as solution_file:
      solution_file.write(SOLUTION_FILE_TEMPLATE.format(day=day, year=year))

    tests_day_dir_path = os.path.join(tests_year_dir_path, day_dir)
    os.mkdir(tests_day_dir_path)
    # test file names must be unique for pytest to run them correctly
    test_file_path = os.path.join(tests_day_dir_path, 'test_{}_{}_{}'.format(year, day, SOLUTION_FILE_NAME))
    with open(test_file_path, 'x') as test_file:
      test_file.write(
        TEST_FILE_TEMPLATE.format(day=day, year=year, zero_padded_day=pad_day(day), test_file_path=test_file_path)
      )

  print(highlight('Success.'))
  print('Created {} and subdirectories + starter solution files.'.format(highlight(year_dir_path)))
  print('Also created test directory {}.'.format(highlight(tests_year_dir_path)))
