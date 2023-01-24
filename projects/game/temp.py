import numpy as np


class Cell:
    def __init__(self, ship=None):
        self.ship = ship
        self.is_selected = False

    def is_empty(self):
        if self.ship == None:
            return True
        return False


arr = np.empty((3, 3), dtype=object)

for y, x in np.ndindex(arr.shape):
    arr[x, y] = Cell()


# for x in np.nditer(arr, ["refs_ok"]):
#     print(x.item().is_selected)


# for cell in arr.flatten():
#     cell.is_selected = True

# print(arr)
# print(arr[0][0].is_selected)
# print(arr[2][2].is_selected)
