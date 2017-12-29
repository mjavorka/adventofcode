# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/22
author: Martin Javorka
"""

import numpy as np


class Direction(object):
    down = 0
    up = 1
    left = 2
    right = 3


class Status(object):
    clean = 0
    infected = 1
    flagged = 2
    weakened = 3


class Day22:

    def __init__(self):

        matrix = np.zeros((0, 1025), dtype=np.int)
        for line in open("input", 'r'):
            a = np.array([1 if x == '#' else 0 for x in line.rstrip()], dtype=int)
            row = np.concatenate((np.zeros(500), a, np.zeros(500)))
            matrix = np.append(matrix, [row], axis=0)

        self.nodes = np.concatenate((np.zeros((500, 1025)), matrix, np.zeros((500, 1025))))

        center = int(self.nodes.shape[0] / 2)
        self.position = [center, center]
        self.d = Direction.up

        self.part2()

    def part1(self):
        infection = 0
        for i in range(10000):
            if self.nodes[self.position[0]][self.position[1]] == 1:
                self.turn_right()
                self.nodes[self.position[0]][self.position[1]] = 0  # clean
            else:
                self.turn_left()
                self.nodes[self.position[0]][self.position[1]] = 1  # infect
                infection += 1

            self.move()
        print(infection)  # 5348

    def part2(self):
        infection = 0
        for i in range(10000000):
            if self.nodes[self.position[0]][self.position[1]] == Status.clean:
                self.turn_left()
                # Clean nodes become weakened
                self.nodes[self.position[0]][self.position[1]] = Status.weakened

            elif self.nodes[self.position[0]][self.position[1]] == Status.infected:
                self.turn_right()
                # Infected nodes become flagged
                self.nodes[self.position[0]][self.position[1]] = Status.flagged

            elif self.nodes[self.position[0]][self.position[1]] == Status.flagged:
                self.reverse()
                # Flagged nodes become clean
                self.nodes[self.position[0]][self.position[1]] = Status.clean

            elif self.nodes[self.position[0]][self.position[1]] == Status.weakened:
                # Weakened nodes become infected
                self.nodes[self.position[0]][self.position[1]] = Status.infected
                infection += 1

            self.move()
        print(infection)  # 2512225
        return

    def move(self):
        if self.d == Direction.up:
            self.position[0] -= 1
        elif self.d == Direction.down:
            self.position[0] += 1
        elif self.d == Direction.left:
            self.position[1] -= 1
        elif self.d == Direction.right:
            self.position[1] += 1

    def turn_right(self):
        if self.d == Direction.up:
            self.d = Direction.right
        elif self.d == Direction.right:
            self.d = Direction.down
        elif self.d == Direction.down:
            self.d = Direction.left
        elif self.d == Direction.left:
            self.d = Direction.up

    def turn_left(self):
        if self.d == Direction.up:
            self.d = Direction.left
        elif self.d == Direction.left:
            self.d = Direction.down
        elif self.d == Direction.down:
            self.d = Direction.right
        elif self.d == Direction.right:
            self.d = Direction.up

    def reverse(self):
        if self.d == Direction.up:
            self.d = Direction.down
        elif self.d == Direction.down:
            self.d = Direction.up
        elif self.d == Direction.left:
            self.d = Direction.right
        elif self.d == Direction.right:
            self.d = Direction.left


Day22()
