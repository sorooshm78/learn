def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


class Person:
    def __init__(self, name):
        self.name = name

    @do_twice
    def show_name(self):
        print(f"name -> {self.name}")


p = Person("sm")
p.show_name()
# name -> sm
# name -> sm

# ----------------------------------------

# One new and exciting feature coming in Python 3.7 is the data class.
# A data class is a class typically containing mainly data, although there aren’t really any restrictions.
# It is created using the new @dataclass decorator, as follows:

from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


# The meaning of the syntax is similar to the function decorators.
# In the example above, you could have done the decoration by writing PlayingCard = dataclass(PlayingCard).

d = DataClassCard("rank", "suit")

print(d)
# DataClassCard(rank='rank', suit='suit')

print(d.rank)
# rank

print(d == DataClassCard("rank", "suit"))
# True

# Writing a class decorator is very similar to writing a function decorator.
# The only difference is that the decorator will receive a class and not a function as an argument.
# In fact, all the decorators you saw above will work as class decorators.
# When you are using them on a class instead of a function, their effect might not be what you want.
# In the following example, the @timer decorator is applied to a class:


import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"name -> {self.name}")


# Here, @timer only measures the time it takes to instantiate the class:

p = Person("sm")  # Person = timer(Person).
# Finished 'Person' in 0.0000 secs

p.show_name()
# name -> name

# ----------------------------------------
