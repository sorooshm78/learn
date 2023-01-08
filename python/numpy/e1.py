import numpy as np


arr = np.array([1, 2, 3])
print(arr)  # [1 2 3]


arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)  # [[1 2 3] [4 5 6]]


arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])  # 7


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
print("0 row 1 column: ", arr[0, 1])  # 2


arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # int64


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  # (2, 4)


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(arr.shape)  # (2, )


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
