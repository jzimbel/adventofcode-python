'''
Custom type definitions used in this project.
'''
from typing import Any, List, NamedTuple, Tuple

Solution = Tuple[Any, Any]

class Point(NamedTuple):
  x: int
  y: int

def extend_named_tuple(nt: NamedTuple, new_name: str, new_fields: List[Tuple[str, type]], prepend_new_fields: bool=False):
  '''
  Utility function to produce a new named tuple that extends an existing one. Useful for adding label and other metadata fields to data tuples.
  '''
  if prepend_new_fields:
    fields = new_fields + list(nt._field_types.items())
  else:
    fields = list(nt._field_types.items()) + new_fields
  return NamedTuple(new_name, fields)

def with_id(nt: NamedTuple) -> NamedTuple:
  '''
  Takes a named tuple type and produces a new one with an 'id' field of type int at index 0.
  >>> IDPoint = with_id(Point)
  >>> IDPoint(99, 3, 4)
  IDPoint(id=99, x=3, y=4)
  '''
  return extend_named_tuple(nt, 'ID{}'.format(nt.__name__), [('id', int)], prepend_new_fields=True)
