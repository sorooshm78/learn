import numpy as np
from enum import Enum


def up(x, y):
    return x - 1, y


def down(x, y):
    return x + 1, y


def right(x, y):
    return x, y + 1


def left(x, y):
    return x, y - 1


row = 5
col = 5
val = "o"


matrix = np.full((row, col), val)

x = 2
y = 2

matrix[x, y] = "x"
print(matrix)

matrix[up(x, y)] = "u"
print(matrix)

matrix[down(x, y)] = "d"
print(matrix)

matrix[right(x, y)] = "r"
print(matrix)

matrix[left(x, y)] = "l"
print(matrix)
