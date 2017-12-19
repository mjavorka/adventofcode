# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/12
author: Martin Javorka
"""


class Day12:

    def __init__(self):
        self.input = list()
        self.parsed = dict()
        self.seen = list()
        self.count = 1
        self.read_file()
        self.parse_input()

        # self.part1()
        self.find_groups()

    def part1(self):
        self.walk_through(0)  # we are looking for 0
        print("Part1: " + str(self.count))

    def read_file(self):
        with open("input", 'r') as file:
            self.input = [line.rstrip().split('<->') for line in file]

    def parse_input(self):
        for value in self.input:
            prog_id = int(value[0].replace(' ', ''))
            self.parsed[prog_id] = [int(x.replace(' ', '')) for x in value[1].split(',')]

    def walk_through(self, looking_for):
        self.seen.append(looking_for)
        for connected in self.parsed[looking_for]:
            if connected not in self.seen:
                self.count += 1
                self.walk_through(connected)

    def find_groups(self):
        programs = [item for item in list(self.parsed.keys()) if item not in self.seen]
        groups = 0
        while programs:
            groups += 1
            self.walk_through(programs[0])
            programs = [item for item in list(self.parsed.keys()) if item not in self.seen]
        print("Part2: " + str(groups))


Day12()
