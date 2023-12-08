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

# Runtime Type Checking
## pydantic
Static type checkers don't help when dealing with data from external sources like the users of your application. That's where runtime type checkers come into play. One such tool is pydantic, which is used to validate data. It raises validation errors when the provided data does not match a type defined with a type hint.

pydantic uses type casting to convert input data to force it to conform to the expected type.

```
$ pip install pydantic
```

It's actually quite simple to use. For example, let's define a Song class with a few attributes:

```
from datetime import date

from pydantic import BaseModel


class Song(BaseModel):
    id: int
    name: str
    release: date
    genres: list[str]#
```

Along with leveraging type hints for data validation, you can also add custom validators to ensure correctness of data beyond its type. Adding custom validation for an attribute is fairly easy. For example, to prevent genre duplications in the Song class, you can add validation like so:
```
from datetime import date

from pydantic import BaseModel, field_validator


class Song(BaseModel):
    id: int
    name: str
    release: date
    genres: list[str]

    @field_validator('genres')
    def no_duplicates_in_genre(cls, v):
        if len(set(v)) != len(v):
            raise ValueError(
                'No duplicates allowed in genre.'
            )
        return v


song = Song(
    id=101,
    name='Bohemian Rhapsody',
    release='1975-10-31',
    genres=[
        'Hard Rock',
        'Progressive Rock',
        'Progressive Rock',
    ]
)
print(song)
# pydantic_core._pydantic_core.ValidationError: 1 validation error for Song
# genres
#   Value error, No duplicates allowed in genre. [type=value_error,
#     input_value=['Hard Rock', 'Progressiv...ck', 'Progressive Rock'], input_type=list]
#     For further information visit https://errors.pydantic.dev/2.5/v/value_error
```

So, the validation method, no_duplicates_in_genre, must be decorated with field_validator, which takes the attribute name as an argument. The validation method must be a class method since validation happens before the instance is created. For data that fails validation, it should raise a standard Python ValueError.

You can also use validator methods to alter the value before validation occurs. To do so, use mode='before':

```
@field_validator('genres', mode='before')
```

For example, you can convert genres to lower case like so:

```
from datetime import date

from pydantic import BaseModel, field_validator


class Song(BaseModel):
    id: int
    name: str
    release: date
    genres: list[str]

    @field_validator('genres', mode='before')
    def to_lower_case(cls, v):
        return [genre.lower() for genre in v]

    @field_validator('genres')
    def no_duplicates_in_genre(cls, v):
        if len(set(v)) != len(v):
            raise ValueError(
                'No duplicates allowed in genre.'
            )
        return v


song = Song(
    id=101,
    name='Bohemian Rhapsody',
    release='1975-10-31',
    genres=[
        'Hard Rock',
        'PrOgReSsIvE ROCK',
        'Progressive Rock',
    ]
)
print(song)
# pydantic_core._pydantic_core.ValidationError: 1 validation error for Song
# genres
#   Value error, No duplicates allowed in genre.
#     [type=value_error, input_value=['Hard Rock', 'PrOgReSsIv...CK', 'Progressive Rock'], input_type=list]
#     For further information visit https://errors.pydantic.dev/2.5/v/value_error
```
to_lower_case converts every element in the genres list to lowercase. Because of mode='before', this method is called before pydantic validates the types. All genres are converted to lowercase and then validated with no_duplicates_in_genre.

pydantic also offers more strict types like StrictStr and EmailStr to make your validations even better. Review Field Types from the docs for more on this.