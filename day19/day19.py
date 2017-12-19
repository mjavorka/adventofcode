# !/usr/bin/python3

"""
http://adventofcode.com/2017/day/19
author: Martin Javorka

RYLONKE

W
B
"""


class Day19:

    def __init__(self):
        path = [line.rstrip() for line in open("input", 'r')]
        width = self.get_width(path)
        count = 0
        x = 0
        y = 0
        message = ''
        direction = 0  # 0=down, 1=up, 2=left, 3=right
        while 0 <= y < len(path):
            path[y] = path[y].ljust(width + 1)
            line = path[y]
            while 0 <= x <= width:
                char = line[x]

                if char == "|":
                    count += 1
                    print(char, y, x)
                    if direction == 0 or direction == 1:
                        break
                elif char == "+":
                    count += 1
                    print(char, y, x)
                    if self.index_exists(line, x + 1) and line[x + 1] != ' ' and direction != 2:
                        print("go right", message)
                        x += 1
                        direction = 3
                    elif self.index_exists(line, x - 1) and line[x - 1] != ' ' and direction != 3:
                        print("go left", message)
                        x -= 1
                        direction = 2
                    elif self.index_exists(path, y - 1) and path[y - 1][x] != ' ':
                        print("go up", message)
                        direction = 1
                        break
                    elif path[y + 1][x] != ' ':
                        print("go down", message)
                        direction = 0
                        break
                    continue
                elif char == "-":
                    count += 1
                    print(char, y, x)
                    if direction == 2:
                        x -= 1
                        continue
                    elif direction == 3:
                        x += 1
                        continue
                    elif direction == 0:
                        break
                    elif direction == 1:
                        break

                elif char.isalpha():
                    count += 1
                    message += char
                    if char == "B":
                        print(message)
                        print(count)
                        return
                    if direction == 3:
                        x += 1
                        continue
                    elif direction == 2:
                        x -= 1
                        continue
                    break

                if direction == 2:
                    x -= 1
                else:
                    x += 1

            if direction == 1:
                y -= 1
            else:
                y += 1

        print(message)
        print(count)

    @staticmethod
    def get_width(path):
        width = 0
        for line in path:
            if len(line) > width:
                width = len(line)

        return width - 1

    @staticmethod
    def index_exists(ls, i):
        return 0 <= i < len(ls)


Day19()
