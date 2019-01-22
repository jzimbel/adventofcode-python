import importlib
from adventofcode.util import (
  get_day_id,
  get_input,
  get_latest_year,
  get_year_id,
  highlight
)

def run_solution(args) -> None:
  year = args.year
  day = args.day
  if year is None:
    year = get_latest_year()
  solution_module_path = f'adventofcode.solutions.{get_year_id(year)}.{get_day_id(day)}'
  solution_module = importlib.import_module(solution_module_path)
  data = get_input(year, day)
  print(f'Running solution for year {highlight(year)}, day {highlight(day)}.')
  print()
  answer1, answer2 = solution_module.run(data)
  print()
  print(highlight('Solutions found.', color='g'))
  print()
  print('Answer to puzzle 1:', highlight(answer1, color='g'))
  print('Answer to puzzle 2:', highlight(answer2, color='g'))
