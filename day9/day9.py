# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/9
autor: Martin Javorka
"""


class Day9:

    def __init__(self):
        self.input = list()
        self.registers = list()
        self.max = 0
        self.read_file()
        self.parse_input()

    def read_file(self):
        with open("input", 'r') as file:
            for blah in file:
                self.input = blah

    def parse_input(self):
        score = 0
        garbage_open = False
        ignore_next = False
        level = 0
        garbage_chars = 0
        reader = ''
        for char in self.input:
            reader += char
            if ignore_next:
                ignore_next = False
                continue
            if char == '!':
                ignore_next = True
            if garbage_open:
                if char == '>':
                    garbage_open = False
                if char != '!' and char != '>':
                    garbage_chars += 1
                continue
            if char == '{':
                level += 1
            elif char == '}':
                score += level
                level -= 1
            elif char == ',':
                continue
            elif char == '<':
                garbage_open = True
        print(garbage_chars)


Day9()
