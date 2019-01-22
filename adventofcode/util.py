import os
import re
import requests
from typing import Optional, Any
from adventofcode.constants import (
  AOC_URL,
  DAY_PREFIX,
  END_MARK,
  INPUTS_ROOT,
  MARKS,
  SOLUTIONS_ROOT,
  USER_AGENT,
  USER_SESSION_ID_FILE_PATH,
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
  return f'{DAY_PREFIX}{pad_day(day)}'

def get_year_id(year: int) -> str:
  '''
  Gets the year identifier for a given year number.

  >>> get_year_id(2018)
  'y2018'
  '''
  return f'{YEAR_PREFIX}{year}'

def highlight(text: Any, color: str='b') -> str:
  '''
  Surround a value in ANSI escape codes to make it stand out when printed.
  '''
  return f'{MARKS[color]}{text}{END_MARK}'

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

def get_user_session_id() -> str:
  '''
  Retrieves unique user session id from the file in the project, or asks the user to provide it if the file doesn't exist.
  '''
  if os.path.isfile(USER_SESSION_ID_FILE_PATH):
    with open(USER_SESSION_ID_FILE_PATH) as f:
      return f.read().strip()
  else:
    done = False
    user_session_id = ''
    print('What is your session id? It\'s needed for downloading puzzle inputs.')
    print('Your id is the value of the cookie named', highlight('session'), f'on {highlight(AOC_URL)}.')
    while not done:
      user_session_id = input(f"{highlight('>', color='r')} ")
      user_session_id = user_session_id.strip()
      if re.fullmatch(r'[\da-f]+', user_session_id):
        with open(USER_SESSION_ID_FILE_PATH, 'w') as f:
          f.write(user_session_id)
        done = True
        print('Thanks.')
      else:
        print('That\'s not a valid id. It should consist only of digits and lowercase letters a-f. Please try again.')
    return user_session_id

def download_input(year: int, day: int, input_file_path: str) -> bool:
  '''
  Attempts to download and save the given input from the Advent of Code site.
  Returns a boolean indicating success/failure.
  '''
  print('Input file', highlight(input_file_path, color='r'), 'does not exist.')
  print(f'Attempting to download puzzle input from {highlight(AOC_URL)}.')
  result = None
  error_count = 0
  while result is None:
    try:
      response = requests.get(
        url=f'{AOC_URL}/{year}/day/{day}/input',
        cookies={'session': get_user_session_id()},
        headers={'User-Agent': USER_AGENT}
      )
      if response.ok:
        os.makedirs(os.path.dirname(input_file_path), exist_ok=True)
        with open(input_file_path, 'w') as f:
          f.write(response.text)
        print(highlight('Success.', color='g'), 'Input downloaded and saved to', f'{highlight(input_file_path)}.')
        result = True
      else:
        print('Server responded with a non-200 status code:', f"{highlight(response.status_code, color='y')}.")
        print('Aborting.')
        result = False
    except requests.exceptions.RequestException:
      error_count += 1
      if error_count >= 2:
        print('Giving up.')
        result = False
      elif error_count == 0:
        print('Error while requesting input from server. Request probably timed out. Trying again.')
      else:
        print('Trying again.')
    except Exception as e:
      print('Unhandled error while requesting input from server. ' + str(e))
      result = False
  print()
  return result


def get_input(year: int, day: int) -> str:
  '''
  Loads an input file into a string and returns it.
  '''
  input_file_path = os.path.join(
    INPUTS_ROOT,
    str(year),
    pad_day(day)
  )
  if not os.path.isfile(input_file_path) and not download_input(year, day, input_file_path):
    raise Exception('Could not retrieve input for the puzzle.')
  with open(input_file_path, 'r') as f:
    return f.read().strip()
