'''
Solution for day 7 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 7` from the project root.
'''
from adventofcode.types import Solution
from typing import Generator, List, NamedTuple, Optional, OrderedDict as OrderedDictType, Set
import re
from collections import OrderedDict
from string import ascii_uppercase

class Dependency(NamedTuple):
  predecessor: str
  successor: str

dependency_pattern = re.compile(r'Step (.) must be finished before step (.)')

class Worker:
  def __init__(self, base_step_duration: int) -> None:
    self.base_step_duration: int = base_step_duration
    self.step: Optional[str] = None
    self.seconds_remaining: int = 0

  def assign_step(self, step: str) -> None:
    self.step = step
    self.seconds_remaining = ord(step) + self.base_step_duration - 64

  def complete_step(self) -> str:
    completed_step = self.step
    self.step = None
    return completed_step

  def perform_second_of_work(self) -> None:
    if self.step is not None:
      self.seconds_remaining -= 1

  def is_done(self) -> bool:
    return self.step is not None and self.seconds_remaining == 0

  def is_ready_to_receive_new_step(self) -> bool:
    return self.step is None

class AssemblyCrew:
  def __init__(self, deps_by_step: OrderedDictType[str, Set[str]], num_workers: int, base_step_duration: int) -> None:
    self.num_steps = len(deps_by_step)
    self.deps_by_step = deps_by_step
    self.workers = [
      Worker(base_step_duration)
      for x in range(num_workers)
    ]
    self.elapsed_seconds = 0
    self.in_progress_steps = set()
    self.completed_steps = []

  def get_available_steps(self) -> Generator[str, None, None]:
    return (
      step
      for step, predecessors in self.deps_by_step.items()
      if (
        step not in self.in_progress_steps
        and step not in self.completed_steps
        and len(predecessors - set(self.completed_steps)) == 0
      )
    )

  def get_next_available_worker_index(self) -> Optional[int]:
    try:
      return next(i for i, w in enumerate(self.workers) if w.is_ready_to_receive_new_step())
    except StopIteration:
      return None

  def assign_worker(self, worker_index: int, step_to_assign: str) -> None:
    self.workers[worker_index].assign_step(step_to_assign)
    self.in_progress_steps.add(step_to_assign)

  def mark_step_complete(self, step: str) -> None:
    self.in_progress_steps.remove(step)
    self.completed_steps.append(step)

  def perform_second_of_work(self) -> None:
    # assign available workers to any available new steps
    for available_step in self.get_available_steps():
      available_worker_index = self.get_next_available_worker_index()
      if available_worker_index is not None:
        self.assign_worker(available_worker_index, available_step)
      else:
        break
    if self.elapsed_seconds % 10 == 0:
      print(self.elapsed_seconds, *(w.step if w.step is not None else '.' for w in self.workers), ''.join(self.completed_steps), sep='\t')
    # call perform_second_of_work on each worker
    for worker in self.workers:
      worker.perform_second_of_work()
      # unassign if done and update completed_steps
      if worker.is_done():
        self.mark_step_complete(worker.complete_step())
    # increment elapsed_seconds
    self.elapsed_seconds += 1

  def is_done(self) -> bool:
    return len(self.completed_steps) == self.num_steps

  def assemble(self) -> int:
    print('Second', *(f'Wrkr {n+1}' for n, w in enumerate(self.workers)), 'Done', sep='\t')
    while not self.is_done():
      self.perform_second_of_work()
    return self.elapsed_seconds

def solution_1(deps_by_step: OrderedDictType[str, Set[str]]) -> str:
  ordered_steps = []
  while len(deps_by_step) > 0:
    next_step = next(step for step, predecessors in deps_by_step.items() if len(predecessors) == 0)
    ordered_steps.append(next_step)
    deps_by_step = OrderedDict(
      (step, predecessors - {next_step})
      for step, predecessors in deps_by_step.items() if step != next_step
    )
  return ''.join(ordered_steps)

def solution_2(deps_by_step: OrderedDictType[str, Set[str]], num_workers: int=5, base_step_duration: int=60) -> int:
  assembly_crew = AssemblyCrew(deps_by_step, num_workers, base_step_duration)
  return assembly_crew.assemble()

def run(data: str) -> Solution:
  dependencies = [
    Dependency(*dependency_pattern.match(line).groups())
    for line in data.split('\n')
  ]
  deps_by_step = OrderedDict((step, set()) for step in ascii_uppercase)
  for dep in dependencies:
    deps_by_step[dep.successor].add(dep.predecessor)
  return (solution_1(deps_by_step), solution_2(deps_by_step))
