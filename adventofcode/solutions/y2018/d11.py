'''
Solution for day 11 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 11` from the project root.
'''
from adventofcode.types import Solution
from adventofcode.util import highlight
from typing import DefaultDict, Tuple, NamedTuple
from collections import defaultdict

class SummedAreaFuelGrid:
  '''
  Holds a grid where each cell's value is the sum of all power levels of the cells above and
  to the left of it, including its own power level.
  https://www.codeproject.com/Articles/441226/Haar-feature-Object-Detection-in-Csharp#integral
  '''
  def __init__(self, serial: int, sidelength: int=300) -> None:
    grid = defaultdict(int)
    for x in range(sidelength):
      for y in range(sidelength):
        rack_id = x + 11
        power = (((((rack_id * (y + 1)) + serial) * rack_id) // 100) % 10) - 5
        grid[(x, y)] = (
          power
          + grid[(x - 1, y)]
          + grid[(x, y - 1)]
          - grid[(x - 1, y - 1)]
        )
    self.grid: DefaultDict[Tuple[int, int], int] = grid
    self.sidelength: int = sidelength

  def region_power(self, x: int, y: int, size: int) -> int:
    '''
    Get the total power of a square region in the grid. x and y give the coordinates of the
    top left corner of the region, size gives the sidelength of the square.
    '''
    s = size - 1
    x0, x1, y0, y1 = x - 1, x + s, y - 1, y + s
    return self.grid[(x1, y1)] + self.grid[(x0, y0)] - self.grid[(x1, y0)] - self.grid[(x0, y1)]

  def max_region_power(self, size: int=3) -> Tuple[int, int, int]:
    '''
    Computes the max power region of given size.
    '''
    cutoff = self.sidelength - size + 1
    return max((self.region_power(x, y, size), x, y) for x in range(cutoff) for y in range(cutoff))

def solution_1(fuel_grid: SummedAreaFuelGrid) -> str:
  power, x, y = fuel_grid.max_region_power()
  print('Max power for regions of size 3:', highlight(power), end='\n\n')
  return f'{x + 1},{y + 1}'

def solution_2(fuel_grid: SummedAreaFuelGrid) -> str:
  print('Determining region with overall max power... ')
  power, x, y, size = max(fuel_grid.max_region_power(size) + (size,) for size in range(1, 301))
  print()
  print('Max power overall:', highlight(power, color='g'), 'for region of size', highlight(size))
  return f'{x + 1},{y + 1},{size}'

def run(data: str) -> Solution:
  fuel_grid = SummedAreaFuelGrid(int(data))
  return (solution_1(fuel_grid), solution_2(fuel_grid))
