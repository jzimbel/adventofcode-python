import os
import re
from typing import Optional
from adventofcode.constants import (
  DAY_PREFIX,
  END_MARK,
  INPUTS_ROOT,
  MARK,
  SOLUTIONS_ROOT,
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
      int(entry.split(YEAR_PREFIX)[1])
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
    str(year),
    pad_day(day)
  )
  if not os.path.isfile(input_file_path):
    raise Exception('Input file does not exist: {}'.format(input_file_path))
  with open(input_file_path, 'r') as f:
    return f.read().strip()
