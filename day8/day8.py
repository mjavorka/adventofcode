# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/8
autor: Martin Javorka
"""


class Day8:

    def __init__(self):
        self.input = list()
        self.registers = list()
        self.max = 0
        self.read_file()
        self.init_registers()
        self.part1()

    def read_file(self):
        with open("input", 'r') as file:
            self.input = [line.split(' ') for line in file]

    def init_registers(self):
        for line in self.input:
            if [line[0], 0] not in self.registers:
                self.registers.append([line[0], 0])
            if [line[4], 0] not in self.registers:
                self.registers.append([line[4], 0])

    def get_register_value(self, register):
        for reg in self.registers:
            if reg[0] == register:
                return reg[1]
        return 0

    def get_largest_value(self):
        maximum = self.registers[0][1]
        for reg in self.registers:
            if reg[1] > maximum:
                maximum = reg[1]
        print("maximum at the end:")
        print(maximum)

    def evaluate_condition(self, line):
        if line[5] == '>':
            return self.get_register_value(line[4]) > int(line[6])
        if line[5] == '<':
            return self.get_register_value(line[4]) < int(line[6])
        if line[5] == '>=':
            return self.get_register_value(line[4]) >= int(line[6])
        if line[5] == '<=':
            return self.get_register_value(line[4]) <= int(line[6])
        if line[5] == '==':
            return self.get_register_value(line[4]) == int(line[6])
        if line[5] == '!=':
            return self.get_register_value(line[4]) != int(line[6])
        return False

    def update_value(self, line):
        for idx, reg in enumerate(self.registers):
            if reg[0] == line[0]:
                if line[1] == 'inc':
                    new_value = reg[1] + int(line[2])
                    self.registers[idx] = [reg[0], new_value]
                    if new_value > self.max:
                        self.max = new_value
                if line[1] == 'dec':
                    new_value = reg[1] - int(line[2])
                    self.registers[idx] = [reg[0], new_value]
                    if new_value > self.max:
                        self.max = new_value
        return

    def part1(self):
        for line in self.input:
            if self.evaluate_condition(line):
                self.update_value(line)
        self.get_largest_value()
        print('highest value during process')
        print(self.max)


Day8()
