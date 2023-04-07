import array as arr


# --------------- ---------------

numbers = arr.array("i", [10, 20, 30])

print(numbers[0])  # gets the 1st element
print(numbers[1])  # gets the 2nd element
print(numbers[2])  # gets the 3rd element

# 10
# 20
# 30

# --------------- ---------------

numbers = arr.array("i", [10, 20, "str"])

print(numbers[0])  # gets the 1st element
print(numbers[1])  # gets the 2nd element
print(numbers[2])  # gets the 3rd element

# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/data_structures/list.py", line 18, in <module>
#     numbers = arr.array("i", [10, 20, "str"])
# TypeError: 'str' object cannot be interpreted as an integer
