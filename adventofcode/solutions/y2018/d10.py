'''
Solution for day 10 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 10` from the project root.
'''
from adventofcode.types import Solution
from typing import List
import re
import math

moving_point_pattern = re.compile(r'(-?\d+)')

class MovingPoint:
  def __init__(self, x: int, y: int, vx: int, vy: int) -> None:
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy

  def advance(self) -> 'MovingPoint':
    return MovingPoint(
      self.x + self.vx,
      self.y + self.vy,
      self.vx,
      self.vy
    )

class PointCanvas:
  def __init__(self, points: List[MovingPoint]) -> None:
    self.points = points

  def __str__(self) -> str:
    return '\n'.join(
      ''.join(
        '#'
        if any(point.x == x and point.y == y for point in self.points)
        else '.'
        for x in range(self.x_min() - 1, self.x_max() + 2)
      )
      for y in range(self.y_min() - 1, self.y_max() + 2)
    )

  def x_min(self) -> int:
    return min(point.x for point in self.points)

  def x_max(self) -> int:
    return max(point.x for point in self.points)

  def y_min(self) -> int:
    return min(point.y for point in self.points)

  def y_max(self) -> int:
    return max(point.y for point in self.points)

  def size(self) -> int:
    return (self.x_max() - self.x_min()) * (self.y_max() - self.y_min())

  def advance(self) -> 'PointCanvas':
    return PointCanvas([point.advance() for point in self.points])

def solution(points: List[MovingPoint]) -> str:
  canvas = PointCanvas(points)
  size = canvas.size()
  previous_canvas = None
  previous_size = math.inf
  elapsed_seconds = 0
  while size < previous_size:
    previous_canvas = canvas
    previous_size = size
    canvas = canvas.advance()
    size = canvas.size()
    elapsed_seconds += 1
  return (f'\n{previous_canvas}', elapsed_seconds - 1)

def run(data: str) -> Solution:
  points = [
    MovingPoint(*(int(n) for n in moving_point_pattern.findall(line)))
    for line in data.split('\n')
  ]
  return solution(points)
