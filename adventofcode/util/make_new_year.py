import os
from adventofcode.constants import (
  DAY_PREFIX,
  PROJECT_ROOT,
  SOLUTION_FILE_NAME,
  SOLUTION_FILE_TEMPLATE,
  TEST_FILE_TEMPLATE,
  SOLUTIONS_DIR_NAME,
  TESTS_ROOT,
  YEAR_PREFIX
)

def make_new_year(year: int) -> None:
  if year < 2000:
    raise ValueError('Year must not be shorthand. E.g. "2018", not "18".')
  year_dir = '{}{}'.format(YEAR_PREFIX, year)
  year_dir_path = os.path.join(PROJECT_ROOT, SOLUTIONS_DIR_NAME, year_dir)
  os.mkdir(year_dir_path, mode=0o755)
  tests_year_dir_path = os.path.join(TESTS_ROOT, SOLUTIONS_DIR_NAME, year_dir)
  os.mkdir(tests_year_dir_path, mode=0o755)

  days = ['d{}'.format(str(n).zfill(2)) for n in range(1, 26)]
  for day in days:
    day_dir = '{}{}'.format(DAY_PREFIX, day)
    day_dir_path = os.path.join(year_dir_path, day_dir)
    os.mkdir(day_dir_path, mode=0o755)
    tests_day_dir_path = os.path.join(tests_year_dir_path, day_dir)
    os.mkdir(tests_day_dir_path, mode=0o755)

    with open(os.path.join(day_dir_path, SOLUTION_FILE_NAME), 'x') as solution_file:
      solution_file.write(SOLUTION_FILE_TEMPLATE.format(day=day, year=year))
    with open(os.path.join(tests_day_dir_path, 'test_{}'.format(SOLUTION_FILE_NAME)), 'x') as test_file:
      test_file.write(TEST_FILE_TEMPLATE.format(day=day, year=year))
  print('Success. Created {} and subdirectories + solution file boilerplate.'.format(year_dir_path))
