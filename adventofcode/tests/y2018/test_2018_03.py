'''
Test for year 2018, day 3 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d03 import line_to_claim, do_claims_overlap, get_overlapping_claim_cells, run

data = '#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2'

def test_line_to_claim() -> None:
  line = data.split('\n')[0]
  assert line_to_claim(line) == (1, 1, 3, 5, 7)

def test_do_claims_overlap() -> None:
  claims = [line_to_claim(line) for line in data.split('\n')]
  assert do_claims_overlap(claims[0], claims[1]) == True
  assert do_claims_overlap(claims[0], claims[2]) == False
  assert do_claims_overlap(claims[1], claims[2]) == False

def test_get_overlapping_claim_cells() -> None:
  claims = [line_to_claim(line) for line in data.split('\n')]
  assert get_overlapping_claim_cells(claims[0], claims[1]) == {(3,3), (3,4), (4,3), (4,4)}
  assert get_overlapping_claim_cells(claims[0], claims[2]) == set()
  assert get_overlapping_claim_cells(claims[1], claims[2]) == set()

def test_run() -> None:
  assert run(data) == (4, 3)
