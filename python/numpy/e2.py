import numpy as np


row = 10
col = 10
val = "o"

# 1
matrix = np.empty((row, col), "S")
matrix.fill(val)
print(matrix)


# 2
matrix = np.full((row, col), val)
print(matrix)
