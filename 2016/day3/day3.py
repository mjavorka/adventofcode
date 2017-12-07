# !/usr/bin/python3

"""
http://adventofcode.com/2016/day/3
autor: Martin Javorka
"""


class Day3:

    def __init__(self):
        self.triangles = list()
        self.read_file()
        self.part1()

    def read_file(self):
        with open("input", 'r') as file:
            for triangle in file:
                triangle_list = triangle.split(",")
                triangle_list[0] = triangle_list[0].rstrip()
                triangle_list[1] = triangle_list[1].rstrip()
                triangle_list[2] = triangle_list[2].rstrip()
                triangle_list = list(map(int, triangle_list))
                self.triangles.append(triangle_list)

    def part1(self):
        count = 0
        for triangle in self.triangles:
            if self.check_valid_triangle(triangle):
                count += 1
        print(count)

    @staticmethod
    def check_valid_triangle(triangle):
        for side in triangle:
            other_sides = (sum(triangle) - side)
            if side > other_sides:
                return False
            elif side == other_sides:
                # print('Degenerated')
                return False
        else:
            return True


Day3()
