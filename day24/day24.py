# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/24
author: Martin Javorka
"""

import itertools


class Day24:

    def __init__(self):
        self.components = [list(map(int, line.rstrip().split('/'))) for line in open("input", 'r')]
        self.towers = []

        # init towers
        for component in self.components:
            if component[0] == 0:
                tower = [component]
                self.towers.append(tower)

        for tower in self.towers:
            self.build_towers(tower)

        max_strength = 0
        for tower in self.towers:
            strength = sum(list(itertools.chain.from_iterable(tower)))
            if strength > max_strength:
                max_strength = strength
        print(max_strength)

    def build_towers(self, tower):
        for component in self.components:
            last = tower[-1]
            if component not in tower and (component[0] == last[-1] or component[1] == last[-1]):
                if component[1] == last[-1]:
                    component = list(reversed(component))
                new_tower = tower[:]
                new_tower.append(component)
                self.towers.append(new_tower)


Day24()
