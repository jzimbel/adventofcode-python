'''
Test for year 2018, day 4 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from datetime import datetime
from adventofcode.solutions.y2018.d04 import get_record, get_records_by_guard_id, run

data = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''

def test_get_record() -> None:
  assert get_record(data.split('\n')[0]) == (datetime.fromisoformat('1518-11-01 00:00'), 'Guard #10 begins shift')

def test_get_records_by_guard_id() -> None:
  records = [get_record(line) for line in data.split('\n')]
  expected = {
    10: [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
    99: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,3,2,2,2,2,1,1,1,1,1,0,0,0,0,0]
  }
  assert get_records_by_guard_id(records) == expected

def test_run() -> None:
  # not yet implemented!
  assert run(data) == (240, 4455)
