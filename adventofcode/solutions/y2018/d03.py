'''
Solution for day 3 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 3` from the project root.
'''
from typing import List, NamedTuple, Set
from adventofcode.types import Solution, Point

class Claim(NamedTuple):
  id: int
  xmin: int
  ymin: int
  xmax: int
  ymax: int

def line_to_claim(line: str) -> Claim:
  parts = line.split(' ')
  xmin = int(parts[2].split(',')[0])
  ymin = int(parts[2].split(',')[1][:-1])
  return Claim(
    int(parts[0][1:]),
    xmin,
    ymin,
    xmin + int(parts[3].split('x')[0]),
    ymin + int(parts[3].split('x')[1])
  )

def do_claims_overlap(claim1: Claim, claim2: Claim) -> bool:
  # https://stackoverflow.com/a/306332
  return (
    claim1.xmin < claim2.xmax
    and claim1.xmax > claim2.xmin
    and claim1.ymin < claim2.ymax
    and claim1.ymax > claim2.ymin
  )

def get_overlapping_claim_cells(claim1: Claim, claim2: Claim) -> Set[Point]:
  claim1_cells = set(Point(x, y) for x in range(claim1.xmin, claim1.xmax) for y in range(claim1.ymin, claim1.ymax))
  claim2_cells = set(Point(x, y) for x in range(claim2.xmin, claim2.xmax) for y in range(claim2.ymin, claim2.ymax))
  return claim1_cells.intersection(claim2_cells)

def solution_1(claims: List[Claim]) -> int:
  overlapping_cells = set()
  for i, claim1 in enumerate(claims):
    print(len(overlapping_cells), 'square inches of overlap found', end='\r')
    for claim2 in claims[i+1:]:
      if do_claims_overlap(claim1, claim2):
        overlapping_cells.update(get_overlapping_claim_cells(claim1, claim2))
  print()
  return len(overlapping_cells)

def solution_2(claims: List[Claim]) -> int:
  # stores ids of claims that have already been found to overlap with another claim
  claim_id_blacklist = set()
  for i, claim1 in enumerate(claims):
    if claim1.id in claim_id_blacklist:
      print('Skipping claim', claim1.id, end='\r')
      continue
    print('Checking claim', claim1.id, end='\r')
    has_overlap = False
    for claim2 in claims[:i] + claims[i+1:]:
      if do_claims_overlap(claim1, claim2):
        has_overlap = True
        claim_id_blacklist.add(claim2.id)
    if not has_overlap:
      print()
      return claim1.id

def run(data: str) -> Solution:
  claims = [line_to_claim(line) for line in data.split('\n')]
  return (solution_1(claims), solution_2(claims))
