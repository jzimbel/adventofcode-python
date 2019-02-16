'''
Solution for day 11 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 11` from the project root.
'''
from adventofcode.types import Solution
from adventofcode.util import highlight
from typing import Iterator, List, NamedTuple
from itertools import chain

class CellRegion(NamedTuple):
  x: int
  y: int
  size: int
  power: int

class SummedAreaFuelGrid:
  '''
  Holds a grid where each cell's value is the sum of all power levels of the cells above and
  to the left of it, including its own power level.
  https://www.codeproject.com/Articles/441226/Haar-feature-Object-Detection-in-Csharp#integral
  '''
  def __init__(self, serial: int, sidelength: int=300) -> None:
    def power_level(x: int, y: int) -> int:
      rack_id = x + 11
      return (((((rack_id * (y + 1)) + serial) * rack_id) // 100) % 10) - 5
    grid = [[None] * sidelength for _ in range(sidelength)]
    for x in range(sidelength):
      for y in range(sidelength):
        power = (grid[x - 1][y] if x > 0 else 0) + sum(power_level(x, Y) for Y in range(y + 1))
        grid[x][y] = power
    self.grid: List[List[int]] = grid
    self.sidelength: int = sidelength

  def region_power(self, x: int, y: int, size: int) -> int:
    '''
    Get the total power of a square region in the grid. x and y give the coordinates of the
    top left corner of the region, size gives the sidelength of the square.

    Throws IndexError if the region extends past the end of the grid.
    '''
    s = size - 1
    bottom_right_sum = self.grid[x + s][y + s]
    top_left_sum = 0 if x == 0 or y == 0 else self.grid[x - 1][y - 1]
    top_right_sum = 0 if y == 0 else self.grid[x + s][y - 1]
    bottom_left_sum = 0 if x == 0 else self.grid[x - 1][y + s]
    return bottom_right_sum + top_left_sum - top_right_sum - bottom_left_sum

  def region_powers(self, size: int=3) -> Iterator[CellRegion]:
    '''
    Generator that yields CellRegions giving the power levels for each region of size `size`
    within the grid.
    '''
    cutoff = self.sidelength - size + 1
    for x in range(cutoff):
      for y in range(cutoff):
        yield CellRegion(x, y, size, self.region_power(x, y, size))
    print('Done searching regions of size', highlight(size), end='\r')

def solution_1(fuel_grid: SummedAreaFuelGrid) -> str:
  x, y, size, power = max(fuel_grid.region_powers(), key=lambda cell_region: cell_region.power)
  print('Max power for regions of size 3:', highlight(power), end='\n\n')
  return f'{x + 1},{y + 1}'

def solution_2(fuel_grid: SummedAreaFuelGrid) -> str:
  all_region_powers = (
    fuel_grid.region_powers(size=size)
    for size in range(1, 301)
  )
  print('Determining region with overall max power... ')
  x, y, size, power = max(chain.from_iterable(all_region_powers), key=lambda cell_region: cell_region.power)
  print()
  print('Max power overall:', highlight(power, color='g'), 'for region of size', highlight(size))
  return f'{x + 1},{y + 1},{size}'

def run(data: str) -> Solution:
  print('Constructing summed area table for fuel grid... ', end='', flush=True)
  fuel_grid = SummedAreaFuelGrid(int(data))
  print('Done.\n')
  return (solution_1(fuel_grid), solution_2(fuel_grid))
