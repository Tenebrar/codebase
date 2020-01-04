from datetime import datetime
from numpy import zeros, argmax
from re import search
from typing import Tuple

from advent_of_code.util import input_file


def parse_event(string: str) -> Tuple[datetime, str]:
    match = search('^\[(.*)\] (.*)\n$', string)
    return datetime.strptime(match.group(1), '%Y-%m-%d %H:%M'), match.group(2)


with input_file() as file:
    events = sorted([parse_event(line) for line in file])

current_guard = None
sleep_minute = None

sleep_schedule = {}
for time, event in events:
    match = search('^Guard #(\d*) begins shift$', event)
    if match:
        current_guard = int(match.group(1))
        if current_guard not in sleep_schedule:
            sleep_schedule[current_guard] = zeros(60, dtype=int)
    elif event == 'falls asleep':
        sleep_minute = time.minute
    else:
        awake_minute = time.minute
        for i in range(sleep_minute, awake_minute):
            sleep_schedule[current_guard][i] += 1

guard, schedule = sorted(sleep_schedule.items(), key=lambda schedule: max(schedule[1]), reverse=True)[0]
minute = argmax(schedule)

print(guard * minute)
