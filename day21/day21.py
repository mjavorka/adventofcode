# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/21
author: Martin Javorka
"""

import numpy as np


class Day21:

    def __init__(self):
        init = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
        self.rules2 = []
        self.rules3 = []
        self.parse_rules()
        self.draw(init, 18)

    def draw(self, init, steps):
        image = init
        for i in range(steps):
            print(i)
            if image.shape[0] == 3:
                image = self.find_rule(image)
            else:
                if image.shape[0] % 2 == 0:
                    splited = self.split_image(image)
                else:
                    splited = self.split_image(image, divisible=3)
                new = self.update_image(splited)
                image = self.merge_image(new)
            # print(image)

        unique, counts = np.unique(image, return_counts=True)
        values = dict(zip(unique, counts))
        print('part1: ', values[1])

    def update_image(self, images):
        new_image = []
        for row in images:
            new_row = []
            for image in row:
                new_row.append(self.find_rule(image))
            new_image.append(new_row)
        return new_image
        # print(new_image)

    @staticmethod
    def merge_image(images):
        merged_rows = []
        for row in images:
            merged_rows.append(np.concatenate(row, axis=1))  # join columns in row together
        merged_image = np.concatenate(merged_rows)  # join all rows together
        return merged_image

    @staticmethod
    def split_image(image, divisible=2):
        split_val = int(image.shape[0] / divisible)
        new_image = []
        for x in range(split_val):
            new_image.append(np.hsplit(np.vsplit(image, split_val)[x], split_val))
        # print(new_image)
        return new_image

    def parse_rules(self):
        data = [line.rstrip().split(' => ') for line in open("input", 'r')]
        for left, right in data:
            pre = np.array([1 if c == "#" else 0 for c in left.replace("/", "")])
            post = np.array([1 if c == "#" else 0 for c in right.replace("/", "")])
            if len(pre) == 4:
                self.rules2.append([pre.reshape((2, 2)), post.reshape((3, 3))])
            elif len(pre) == 9:
                self.rules3.append([pre.reshape((3, 3)), post.reshape((4, 4))])

    @staticmethod
    def all_flips_rotations(m):
        possibilities = []
        for k in range(4):
            rot = np.rot90(m, k=k)
            possibilities.append(rot)
            possibilities.append(np.fliplr(rot))
            possibilities.append(np.flipud(rot))
        return possibilities

    def find_rule(self, m):
        possibilities = self.all_flips_rotations(m)
        for option in possibilities:
            if m.shape[0] == 2:
                for rule in self.rules2:
                    if np.array_equal(option, rule[0]):
                        return rule[1]
            else:
                for rule in self.rules3:
                    if np.array_equal(option, rule[0]):
                        return rule[1]


Day21()
