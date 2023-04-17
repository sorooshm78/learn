def gen():
    print("1 call")
    yield "1"

    print("2 call")
    yield "2"

    print("3 call")
    yield "3"


for step in gen():
    print(step)

# 1 call
# 1
# 2 call
# 2
# 3 call
# 3

# ----------------------------------------


def gen():
    yield "1"

    yield "2"

    print("before return")

    return 3

    print("after retrun")

    yield "4"


g = gen()

print(next(g))
print(next(g))
print(next(g))

# 1
# 2
# before return
# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/generator.py", line 42, in <module>
#     print(next(g))
# StopIteration: 3


for step in gen():
    print(step)

# 1
# 2
# before return

# ----------------------------------------


def gen():
    for counter in range(10):
        print(f"before yield {counter}")
        yield counter
        print(f"after yield {counter}")


g = gen()

print(next(g))
# before yield 0
# 0

print(next(g))
# after yield 0
# before yield 1
# 1


# ----------------------------------------

# Generator Expression Syntax
# A generator expression has the following syntax,
# (expression for item in iterable)


squares_generator = (i * i for i in range(5))

for i in squares_generator:
    print(i)

# 0
# 1
# 4
# 9
# 16


# ----------------------------------------

import sys

nums_squared_lc = [i**2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))
# 87624

nums_squared_gc = (i**2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
# 120


# ----------------------------------------
