# Typing in Python
We'll also dive into how you can use Python's type system for static type checking with mypy
and runtime type checking with pydantic, marshmallow, and typeguard.

## Static typing
* mypy

## Runtime type checking / data validation
* marshmallow
* pydantic

# Type Hints
Type hints were added to Python in version 3.5.
They allow developers to annotate expected types for variables, function parameters,
and function returns inside Python code.
While such types are not enforced by the Python interpreter -- again,
Python is a dynamically typed language -- they do offer a number of benefits.
First and foremost, with type hints, you can better express the intent of what it is that your code is doing and how to use it.
Better understanding results in fewer bugs

```
def daily_average(temperatures: list[float]) -> float:
    return sum(temperatures) / len(temperatures)


print(daily_average.__annotations__)
{'temperatures': list[float], 'return': <class 'float'>}
```

# Type Annotations vs Type Hints
Type annotations are just syntax to annotate function inputs, function outputs, and variables:

```
def sum_xy(x: 'an integer', y: 'another integer') -> int:
    return x + y


print(sum_xy.__annotations__)
{'x': 'an integer', 'y': 'another integer', 'return': <class 'int'}
```

Type hints are built on top of annotations to make them more useful. Hints and annotations are often used interchangeably, but they are different

# Python's typing Module
You may be wondering why sometimes you see code like this:

```
from typing import List


def daily_average(temperatures: List[float]) -> float:
    return sum(temperatures) / len(temperatures)
```

It's using the built-in float to define the function return type, but the List is imported from the typing module.

Before Python 3.9, the Python interpreter didn't support the use of built-ins with arguments for type hinting.

For example, it was possible to use list as a type hint like so:

```
def daily_average(temperatures: list) -> float:
    return sum(temperatures) / len(temperatures)
```

But it wasn't possible to define the expected type of list elements (list[float]) without the typing module. The same can be said for dictionaries and other sequences and complex types:

```
from typing import Tuple, Dict


def generate_map(points: Tuple[float, float]) -> Dict[str, int]:
    return map(points)
```
Besides that, the typing module allows you to define new types, type aliases, type Any and many other things.

For example, you may want to allow multiple types. For that you can use Union:

```
from typing import Union


def sum_ab(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b
```
Since Python 3.9 you can use built-ins like so:

```
def sort_names(names: list[str]) -> list[str]:
    return sorted(names)
```

Since Python 3.10, you can use | to define union types:

```
def sum_ab(a: int | float, b: int | float) -> int | float:
    return a + b
```

