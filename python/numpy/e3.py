import numpy as np
import random


row = 10
col = 10
empty = "o"
ship = "x"

matrix = np.full((row, col), empty)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


def random_point():
    while True:
        x = random.randrange(row)
        y = random.randrange(col)
        return Point(x, y)
        if matrix[x, y] == empty:
            return Point(x, y)


def slice_with_direct(point, count, direction):
    if direction == "up":
        return Point(slice(point.x - count + 1, point.x + 1), point.y)

    if direction == "down":
        return Point(slice(point.x, point.x + count), point.y)

    if direction == "right":
        return Point(point.x, slice(point.y, point.y + count))

    if direction == "left":
        return Point(point.x, slice(point.y - count + 1, point.y + 1))


def make_shape(count, shape):
    while True:
        point = random_point()
        print(point)
        directs = np.array(["up", "down", "right", "left"])
        random.shuffle(directs)
        for direct in directs:
            print(direct)
            p = slice_with_direct(point, count, direct)
            if len(matrix[p.x, p.y]) == count:
                if shape not in matrix[p.x, p.y]:
                    matrix[p.x, p.y] = shape
                    return


make_shape(4, ship)
make_shape(4, ship)
make_shape(4, ship)
make_shape(4, ship)
print(matrix)
