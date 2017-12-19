# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/17
author: Martin Javorka
"""


class Day17:

    @staticmethod
    def part1():
        position = 0
        spinlock = [0]
        steps = 355
        for x in range(1, 2018):
            idx = ((position + steps) % len(spinlock)) + 1
            if idx >= len(spinlock):
                spinlock = spinlock + [x]
            else:
                spinlock = spinlock[:idx] + [x] + spinlock[idx:]
            position = spinlock.index(x)

        find = spinlock.index(2017)
        print(spinlock[find + 1])

    @staticmethod
    def part2():
        idx = 0
        n = 0
        steps = 355
        for i in range(1, 50000001):
            idx = (idx + steps) % i
            if idx == 0:
                n = i
            idx += 1
        print(n)


# Day17().part1()
Day17().part2()


