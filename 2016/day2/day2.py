# !/usr/bin/python3

"""
http://adventofcode.com/2016/day/2
autor: Martin Javorka
"""


class Day2:

    def __init__(self):
        self.y = 1
        self.x = 1
        self.keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.keypad2 = [['', '', 1, '', ''],
                        ['', 2, 3, 4, ''],
                        [5, 6, 7, 8, 9],
                        ['', 'A', 'B', 'C',  ''],
                        ['', '', 'D', '', '']]
        # self.part1()
        self.part2()

    def part1(self):
        # starting coordinates
        self.y = 1
        self.x = 1
        with open("input", 'r') as infile:
            for instructions in infile:
                instructions = instructions.rstrip()
                self.read_instructions(instructions)

    def part2(self):
        # starting coordinates
        self.x = 2
        self.y = 0
        with open("input", 'r') as infile:
            for instructions in infile:
                instructions = instructions.rstrip()
                self.read_instructions2(instructions)

    def read_instructions(self, instructions):
        for instruction in instructions:
            self.move(instruction)
            if self.x < 0 or self.x > 2 or self.y < 0 or self.y > 2:
                self.move_back(instruction)

        print(self.keypad[self.x][self.y])

    def read_instructions2(self, instructions):
        for instruction in instructions:
            self.move(instruction)
            if self.x < 0 or self.x > 4 or self.y < 0 or self.y > 4 or self.keypad2[self.x][self.y] == '':
                self.move_back(instruction)

        print(self.keypad2[self.x][self.y])
        # print('________________')

    def move(self, instruction):
        if instruction == "U":    # up
            self.x -= 1
        elif instruction == "D":  # down
            self.x += 1
        elif instruction == "L":  # left
            self.y -= 1
        elif instruction == "R":  # right
            self.y += 1

    def move_back(self, instruction):
        if instruction == "U":
            self.x += 1
        elif instruction == "D":
            self.x -= 1
        elif instruction == "L":
            self.y += 1
        elif instruction == "R":
            self.y -= 1


Day2()
