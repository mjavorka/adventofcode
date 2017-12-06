# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/5
autor: Martin Javorka
"""

import copy


class Day6:

    def __init__(self):
        self.banks = list()
        self.read_file()
        self.exec()

    def read_file(self):
        with open("input", 'r') as infile:
            for banks in infile:
                banks_list = banks.split("\t")
                self.banks = list(map(int, banks_list))
                return

    def exec(self):
        seen = list()
        seen.append(copy.copy(self.banks))
        steps = 1
        while True:
            for idx, bank in enumerate(self.banks):
                max_banks = max(self.banks)
                if idx == self.banks.index(max_banks):
                    self.banks[idx] -= max_banks
                    self.redistribute(max_banks, idx)
                    break

            if self.banks in seen:
                print(steps)  # part1
                print(steps - seen.index(self.banks))  # part2
                return
            seen.append(copy.copy(self.banks))
            steps += 1

    def redistribute(self, amount, idx):
        while amount > 0:
            if idx < len(self.banks) - 1:
                idx += 1
            else:
                idx = 0
            self.banks[idx] += 1
            amount -= 1
        return self.banks


Day6()
