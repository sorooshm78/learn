# new_list = [experssion for member in iterable]

squares = [i * i for i in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# -------------------------------------

names = ["gholi", "sina", "gholam"]
print([name.upper() for name in names])
# ['GHOLI', 'SINA', 'GHOLAM']

# -------------------------------------

nums = [5, 10, 15, 20, 25, 30, 35]
print([num for num in nums if num % 2 == 0])
# [10, 20, 30]

# -------------------------------------

nums = [1.25, -9.4 > 5, 10.22, 3.78, -5.92, 1.18]
print([num if num > 0 else 0 for num in nums])
# [1.25, 0, 10.22, 3.78, 0, 1.18]

# -------------------------------------

print({i: i * i for i in range(5)})
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# -------------------------------------

cities = ["a", "b", "c", "d"]
print({city: [n for n in range(2)] for city in cities})
# {
#   'a': [0, 1],
#   'b': [0, 1],
#   'c': [0, 1],
#   'd': [0, 1]
# }

# -------------------------------------

matrix = [[i for i in range(5)] for _ in range(4)]
print(matrix)
# [
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
# ]

# -------------------------------------
