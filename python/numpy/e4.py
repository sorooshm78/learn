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


def get_list_of_point(points):
    list_point = []
    for x in range(points.x.start, points.x.stop):
        for y in range(points.y.start, points.y.stop):
            list_point.append(Point(x, y))

    return list_point


########################################

# point = Point(slice(0, 2), slice(0, 1))

# points = Point(
#     slice(max(0, point.x.start - 1), max(0, point.x.stop + 1)),
#     slice(max(0, point.y.start - 1), max(0, point.y.stop + 1)),
# )

# print(matrix[points.x, points.y])
# print(matrix)

########################################

# point = Point(9, 9)

# print(matrix[point.x, point.y])


# points = Point(
#     slice(max(0, point.x - 1), min(col, point.x + 2)),
#     slice(max(0, point.y - 1), min(row, point.y + 2)),
# )
# print(matrix[points.x, points.y])
# print(matrix)
# for p in get_list_of_point(points):
#     print(p)

########################################

point = Point(9, 9)

print(matrix[point.x, point.y])


points = Point(
    slice(point.x, point.x + 1),
    slice(0, row),
)
print(matrix[points.x, points.y])
print(matrix)
for p in get_list_of_point(points):
    print(p)
