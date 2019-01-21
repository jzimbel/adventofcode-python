'''
Solution for day 6 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 6` from the project root.
'''
from typing import List, NamedTuple, Union, Dict
from adventofcode.types import Point, Solution, with_id

IDPoint = with_id(Point)

class IDDistance(NamedTuple):
  id: int
  dist: int

def manhattan(p1: Union[Point, IDPoint], p2: Union[Point, IDPoint]) -> int:
  return abs(p1.x - p2.x) + abs(p1.y - p2.y)

class Voronoi:
  def __init__(self, seeds: List[IDPoint]) -> None:
    self.seeds = seeds
    seeds_x = [p.x for p in seeds]
    seeds_y = [p.y for p in seeds]
    self.x_min = min(seeds_x)
    self.x_max = max(seeds_x)
    self.y_min = min(seeds_y)
    self.y_max = max(seeds_y)
    self._get_initial_grid()
    self._get_qualified_ids()
    self._get_qualified_grid()

  def _get_point_id(self, point):
    distances = [
      IDDistance(seed.id, manhattan(point, seed))
      for seed in self.seeds
    ]
    min_distance = min(distances, key=lambda iddistance: iddistance.dist)
    if len([1 for d in distances if d.dist == min_distance.dist]) == 1:
      # point only gets a label if it's not tied for distance between 2+ seeds
      return min_distance.id
    else:
      return None

  def _get_initial_grid(self):
    self.grid = [
      IDPoint(
        self._get_point_id(Point(x, y)),
        x,
        y
      )
      for x in range(self.x_min, self.x_max + 1)
      for y in range(self.y_min, self.y_max + 1)
    ]

  def _get_qualified_ids(self):
    all_ids = {
      seed.id
      for seed in self.seeds
    }
    edge_ids = {
      idpoint.id
      for idpoint in self.grid
      if idpoint.x in (self.x_min, self.x_max) or idpoint.y in (self.y_min, self.y_max)
    }
    self.qualified_ids = all_ids - edge_ids

  def _get_qualified_grid(self):
    self.grid = [
      point._replace(id=point.id if point.id in self.qualified_ids else None)
      for point in self.grid
    ]

  def get_areas(self):
    areas = {id: 0 for id in self.qualified_ids}
    for point in self.grid:
      if point.id is not None:
        areas[point.id] += 1
    return areas

def solution_1(voronoi: Voronoi) -> int:
  return max(voronoi.get_areas().values())

def run(data: str) -> Solution:
  seeds = [
    IDPoint(
      index,
      *(int(scalar) for scalar in line.split(', '))
    )
    for index, line in enumerate(data.split('\n'))
  ]
  voronoi = Voronoi(seeds)
  return (solution_1(voronoi), None)
