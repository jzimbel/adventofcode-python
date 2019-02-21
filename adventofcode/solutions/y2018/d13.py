'''
Solution for day 13 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 13` from the project root.
'''
from adventofcode.types import Solution, Point
from typing import Any, Dict, Iterable, List, Tuple
from collections import deque

TrackMap = Dict[Point, str]
CartDescriptor = Tuple[Point, str]

LEFT     = -1
STRAIGHT = 0
RIGHT    = 1

NORTH = Point(0, -1)
EAST  = Point(1, 0)
SOUTH = Point(0, 1)
WEST  = Point(-1, 0)

STRAIGHT_NS  = '|'
STRAIGHT_EW  = '-'
CORNERS      = '/\\'
INTERSECTION = '+'

DIRECTION_ORDER = [WEST, SOUTH, EAST, NORTH]
TURN_ORDER = [RIGHT, STRAIGHT, LEFT]
CART_SYMBOLS = {
  '^': NORTH,
  '>': EAST,
  'v': SOUTH,
  '<': WEST
}

class Cart:
  def __init__(self, location: Point, symbol: str) -> None:
    self.x = location.x
    self.y = location.y
    self._directions = deque(DIRECTION_ORDER)
    starting_direction = CART_SYMBOLS[symbol]
    while self.direction != starting_direction:
      self._directions.rotate()
    self._turns = deque(TURN_ORDER)
    self.crashed = False

  def move(self, track_piece: str, others: Iterable['Cart']=[]) -> None:
    '''
    Move this cart and determine if it's collided with another cart.
    '''
    if track_piece == INTERSECTION:
      self._handle_intersection()
    elif track_piece in CORNERS:
      self._handle_corner(track_piece)
    v = self.direction
    self.x += v.x
    self.y += v.y
    for other in others:
      if self == other:
        self.crashed = True
        other.crashed = True
        break

  def _handle_corner(self, track_piece: str) -> None:
    if track_piece == '/':
      self._directions.rotate(RIGHT if self.direction.x == 0 else LEFT)
    else:
      self._directions.rotate(LEFT if self.direction.x == 0 else RIGHT)

  def _handle_intersection(self) -> None:
    self._directions.rotate(self._turns[-1])
    self._turns.rotate()

  @property
  def direction(self) -> Point:
    return self._directions[-1]

  @property
  def location(self) -> Point:
    return Point(self.x, self.y)

  def __eq__(self, other: Any) -> bool:
    return isinstance(other, Cart) and self.location == other.location

  def __lt__(self, other: Any) -> bool:
    return isinstance(other, Cart) and (self.y, self.x) < (other.y, other.x)

def shared_solution(track_map: TrackMap, cart_descriptors: List[CartDescriptor]) -> str:
  carts = sorted(Cart(*descriptor) for descriptor in cart_descriptors)
  collision_location = None
  while len(carts) > 1:
    numbered_carts = list(enumerate(carts))
    for i, cart in numbered_carts:
      if cart.crashed:
        continue
      cart.move(
        track_map[cart.location],
        (other for n, other in numbered_carts if n != i and not other.crashed)
      )
      if collision_location is None and cart.crashed:
        collision_location = cart.location
    carts = sorted(c for c in carts if not c.crashed)
  x1, y1 = collision_location
  x2, y2 = carts[0].location
  return (f'{x1},{y1}', f'{x2},{y2}')

def run(data: str) -> Solution:
  track_map = {}
  cart_descriptors = []
  for y, line in enumerate(data.split('\n')):
    for x, char in enumerate(line):
      location = Point(x, y)
      if char in CART_SYMBOLS:
        cart_descriptors.append((location, char))
        if char in '^v':
          track_map[location] = STRAIGHT_NS
        else:
          track_map[location] = STRAIGHT_EW
      else:
        track_map[location] = char
  return shared_solution(track_map, cart_descriptors)
