# A great convenience when working with Python, especially in the interactive shell, is its powerful introspection ability.
# Introspection is the ability of an object to know about its own attributes at runtime.
# For instance, a function knows its own name and documentation:


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_hello():
    print("hello")


print(say_hello)
# <function do_twice.<locals>.wrapper_do_twice at 0x7fb6fe78a4d0>

print(say_hello.__name__)
# wrapper_do_twice

print(help(say_hello))
# Help on function wrapper_do_twice in module __main__:
# wrapper_do_twice(*args, **kwargs)


# To fix this, decorators should use the @functools.wraps decorator,
# which will preserve information about the original function.

import functools

# The @functools.wraps decorator uses the function functools.update_wrapper()
# to update special attributes like __name__ and __doc__ that are used in the introspection


def new_do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@new_do_twice
def new_say_hello():
    print("new hellow")


print(new_say_hello)
# <function new_say_hello at 0x7f61bc8e3d00>

print(new_say_hello.__name__)
# new_say_hello

print(help(new_say_hello))
# Help on function new_say_hello in module __main__:
# new_say_hello()


# ---------------------------------------------

from functools import partial, update_wrapper


def add(x, y):
    """add two number"""
    return x + y


add_five = partial(add, 5)  # add(x=5, y)

print(add_five(6))  # add(x=5, y=6)
# 11

print(add_five(6, 2))
# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/decorators/_functools.py", line 77, in <module>
#     print(add_five(6, 2))
# TypeError: add() takes 2 positional arguments but 3 were given


add_two = partial(add, y=2)  # add(x, y=2)

print(add_two(5))  # add(x=5, y=2)
# 7


add_one = partial(add, 1)


print(add_one.__doc__)
# partial(func, *args, **keywords) - new function with partial application
#     of the given arguments and keywords.

update_wrapper(add_one, add)

print(add_one.__doc__)
# add two number

# ---------------------------------------------

from functools import partialmethod


class Demo:
    def __init__(self):
        self.color = "black"

    def _color(self, type):
        self.color = type

    set_red = partialmethod(_color, type="red")
    set_blue = partialmethod(_color, type="blue")
    set_green = partialmethod(_color, type="green")


obj = Demo()

print(obj.color)
# black

obj.set_blue()

print(obj.color)
# blue

# ---------------------------------------------

from functools import cmp_to_key


def cmp_age(p1, p2):
    if p1.age > p2.age:
        return 1
    elif p2.age > p1.age:
        return -1
    else:
        return 0


class Person:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"age : {self.age}"


persons = [
    Person(11),
    Person(1),
    Person(20),
    Person(19),
]

sorted_persons = sorted(persons, key=cmp_to_key(cmp_age))

print([p.age for p in persons])
# [11, 1, 20, 19]

print([p.age for p in sorted_persons])
# [1, 11, 19, 20]

# ---------------------------------------------

# SingleDispatch It is a function decorator. It transforms a function into a generic
# function so that it can have different behaviors depending upon the type of its first argument.
# It is used for function overloading, the overloaded implementations are registered using the register() attribute.

from functools import singledispatch


@singledispatch
def fun(s):
    print(s)


@fun.register(int)
def _(s):
    print(s * 2)


@fun.register(float)
def _(f):
    print(int(f))


fun("str")
# str

fun(10)
# 20

fun(25.36)
# 25

# ---------------------------------------------
