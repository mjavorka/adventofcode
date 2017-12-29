# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/20
author: Martin Javorka
"""


class Day20:

    def __init__(self):
        data = [line.rstrip().split(', ') for line in open("input", 'r')]
        self.particles = []
        for row in data:
            position = list(map(int, row[0].strip('p=<>').split(',')))
            velocity = list(map(int, row[1].strip('v=<>').split(',')))
            acceleration = list(map(int, row[2].strip('a=<>').split(',')))
            self.particles.append([position, velocity, acceleration])

        positions = [x for x in range(len(self.particles))]
        for i in range(2000):
            for x, particle in enumerate(self.particles):
                particle[1][0] += particle[2][0]  # Increase the X velocity by the X acceleration.
                particle[1][1] += particle[2][1]  # Increase the Y velocity by the Y acceleration.
                particle[1][2] += particle[2][2]  # Increase the Z velocity by the Z acceleration.

                particle[0][0] += particle[1][0]  # Increase the X position by the X velocity.
                particle[0][1] += particle[1][1]  # Increase the Y position by the Y velocity.
                particle[0][2] += particle[1][2]  # Increase the Z position by the Z velocity.
                # distance = abs(particle[0][0]) + abs(particle[0][1]) + abs(particle[0][2])
                positions[x] = particle[0]

            duplicates = self.get_duplicates(positions)
            positions = self.remove_duplicates(positions, duplicates)

        # print(distances.index(min(distances)))
        print(len(self.particles))

    @staticmethod
    def get_duplicates(list_):
        new = list()
        for item in list_:
            if list_.count(item) > 1 and item not in new:
                new.append(item)
        return new

    def remove_duplicates(self, list_, duplicates):
        for dupl in duplicates:
            while dupl in list_:
                idx = list_.index(dupl)
                list_.pop(idx)
                self.particles.pop(idx)
        return list_


Day20()
