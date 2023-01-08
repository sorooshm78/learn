import numpy as np
import random


def up(x, y):
    return x - 1, y


def down(x, y):
    return x + 1, y


def right(x, y):
    return x, y + 1


def left(x, y):
    return x, y - 1


def make_shape(matrix, count, shape):
    pass


row = 5
col = 5
val = "o"


matrix = np.full((row, col), val)

x = 2
y = 2

matrix[x, y] = "x"

# print(matrix)

matrix[up(x, y)] = "u"
matrix[down(x, y)] = "d"
matrix[right(x, y)] = "r"
matrix[left(x, y)] = "l"

print(matrix)


def random_point():
    while True:
        x = random.randrange(row)
        y = random.randrange(col)
        print(x, y)
        if matrix[x, y] == "o":
            return x, y


point = random_point()
print(point)
