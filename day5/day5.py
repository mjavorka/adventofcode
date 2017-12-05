# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/5
autor: Martin Javorka
"""


class Day5part1:

    def __init__(self):
        instruction_list = self.get_instructions()
        self.read_intructions_iter(instruction_list)

    @staticmethod
    def get_instructions():
        instruction_list = list()
        with open("input", 'r') as infile:
            for instruction in infile:
                instruction = instruction.rstrip()
                instruction_list.append(int(instruction))
        return instruction_list

    def read_instructions_recur(self, instruction_list, idx, instruction, steps):

        try:
            instruction_list[idx] += 1
            idx += instruction
            steps += 1
            # print(instruction_list)
            self.read_instructions_recur(instruction_list, idx, instruction_list[idx], steps)
        except IndexError:
            print(steps)

    def read_intructions_iter(self, instruction_list):

        idx = 0
        steps = 0
        try:
            while True:
                # print(instruction_list)
                instruction = instruction_list[idx]
                instruction_list[idx] += 1
                idx += instruction
                steps += 1
        except IndexError:
            print(steps)


class Day5part2:

    def __init__(self):
        instruction_list = Day5part1.get_instructions()
        self.read_intructions(instruction_list)

    def read_intructions(self, instruction_list):
        idx = 0
        steps = 0
        try:
            while True:
                # print(instruction_list)
                instruction = instruction_list[idx]
                if instruction >= 3:
                    instruction_list[idx] -= 1
                else:
                    instruction_list[idx] += 1
                idx += instruction
                steps += 1
        except IndexError:
            print(steps)


Day5part1()
Day5part2()
