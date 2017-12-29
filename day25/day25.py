# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/25
author: Martin Javorka
"""


class Day25:

    def __init__(self):
        steps = 12317297
        current = 'A'
        tape = [0] * 12317297
        middle = int(len(tape) / 2)
        #        state if current state 0 elseif current state 1
        states = {'A': [[1, 'right', 'B'], [0, 'left', 'D']],
                  'B': [[1, 'right', 'C'], [0, 'right', 'F']],
                  'C': [[1, 'left', 'C'],  [1, 'left', 'A']],
                  'D': [[0, 'left', 'E'],  [1, 'right', 'A']],
                  'E': [[1, 'left', 'A'],  [0, 'right', 'B']],
                  'F': [[0, 'right', 'C'], [0, 'right', 'E']]}

        for i in range(steps):
            rules = states[current][tape[middle]]
            tape[middle] = rules[0]  # Write the value

            # Move one slot to
            if rules[1] == 'left':
                middle -= 1
            else:
                middle += 1

            current = rules[2]  # Continue with state

        checksum = tape.count(1)
        print(checksum)


Day25()
