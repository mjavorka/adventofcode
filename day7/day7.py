# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/7
autor: Martin Javorka
"""


class Day7:

    def __init__(self):
        self.input = list()
        self.programs = list()
        self.names = list()
        self.above = list()
        self.towers = list()
        self.top = ''
        self.read_file()
        self.part1()
        self.part2()

    def read_file(self):
        with open("input", 'r') as infile:
            for program in infile:
                program = program.rstrip()
                self.input.append(program)

    def check_top(self, name):
        for program in self.input:
            if '->' not in program:
                n, w = program.replace(')', '').split('(')
                if name == n.strip():
                    return True
                else:
                    continue
        return False

    def parse_program(self, part1=True):
        for program in self.input:
            try:
                name, programs_above = program.split('->')
                if part1:
                    self.parse_programs_above(programs_above)
                    self.parse_name_part1(name)
                else:
                    self.parse_name(name)
                    self.create_tower(name, programs_above)
            except ValueError:
                if not part1:
                    self.parse_name(program)
                continue

    def part1(self):
        self.parse_program()
        for prog in self.names:
            if prog not in self.above:
                self.top = prog
                return

    def part2(self):
        self.parse_program(False)
        self.check_weights(self.top)

    def parse_name(self, name):
        name, weight = name.replace(')', '').split('(')
        self.programs.append([name.strip(), int(weight)])

    def parse_name_part1(self, name):
        name, weight = name.replace(')', '').split('(')
        self.names.append(name.strip())

    def parse_programs_above(self, programs):
        for program in programs.split(','):
            self.above.append(program.strip())

    def create_tower(self, name, programs):
        name, weight = name.replace(' ', '').split('(')
        above = programs.replace(' ', '').split(',')
        self.towers.append([name, above])

    def return_weight(self, program):
        for prog in self.programs:
            if program == prog[0]:
                return int(prog[1])

    def check_weights(self, top):
        for tower in self.towers:
            weight = self.return_weight(tower[0])
            weights = list()
            if tower[0] == top:
                for program in tower[1]:
                    weights.append(self.check_weights(program))
                if self.check_equal(weights):
                    return weight + sum(weights)
                else:
                    idx = self.get_idx(weights)
                    print(weights)
                    print(tower[1][idx])
                    exit()

        return self.return_weight(top)

    @staticmethod
    def check_equal(lst):
        return lst[1:] == lst[:-1]

    @staticmethod
    def get_idx(lst):
        idx = 0
        while lst.count(lst[idx]) != 1:
            idx += 1
        return idx


Day7()
