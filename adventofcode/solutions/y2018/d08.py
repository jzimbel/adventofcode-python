'''
Solution for day 8 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 8` from the project root.
'''
from adventofcode.types import Solution
from typing import List, Tuple

class Tree:
  def __init__(self, children: List['Tree'], metadata: List[int]) -> None:
    self.children = children
    self.metadata = metadata
    self._value = None

  @classmethod
  def from_list(cls, tree_def: List[int], recursing: bool=False) -> Tuple['Tree', int]:
    child_count, metadata_count = tree_def[:2]
    children = []
    index = 2
    for n in range(child_count):
      child, relative_index = cls.from_list(tree_def[index:], recursing=True)
      index += relative_index
      children.append(child)
    metadata = tree_def[index:index + metadata_count]
    index += metadata_count
    if recursing:
      return cls(children, metadata), index
    else:
      return cls(children, metadata)

  def sum_metadata(self):
    return sum(child.sum_metadata() for child in self.children) + sum(self.metadata)

  def get_value(self):
    if self._value is not None:
      return self._value
    self._value = 0
    if len(self.children) == 0:
      self._value = self.sum_metadata()
    else:
      for metadatum in self.metadata:
        if metadatum == 0 or metadatum > len(self.children):
          continue
        self._value += self.children[metadatum - 1].get_value()
    return self._value

def solution_1(tree: Tree) -> int:
  return tree.sum_metadata()

def solution_2(tree: Tree) -> int:
  return tree.get_value()

def run(data: str) -> Solution:
  tree = Tree.from_list([int(n) for n in data.split()])
  return (solution_1(tree), solution_2(tree))
