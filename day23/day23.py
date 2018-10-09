# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/23
author: Martin Javorka
"""


class Day23:

    def __init__(self):
        self.registers = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'g': 0, 'h': 0}
        self.instructions = [line.rstrip().split(' ') for line in open("input", 'r')]
        self.mul_count = 0

        # self.process()

    @staticmethod
    def part2():
        h = 0
        for x in range(108100, 125100 + 1, 17):
            for i in range(2, x):
                if x % i == 0:
                    h += 1
                    break
        print(h)

    def process(self):
        i = 0
        while 0 <= i < len(self.instructions) - 1:
            instruction = self.instructions[i]

            if instruction[0] == 'set':
                if instruction[2].lstrip("-").isdigit():
                    self.registers[instruction[1]] = int(instruction[2])
                else:
                    self.registers[instruction[1]] = self.registers[instruction[2]]

            if instruction[0] == 'sub':
                if instruction[2].lstrip("-").isdigit():
                    self.registers[instruction[1]] -= int(instruction[2])
                else:
                    self.registers[instruction[1]] -= self.registers[instruction[2]]

            if instruction[0] == 'mul':
                self.mul_count += 1
                if instruction[2].lstrip("-").isdigit():
                    self.registers[instruction[1]] *= int(instruction[2])
                else:
                    self.registers[instruction[1]] *= self.registers[instruction[2]]

            if instruction[0] == 'jnz':
                if instruction[1].lstrip("-").isdigit():
                    value = int(instruction[1])
                else:
                    value = self.registers[instruction[1]]
                if value != 0:
                    i += int(instruction[2])
                    continue
            i += 1


Day23()
