import numpy as np
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


row = 10
col = 10
empty = "o"
ship = "x"


matrix = np.arange(100).reshape(row, col)


point = Point(slice(0, 2), slice(0, 1))
print(matrix[point.x, point.y])

point = Point(
    slice(max(0, point.x.start - 1), max(0, point.x.stop + 1)),
    slice(max(0, point.y.start - 1), max(0, point.y.stop + 1)),
)

print(matrix[point.x, point.y])
print(matrix)
