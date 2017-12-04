# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/4
autor: Martin Javorka
"""


class Day4:

    def part1(self):
        num_valid = 0
        with open("input", 'r') as infile:
            for line in infile:
                words = self.get_words(line)
                if self.read_words(words):
                    num_valid += 1
        print(num_valid)

    def get_words(self, line):
        words = line.split(' ')
        return words

    def read_words(self, words):
        used_words = list()
        for word in words:
            word = word.rstrip()
            if word not in used_words:
                used_words.append(word)
            else:
                return False
        return True

    def read_words2(self, words):
        used_combinations = list()
        for word in words:
            word = word.rstrip()
            chars = list()
            for char in word:
                chars.append(char)
            sorted_word = ''.join(sorted(chars))
            if sorted_word not in used_combinations:
                used_combinations.append(sorted_word)
            else:
                return False
        return True

    def part2(self):
        num_valid = 0
        with open("input", 'r') as infile:
            for line in infile:
                words = self.get_words(line)
                if self.read_words2(words):
                    num_valid += 1
        print(num_valid)


day4 = Day4()
day4.part1()
day4.part2()

