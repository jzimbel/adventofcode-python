'''
Solution for day 6 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 6` from the project root.
'''
from typing import Any, Callable, List, NamedTuple, Union, Dict, Optional
from adventofcode.types import Point, Solution, with_id
from functools import wraps

# TYPE DEFINITIONS

IDPoint = with_id(Point)
PointType = Union[Point, IDPoint]

def newobj(method):
  '''
  method decorator that converts the method to one that creates a new object
  instead of mutating the existing one
  http://kracekumar.com/post/100897281440/fluent-interface-in-python
  '''
  @wraps(method)
  # Well, newobj can be decorated with function, but we will cover the case
  # where it decorated with method
  def inner(self, *args, **kwargs):
      obj = self.__class__.__new__(self.__class__)
      obj.__dict__ = self.__dict__.copy()
      method(obj, *args, **kwargs)
      return obj
  return inner

class IDDistance(NamedTuple):
  id: int
  dist: int

def manhattan(p1: PointType, p2: PointType) -> int:
  return abs(p1.x - p2.x) + abs(p1.y - p2.y)

class SeedGrid:
  def __init__(self, seeds: List[IDPoint], padding: int = 0) -> None:
    self.seeds: List[IDPoint] = seeds
    seeds_x = [p.x for p in seeds]
    seeds_y = [p.y for p in seeds]
    self.x_min: int = min(seeds_x) - padding
    self.x_max: int = max(seeds_x) + padding
    self.y_min: int = min(seeds_y) - padding
    self.y_max: int = max(seeds_y) + padding
    self.grid: List[PointType] = [
      Point(x, y)
      for x in range(self.x_min, self.x_max + 1)
      for y in range(self.y_min, self.y_max + 1)
    ]

  @newobj
  def map_grid(self, func: Callable[[Any, List[IDPoint]], Any]) -> None:
    self.grid = [
      func(point, self.seeds)
      for point in self.grid
    ]

# FUNCTIONS FOR PART 1

def get_id_point(point: Point, seeds: List[IDPoint]) -> IDPoint:
  print(f'Labelling points in x={point.x}    ', end='\r')
  distances = [
    IDDistance(seed.id, manhattan(point, seed))
    for seed in seeds
  ]
  min_distance = min(distances, key=lambda iddistance: iddistance.dist)
  if len([d for d in distances if d.dist == min_distance.dist]) == 1:
    # point only gets a label if it's not tied for distance between 2+ seeds
    return IDPoint(min_distance.id, *point)
  else:
    return IDPoint(None, *point)

def get_qualified_ids(seedGrid: SeedGrid) -> List[int]:
  all_ids = {
    seed.id
    for seed in seedGrid.seeds
  }
  edge_ids = {
    idpoint.id
    for idpoint in seedGrid.grid
    if idpoint.x in (seedGrid.x_min, seedGrid.x_max) or idpoint.y in (seedGrid.y_min, seedGrid.y_max)
  }
  return all_ids - edge_ids

def get_areas(seedGrid: SeedGrid, qualified_ids: List[int]) -> Dict[int, int]:
  areas = {id: 0 for id in qualified_ids}
  for point in seedGrid.grid:
    if point.id is not None:
      areas[point.id] += 1
  return areas

# FUNCTIONS FOR PART 2

def get_sum_distance(point: Point, seeds: List[IDPoint]) -> int:
  print(f'Getting sum distances for points in x={point.x}    ', end='\r')
  return sum(
    manhattan(point, seed)
    for seed in seeds
  )

def solution_1(seeds: List[IDPoint]) -> int:
  seedGrid = SeedGrid(seeds).map_grid(get_id_point)
  print()
  print('Filtering out regions with infinite area')
  qualified_ids = get_qualified_ids(seedGrid)
  voronoi = seedGrid.map_grid(
    lambda point, seeds: point if point.id in qualified_ids else point._replace(id=None)
  )
  return max(get_areas(voronoi, qualified_ids).values())

def solution_2(seeds: List[IDPoint], max_distance: int=10000) -> int:
  # pad the grid in each direction by m, where n seeds * m distance from each seed = max_distance
  padding = max_distance // len(seeds)
  distances = SeedGrid(seeds, padding).map_grid(get_sum_distance).grid
  print()
  return len([d for d in distances if d < max_distance])

def run(data: str) -> Solution:
  seeds = [
    IDPoint(
      index,
      *(int(scalar) for scalar in line.split(', '))
    )
    for index, line in enumerate(data.split('\n'))
  ]
  return (solution_1(seeds), solution_2(seeds))
