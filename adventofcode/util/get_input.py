import os
from adventofcode.constants import (
  DAY_PREFIX,
  INPUT_FILE_NAME,
  PROJECT_ROOT,
  SOLUTIONS_DIR_NAME,
  YEAR_PREFIX
)

def get_input(year: int, day: int) -> str:
  input_file_path = os.path.join(
    PROJECT_ROOT,
    SOLUTIONS_DIR_NAME,
    '{}{}'.format(YEAR_PREFIX, year),
    '{}{}'.format(DAY_PREFIX, str(day).zfill(2)),
    INPUT_FILE_NAME
  )
  if not os.path.isfile(input_file_path):
    raise Exception('Input file does not exist: {}'.format(input_file_path))
  with open(input_file_path, 'r') as f:
    return f.read().strip()