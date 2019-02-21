'''
Test for year 2018, day 13 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.types import Point
from adventofcode.solutions.y2018.d13 import NORTH, EAST, SOUTH, WEST, Cart, run

data = r'''/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/'''

def test_cart() -> None:
  cart = Cart(Point(0, 0), '^')
  assert cart.location == (0, 0)
  assert cart.direction == NORTH

def test_cart_move_straight() -> None:
  cart1 = Cart(Point(5, 6), '>')
  cart1.move('-')
  assert cart1.location == (6, 6)
  assert cart1.direction == EAST

  cart2 = Cart(Point(18, 7), 'v')
  cart2.move('|')
  assert cart2.x == 18
  assert cart2.y == 8
  assert cart2.direction == SOUTH

def test_cart_move_corner() -> None:
  cart1 = Cart(Point(1, 1), '^')
  cart1.move('/')
  assert cart1.location == (2, 1)
  assert cart1.direction == EAST
  cart1.move('\\')
  assert cart1.location == (2, 2)
  assert cart1.direction == SOUTH

  cart2 = Cart(Point(1, 1), '^')
  cart2.move('\\')
  assert cart2.location == (0, 1)
  assert cart2.direction == WEST
  cart2.move('/')
  assert cart2.location == (0, 2)
  assert cart2.direction == SOUTH

def test_cart_move_intersection() -> None:
  cart = Cart(Point(5, 5), '>')
  cart.move('+')
  assert cart.location == (5, 4)
  assert cart.direction == NORTH
  cart.move('+')
  assert cart.location == (5, 3)
  assert cart.direction == NORTH
  cart.move('+')
  assert cart.location == (6, 3)
  assert cart.direction == EAST
  cart.move('+')
  assert cart.location == (6, 2)
  assert cart.direction == NORTH

def test_cart_move_collision_detection() -> None:
  cart1 = Cart(Point(3, 4), '>')
  cart2 = Cart(Point(3, 5), 'v')
  cart3 = Cart(Point(4, 4), '^')
  cart4 = Cart(Point(4, 5), '<')
  others = [cart2, cart3, cart4]

  cart1.move('-', others)
  assert cart1.crashed
  assert cart3.crashed
  assert not cart2.crashed
  assert not cart4.crashed

def test_cart_equality() -> None:
  cart1 = Cart(Point(4, 6), '^')
  cart2 = Cart(Point(4, 6), '>')
  cart3 = Cart(Point(5, 6), '^')
  assert cart1 == cart2
  assert cart1 != cart3
  assert cart2 != cart3

def test_cart_inequality() -> None:
  cart1 = Cart(Point(3, 7), '>') # after move == 3,6
  cart2 = Cart(Point(2, 7), 'v') # after move == 3,7
  cart3 = Cart(Point(1, 8), '^') # after move == 0,8
  assert cart1 > cart2
  assert cart2 < cart1
  assert cart1 < cart3
  assert cart2 < cart3

  carts = sorted([cart1, cart2, cart3])
  assert carts == [cart2, cart1, cart3]
  for cart in carts:
    cart.move('+')
  carts.sort()
  assert carts == [cart1, cart2, cart3]

def test_run() -> None:
  assert run(data) == ('2,0', '6,4')
