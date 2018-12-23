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
  tests_year_dir_path = os.path.join(TESTS_ROOT, year_dir)
  os.mkdir(tests_year_dir_path, mode=0o755)

  for day in range(1, 26):
    zero_padded_day = str(day).zfill(2)
    day_dir = '{}{}'.format(DAY_PREFIX, zero_padded_day)
    day_dir_path = os.path.join(year_dir_path, day_dir)
    os.mkdir(day_dir_path, mode=0o755)
    tests_day_dir_path = os.path.join(tests_year_dir_path, day_dir)
    os.mkdir(tests_day_dir_path, mode=0o755)

    solution_file_path = os.path.join(day_dir_path, SOLUTION_FILE_NAME)
    with open(solution_file_path, 'x') as solution_file:
      solution_file.write(SOLUTION_FILE_TEMPLATE.format(day=day, year=year))
    test_file_path = os.path.join(tests_day_dir_path, 'test_{}_{}_{}'.format(year, day, SOLUTION_FILE_NAME))
    with open(test_file_path, 'x') as test_file:
      test_file.write(
        TEST_FILE_TEMPLATE.format(day=day, year=year, zero_padded_day=zero_padded_day, test_file_path=test_file_path)
      )
  print('Success. Created {} and subdirectories + starter solution files.'.format(year_dir_path))
  print('Also created test directory {}.'.format(tests_year_dir_path))
