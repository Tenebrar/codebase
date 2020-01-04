from typing import List

from numpy import zeros

from advent_of_code.util import input_file


class ChangingValue:
    def __init__(self):
        self.min = 0
        self.value = 0
        self.max = 0

    def change(self, value):
        self.value += value
        self.max = max(self.value, self.max)
        self.min = min(self.value, self.min)

    def reset_value(self):
        self.value = 0


def check_grid(wire1: List[str], wire2: List[str]) -> None:
    x = ChangingValue()
    y = ChangingValue()

    for d in wire1:
        if d[0] == 'R':
            x.change(int(d[1:]))
        elif d[0] == 'L':
            x.change(-int(d[1:]))
        elif d[0] == 'U':
            y.change(int(d[1:]))
        elif d[0] == 'D':
            y.change(-int(d[1:]))
        else:
            raise Exception()

    x.reset_value()
    y.reset_value()

    for d in wire2:
        if d[0] == 'R':
            x.change(int(d[1:]))
        elif d[0] == 'L':
            x.change(-int(d[1:]))
        elif d[0] == 'U':
            y.change(int(d[1:]))
        elif d[0] == 'D':
            y.change(-int(d[1:]))
        else:
            raise Exception()

    grid = zeros((-x.min + 1 + x.max, -y.min + 1 + y.max), dtype=int)
    dist_grid1 = zeros((-x.min + 1 + x.max, -y.min + 1 + y.max), dtype=int)
    dist_grid2 = zeros((-x.min + 1 + x.max, -y.min + 1 + y.max), dtype=int)

    current_x = -x.min
    current_y = -y.min
    dist = 1

    grid[current_x][current_y] = -1

    for d in wire1:
        if d[0] == 'R':
            dir = (1, 0)
        elif d[0] == 'L':
            dir = (-1, 0)
        elif d[0] == 'U':
            dir = (0, 1)
        elif d[0] == 'D':
            dir = (0, -1)
        else:
            raise Exception()

        val = int(d[1:])

        for i in range(1, val + 1):
            if grid[current_x + dir[0] * i][current_y + dir[1] * i] == 0:
                grid[current_x + dir[0]*i][current_y + dir[1]*i] = 1
            if dist_grid1[current_x + dir[0] * i][current_y + dir[1] * i] == 0:
                dist_grid1[current_x + dir[0] * i][current_y + dir[1] * i] = dist
            dist += 1

        current_x += dir[0] * val
        current_y += dir[1] * val

    current_x = -x.min
    current_y = -y.min
    dist = 1

    for d in wire2:
        if d[0] == 'R':
            dir = (1, 0)
        elif d[0] == 'L':
            dir = (-1, 0)
        elif d[0] == 'U':
            dir = (0, 1)
        elif d[0] == 'D':
            dir = (0, -1)
        else:
            raise Exception()

        val = int(d[1:])

        for i in range(1, val + 1):
            if grid[current_x + dir[0]*i][current_y + dir[1]*i] == 0:
                grid[current_x + dir[0] * i][current_y + dir[1] * i] = 2
            elif grid[current_x + dir[0] * i][current_y + dir[1] * i] == 1:
                grid[current_x + dir[0] * i][current_y + dir[1] * i] = 3

            if dist_grid2[current_x + dir[0] * i][current_y + dir[1] * i] == 0:
                dist_grid2[current_x + dir[0] * i][current_y + dir[1] * i] = dist
            dist += 1

        current_x += dir[0] * val
        current_y += dir[1] * val

    min_dist = 100000000
    for _x in range(len(grid)):
        for _y in range(len(grid[0])):
            if grid[_x][_y] == 3:
                dist = dist_grid1[_x][_y] + dist_grid2[_x][_y]
                if dist < min_dist:
                    min_dist = dist

    print(min_dist)


check_grid('R8,U5,L5,D3'.split(','), 'U7,R6,D4,L4'.split(','))
check_grid('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','), 'U62,R66,U55,R34,D71,R55,D58,R83'.split(','))
check_grid('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','), 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))

with input_file() as file:
    wire1 = file.readline().split(',')
    wire2 = file.readline().split(',')

check_grid(wire1, wire2)
