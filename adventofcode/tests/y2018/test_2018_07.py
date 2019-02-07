'''
Test for year 2018, day 7 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2018.d07 import solution_1, solution_2, dependency_pattern, Dependency
from typing import NamedTuple
from collections import OrderedDict

data = \
'''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''

dependencies = [
  Dependency(*dependency_pattern.match(line).groups())
  for line in data.split('\n')
]
deps_by_step = OrderedDict((step, set()) for step in 'ABCDEF')
for dep in dependencies:
  deps_by_step[dep.successor].add(dep.predecessor)

def test_solution_1() -> None:
  assert solution_1(deps_by_step) == 'CABDFE'

def test_solution_2() -> None:
  assert solution_2(deps_by_step, num_workers=2, base_step_duration=0) == 15
