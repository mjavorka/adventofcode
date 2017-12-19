# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/15
author: Martin Javorka
"""

import time


class Day15:
    """
        42.9593939781189 seconds
    """
    @staticmethod
    def part1(gen_a=116, gen_b=299):
        pairs = 0
        for i in range(40000000):
            gen_a = gen_a * 16807 % 2147483647
            gen_b = gen_b * 48271 % 2147483647
            if bin(gen_a)[-16:] == bin(gen_b)[-16:]:
                pairs += 1

        print("Part1: " + str(pairs))

    @staticmethod
    def part2(gen_a=116, gen_b=299):
        a_values = []
        b_values = []
        b_count = 0
        while b_count <= 5000000:
            gen_a = gen_a * 16807 % 2147483647
            gen_b = gen_b * 48271 % 2147483647

            if gen_a % 4 == 0:
                a_values.append(gen_a)
            if gen_b % 8 == 0:
                b_values.append(gen_b)
                b_count += 1

        pairs = 0
        for x in range(len(b_values)):
            gen_a = a_values[x]
            gen_b = b_values[x]

            if bin(gen_a)[-16:] == bin(gen_b)[-16:]:
                pairs += 1

        print("Part2: " + str(pairs))


start_time = time.time()
Day15().part1()
print("--- %s seconds ---" % (time.time() - start_time))
# Day15().part2()
# Day15().part2(65, 8921)  # testing

