'''
Solution for day 4 of the 2018 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2018 4` from the project root.
'''
from typing import DefaultDict, List, NamedTuple
from datetime import datetime
from collections import defaultdict
import re
from functools import reduce
from operator import concat
from adventofcode.types import Solution
from adventofcode.util import highlight

class Record(NamedTuple):
  timestamp: datetime
  event: str

record_matcher = re.compile(r'\[(?P<timestamp>.*)\] (?P<event>.*)')
guard_id_matcher = re.compile(r'Guard #(?P<id>\d+)')

def get_record(line: str) -> Record:
  match = record_matcher.match(line)
  timestamp = datetime.fromisoformat(match.group('timestamp'))
  event = match.group('event')
  return Record(timestamp, event)

def get_records_by_guard_id(records: List[Record]) -> DefaultDict[int, List[int]]:
  records_by_guard_id = defaultdict(lambda: [0 for minute_index in range(60)])
  guard_id = None
  sleep_timestamp = None
  for timestamp, event in records:
    match = guard_id_matcher.match(event)
    if match:
      guard_id = int(match.group('id'))
    elif event == 'falls asleep':
      sleep_timestamp = timestamp
    else:
      sleep_range = range(sleep_timestamp.minute, timestamp.minute)
      records_by_guard_id[guard_id] = [
        (sleep_count + 1)
        if minute_index in sleep_range
        else sleep_count
        for minute_index, sleep_count
        in enumerate(records_by_guard_id[guard_id])
      ]
  return records_by_guard_id

def solution_1(records_by_guard_id: DefaultDict[int, List[int]]) -> int:
  id_of_guard_that_sleeps_the_most = max(records_by_guard_id.items(), key=lambda indexed_tuple: sum(indexed_tuple[1]))[0]
  total_minutes_slept_by_that_guard = sum(records_by_guard_id[id_of_guard_that_sleeps_the_most])
  indexed_minute_most_slept_by_that_guard = max(enumerate(records_by_guard_id[id_of_guard_that_sleeps_the_most]), key=lambda indexed_tuple: indexed_tuple[1])
  solution = id_of_guard_that_sleeps_the_most * indexed_minute_most_slept_by_that_guard[0]
  print(
    'Guard #{} slept the most minutes ({}).'.format(highlight(id_of_guard_that_sleeps_the_most), highlight(total_minutes_slept_by_that_guard)),
    'They spent minute 00:{}'.format(highlight(indexed_minute_most_slept_by_that_guard[0])),
    'sleeping most often--they were asleep during that minute on',
    highlight(indexed_minute_most_slept_by_that_guard[1]),
    'different days.'
  )
  print('{} * {} = {}'.format(id_of_guard_that_sleeps_the_most, indexed_minute_most_slept_by_that_guard[0], highlight(solution, color='g')))
  return solution

def solution_2(records_by_guard_id: DefaultDict[int, List[int]]) -> int:
  # restructure records_by_guard_id into a flat list of (guard_id, minute, sleep_count) tuples
  combined_records = reduce(
    concat,
    (
      [
        (guard_id, minute, record)
        for minute, record in enumerate(records)
      ]
      for guard_id, records in records_by_guard_id.items()
    )
  )
  sleepiest_minute_guard_id, sleepiest_minute, sleep_count = max(combined_records, key=lambda x: x[2])
  solution = sleepiest_minute_guard_id * sleepiest_minute
  print(
    'Guard #{} spent minute 00:{}'.format(highlight(sleepiest_minute_guard_id), highlight(sleepiest_minute)),
    'sleeping more than any other guard spent any other single minute sleeping.',
    'They were asleep during that minute on',
    highlight(sleep_count),
    'different days.'
  )
  print('{} * {} = {}'.format(sleepiest_minute_guard_id, sleepiest_minute, highlight(solution, color='g')))
  return solution

def run(data: str) -> Solution:
  records = [get_record(line) for line in data.split('\n')]
  records.sort(key=lambda record: record.timestamp)
  records_by_guard_id = get_records_by_guard_id(records)
  return (solution_1(records_by_guard_id), solution_2(records_by_guard_id))
