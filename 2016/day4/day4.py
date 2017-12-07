# !/usr/bin/python3

"""
http://adventofcode.com/2016/day/4
autor: Martin Javorka
"""

from string import ascii_lowercase


class Day4:

    def __init__(self):
        self.decoys = list()
        self.read_file()
        # self.part1()
        self.part2()

    def read_file(self):
        with open("input", 'r') as file:
            self.decoys = [decoy.rstrip().split('-') for decoy in file]

    def part1(self):
        sum_ = 0
        for decoy in self.decoys:
            sector_id, checksum = decoy[-1].strip(']').split('[')
            encrypted_name = ''.join(decoy[:-1])
            my_checksum = self.make_checksum(encrypted_name)
            if my_checksum == checksum:
                sum_ += int(sector_id)
        print(sum_)

    @staticmethod
    def make_checksum(name):
        char_list = list()
        for char in name:
            if [char, name.count(char)] not in char_list:
                char_list.append([char, name.count(char)])

        # my poor bad solution :D (of course not working)
        # checksum_list = sorted(char_list, key=itemgetter(1, 0), reverse=True)
        checksum_list = sorted(char_list, key=lambda x: (-x[1], x[0]))
        return ''.join([check[0] for check in checksum_list[:5]])

    def part2(self):
        for decoy in self.decoys:
            sector_id, checksum = decoy[-1].strip(']').split('[')
            encrypted_name = ' '.join(decoy[:-1])
            self.decrypt_name(encrypted_name, sector_id)

    @staticmethod
    def decrypt_name(name, sector_id):

        alphabet = [char for char in ascii_lowercase]
        decrypted = ''
        for char in name:
            if char == ' ':
                decrypted += ' '
            else:
                idx = (int(sector_id) + alphabet.index(char)) % len(alphabet)
                decrypted += alphabet[idx]
        print(decrypted)
        print(sector_id)


Day4()
