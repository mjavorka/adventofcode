# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/10
author: Martin Javorka
"""

from itertools import cycle, islice


class Day10Part1:

    def __init__(self):
        self.list_of_numbers = [x for x in range(256)]
        self.lengths = list()  # input
        self.read_file()
        self.part1()

    def read_file(self):
        self.lengths = list(map(int, open("input", 'r').readline().split(',')))

    def part1(self):
        skip_size = 0
        current_position = 0
        for length in self.lengths:
            sublist = list(islice(cycle(self.list_of_numbers), current_position, current_position + length))
            sublist.reverse()
            self.return_sublist(sublist, current_position)
            current_position = current_position + length + skip_size
            skip_size += 1
        print("part1 result = " + str(self.list_of_numbers[0] * self.list_of_numbers[1]))

    def return_sublist(self, sublist, current_position):
        real_current_position = current_position % len(self.list_of_numbers)
        while sublist:
            self.list_of_numbers[real_current_position] = sublist.pop(0)
            real_current_position = (real_current_position + 1) % len(self.list_of_numbers)


class Day10Part2:

    def __init__(self):
        self.input = list()
        self.ascii = list()
        self.list_of_numbers = [x for x in range(256)]
        self.read_file()
        self.to_ascii()
        self.sparse_hash()
        dense = self.dense_hash()
        print("Part 2: " + self.kh(dense))

    def read_file(self):
        self.input = open("input", 'r').readline().rstrip()

    def to_ascii(self):
        for char in self.input:
            ascii_val = ord(char)
            self.ascii.append(ascii_val)
        self.ascii = self.ascii + [17, 31, 73, 47, 23]  # input combined with the standard length suffix values

    def sparse_hash(self):
        position = 0
        skip = 0
        for i in range(64):  # 64 rounds
            for length in self.ascii:
                sublist = list(islice(cycle(self.list_of_numbers), position, position + length))
                sublist.reverse()
                self.return_sublist(sublist, position)
                position = position + length + skip
                skip += 1

    def return_sublist(self, sublist, current_position):
        real_current_position = current_position % len(self.list_of_numbers)
        while sublist:
            self.list_of_numbers[real_current_position] = sublist.pop(0)
            real_current_position = (real_current_position + 1) % len(self.list_of_numbers)

    def dense_hash(self):
        numbers = list()
        for i in range(16):
            block = self.list_of_numbers[i*16: i*16+16]
            xor = 0
            for value in block:
                xor ^= value
            # print(xor)
            numbers.append(xor)
        return numbers

    def kh(self, dense):
        knot_hash = ''
        for i in dense:
            if len(hex(i)[2:]) == 2:
                knot_hash += hex(i)[2:]
            else:
                knot_hash += '0' + hex(i)[2:]
        return knot_hash


# Day10Part1()
Day10Part2()
