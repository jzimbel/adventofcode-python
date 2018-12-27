from datetime import date
from adventofcode.util import (
  get_latest_year,
  make_new_year
)

def run_make_new_year(args) -> None:
  year = args.year
  if year is None:
    latest_year = get_latest_year()
    year = date.today().year if latest_year is None else (latest_year + 1)
  make_new_year(year)
