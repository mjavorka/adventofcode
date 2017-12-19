# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/10
author: Martin Javorka

Used axial coordinates:

        NW|N |
        --+--+--
        SW|  |NE
        --+--+--
          |S |SE

Distance from the center is just (abs(x) + abs(y) + abs(x+y)) / 2

TODO Study hexagonal grids: https://www.redblobgames.com/grids/hexagons/
"""


class Day11:

    def __init__(self):
        self.directions = list()  # input
        self.read_file()
        self.distance()

    def read_file(self):
        self.directions = open("input", 'r').readline().split(',')

    def distance(self):
        x = 0
        y = 0
        max_distance = 0
        dist = 0
        for direction in self.directions:
            if direction == 'n':
                y += 1
            elif direction == 'ne':
                x += 1
            elif direction == 'se':
                x += 1
                y -= 1
            elif direction == 's':
                y -= 1
            elif direction == 'sw':
                x -= 1
            elif direction == 'nw':
                x -= 1
                y += 1
            dist = int((abs(x) + abs(y) + abs(x + y)) / 2)
            if max_distance < dist:
                max_distance = dist
        print("distance: " + str(dist))  # part1
        print("max distance: " + str(max_distance))  # part2


Day11()
