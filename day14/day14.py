# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/14
author: Martin Javorka

really really slow: 127.86960887908936 seconds
"""

from itertools import cycle, islice
from scipy.ndimage import label
import numpy as np


class Day10Part2:

    def __init__(self, key_string):
        self.input = key_string
        self.ascii = list()
        self.list_of_numbers = [x for x in range(256)]
        self.to_ascii()
        self.sparse_hash()
        self.dense = list()
        self.dense_hash()

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
        for i in range(16):
            block = self.list_of_numbers[i*16: i*16+16]
            xor = 0
            for value in block:
                xor ^= value
            # print(xor)
            self.dense.append(xor)

    def kh(self):
        knot_hash = ''
        for i in self.dense:
            if len(hex(i)[2:]) == 2:
                knot_hash += hex(i)[2:]
            else:
                knot_hash += '0' + hex(i)[2:]
        return knot_hash


# key_string = 'flqrgnkx-'  # test
key_string = 'jzgqcdpd-'
used = 0
matrix = np.zeros((128, 128), dtype=int)
for i in range(128):
    knot_hash = Day10Part2(key_string + str(i)).kh()
    binary_string = bin(int(knot_hash, 16))[2:].zfill(128)
    used += binary_string.count('1')
    a = np.array(list(binary_string), dtype=int)
    matrix = np.append(matrix, [a], axis=0)

print("part1: " + str(used))
labeled_array, num_features = label(matrix)
print("part2: " + str(num_features))
