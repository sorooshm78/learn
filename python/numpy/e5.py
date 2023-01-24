import numpy as np
import random


class Cell:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def is_empty(self):
        return False


# arr = np.full((3, 3), Cell(), dtype=object)

# arr[0, 0].x = 5
# arr[0, 0].y = 5

# print(arr[0, 0])
# print(arr[0, 1])
# print(arr[0, 2])
# print(arr)


arr = np.empty((3, 3), dtype=object)

for y, x in np.ndindex(arr.shape):
    arr[y, x] = Cell()

print(arr)

print("*********")

c = Cell(10, 10)
arr[0, 0:3] = Cell(10, 10)

print(arr)
