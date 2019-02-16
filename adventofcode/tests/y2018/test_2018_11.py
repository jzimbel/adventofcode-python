'''
Test for year 2018, day 11 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d11 import SummedAreaFuelGrid

def test_region_power() -> None:
  '''
  Sum grid looks like
  0  1  3  5 +x
  2  5 10 16
  5 12 12 14
  9 11  8  8
  +y
  '''
  fuel_grid = SummedAreaFuelGrid(6042, sidelength=4)
  assert fuel_grid.region_power(0, 0, 3) == 12
  assert fuel_grid.region_power(0, 0, 4) == 8
  assert fuel_grid.region_power(1, 1, 2) == 12 - 3 - 5
  assert fuel_grid.region_power(0, 1, 3) == 8 - 3
  assert fuel_grid.region_power(2, 2, 2) == 8 + 5 - 16 - 11
  assert fuel_grid.region_power(2, 0, 2) == 16 - 5
