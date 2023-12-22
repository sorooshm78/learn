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


# Duck Typing
Another term that is often used when talking about Python is duck typing. This moniker comes from the phrase “if it walks like a duck and it quacks like a duck, then it must be a duck” (or any of its variations).

Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. Using duck typing you do not check types at all. Instead you check for the presence of a given method or attribute.

As an example, you can call len() on any Python object that defines a .__len__() method:

```
>>> class TheHobbit:
...     def __len__(self):
...         return 95022
...
>>> the_hobbit = TheHobbit()
>>> len(the_hobbit)
95022
```

Note that the call to len() gives the return value of the .__len__() method. In fact, the implementation of len() is essentially equivalent to the following:

```
def len(obj):
    return obj.__len__()
```

In order to call len(obj), the only real constraint on obj is that it must define a .__len__() method. Otherwise, the object can be of types as different as str, list, dict, or TheHobbit.

Duck typing is somewhat supported when doing static type checking of Python code, using structural subtyping. You’ll learn more about duck typing later.

It’s time for our first type hints! To add information about types to the function, you simply annotate its arguments and return value as follows:

```
def headline(text: str, align: bool = True) -> str:
    ...
```

The text: str syntax says that the text argument should be of type str. Similarly, the optional align argument should have type bool with the default value True. Finally, the -> str notation specifies that headline() will return a string

In terms of style, PEP 8 recommends the following:

* Use normal rules for colons, that is, no space before and one space after a colon: text: str.
* Use spaces around the = sign when combining an argument annotation with a default value: align: bool = True.
* Use spaces around the -> arrow: def headline(...) -> str.

Adding type hints like this has no runtime effect: they are only hints and are not enforced on their own. For instance, if we use a wrong type for the (admittedly badly named) align argument, the code still runs without any problems or warnings:

```
>>> print(headline("python type checking", align="left"))
Python Type Checking
--------------------
```

The most common tool for doing type checking is Mypy though. You’ll get a short introduction to Mypy in a moment, while you can learn much more about how it works later.

If you don’t already have Mypy on your system, you can install it using pip:

```
$ pip install mypy
```

This is essentially the same code you saw earlier: the definition of headline() and two examples that are using it.

Now run Mypy on this code:

```
$ mypy headlines.py
headlines.py:10: error: Argument "align" to "headline" has incompatible
                        type "str"; expected "bool"
```

# Annotations
Annotations were introduced in Python 3.0, originally without any specific purpose. They were simply a way to associate arbitrary expressions to function arguments and return values.

Years later, PEP 484 defined how to add type hints to your Python code, based off work that Jukka Lehtosalo had done on his Ph.D. project—Mypy. The main way to add type hints is using annotations. As type checking is becoming more and more common, this also means that annotations should mainly be reserved for type hints.

The next sections explain how annotations work in the context of type hints.

# Function Annotations
For functions, you can annotate arguments and the return value. This is done as follows:

```
def func(arg: arg_type, optarg: arg_type = default) -> return_type:
```

For arguments the syntax is argument: annotation, while the return type is annotated using -> annotation. Note that the annotation must be a valid Python expression.

The following simple example adds annotations to a function that calculates the circumference of a circle:

```
import math

def circumference(radius: float) -> float:
    return 2 * math.pi * radius
```

When running the code, you can also inspect the annotations. They are stored in a special .__annotations__ attribute on the function:

```
>>> circumference(1.23)
7.728317927830891

>>> circumference.__annotations__
{'radius': <class 'float'>, 'return': <class 'float'>}
```

Sometimes you might be confused by how Mypy is interpreting your type hints. For those cases there are special Mypy expressions: reveal_type() and reveal_locals(). You can add these to your code before running Mypy, and Mypy will dutifully report which types it has inferred. As an example, save the following code to reveal.py:

```
# reveal.py

import math
reveal_type(math.pi)

radius = 1
circumference = 2 * math.pi * radius
reveal_locals()
```

Next, run this code through Mypy:

```
$ mypy reveal.py
reveal.py:4: error: Revealed type is 'builtins.float'

reveal.py:8: error: Revealed local types are:
reveal.py:8: error: circumference: builtins.float
reveal.py:8: error: radius: builtins.int
```

Even without any annotations Mypy has correctly inferred the types of the built-in math.pi, as well as our local variables radius and circumference.

If Mypy says that “Name ‘reveal_locals‘ is not defined” you might need to update your Mypy installation. The reveal_locals() expression is available in Mypy version 0.610 and later.

Variable Annotations
In the definition of circumference() in the previous section, you only annotated the arguments and the return value. You did not add any annotations inside the function body. More often than not, this is enough.

However, sometimes the type checker needs help in figuring out the types of variables as well. Variable annotations were defined in PEP 526 and introduced in Python 3.6. The syntax is the same as for function argument annotations:

```
pi: float = 3.142

def circumference(radius: float) -> float:
    return 2 * pi * radius
```

The variable pi has been annotated with the float type hint.

Annotations of variables are stored in the module level __annotations__ dictionary:

```
>>> circumference(1)
6.284

>>> __annotations__
{'pi': <class 'float'>}
```

You’re allowed to annotate a variable without giving it a value. This adds the annotation to the __annotations__ dictionary, while the variable remains undefined:

```
>>> nothing: str
>>> nothing
NameError: name 'nothing' is not defined

>>> __annotations__
{'nothing': <class 'str'>}
```

Since no value was assigned to nothing, the name nothing is not yet defined.

# Variable Annotations
In the definition of circumference() in the previous section, you only annotated the arguments and the return value. You did not add any annotations inside the function body. More often than not, this is enough.

However, sometimes the type checker needs help in figuring out the types of variables as well. Variable annotations were defined in PEP 526 and introduced in Python 3.6. The syntax is the same as for function argument annotations:
```
pi: float = 3.142

def circumference(radius: float) -> float:
    return 2 * pi * radius
```
The variable pi has been annotated with the float type hint.

Annotations of variables are stored in the module level __annotations__ dictionary:

```
>>> circumference(1)
6.284

>>> __annotations__
{'pi': <class 'float'>}
```

You’re allowed to annotate a variable without giving it a value. This adds the annotation to the __annotations__ dictionary, while the variable remains undefined:

```

>>> nothing: str
>>> nothing
NameError: name 'nothing' is not defined
```
```
>>> __annotations__
{'nothing': <class 'str'>}
```
Since no value was assigned to nothing, the name nothing is not yet defined.

With simple types like str, float, and bool, adding type hints is as easy as using the type itself:
```
>>> name: str = "Guido"
>>> pi: float = 3.142
>>> centered: bool = False
```

With composite types, you are allowed to do the same:
```
>>> names: list = ["Guido", "Jukka", "Ivan"]
>>> version: tuple = (3, 7, 1)
>>> options: dict = {"centered": False, "capitalize": True}
```

However, this does not really tell the full story. What will be the types of names[2], version[0], and options["centered"]? In this concrete case you can see that they are str, int, and bool, respectively. However, the type hints themselves give no information about this.

Instead, you should use the special types defined in the typing module. These types add syntax for specifying the types of elements of composite types. You can write the following:

```
>>> from typing import Dict, List, Tuple

>>> names: List[str] = ["Guido", "Jukka", "Ivan"]
>>> version: Tuple[int, int, int] = (3, 7, 1)
>>> options: Dict[str, bool] = {"centered": False, "capitalize": True}
```

The typing module contains many more composite types, including Counter, Deque, FrozenSet, NamedTuple, and Set. In addition, the module includes other kinds of types that you’ll see in later sections.

Let’s return to the card game. A card is represented by a tuple of two strings. You can write this as Tuple[str, str], so the type of the deck of cards becomes List[Tuple[str, str]]. Therefore you can annotate create_deck() as follows:

```
def create_deck(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck
```

In addition to the return value, you’ve also added the bool type to the optional shuffle argument.

In many cases your functions will expect some kind of /*sequence*/, and not really care whether it is a list or a tuple. In these cases you should use typing.Sequence when annotating the function argument:
```
from typing import List, Sequence

def square(elems: Sequence[float]) -> List[float]:
    return [x**2 for x in elems]
```

Using Sequence is an example of using duck typing. A Sequence is anything that supports len() and .__getitem__(), independent of its actual type.

# Type Aliases
The type hints might become quite oblique when working with nested types like the deck of cards. You may need to stare at List[Tuple[str, str]] a bit before figuring out that it matches our representation of a deck of cards.

Now consider how you would annotate deal_hands():
```
def deal_hands(
    deck: List[Tuple[str, str]]
) -> Tuple[
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])
```
That’s just terrible!

Recall that type annotations are regular Python expressions. That means that you can define your own type aliases by assigning them to new variables. You can for instance create Card and Deck type aliases:

```
from typing import List, Tuple

Card = Tuple[str, str]
Deck = List[Card]
```
Card can now be used in type hints or in the definition of new type aliases, like Deck in the example above.

Using these aliases, the annotations of deal_hands() become much more readable:
```
def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])
```
Type aliases are great for making your code and its intent clearer. At the same time, these aliases can be inspected to see what they represent:

```
>>> from typing import List, Tuple
>>> Card = Tuple[str, str]
>>> Deck = List[Card]

>>> Deck
typing.List[typing.Tuple[str, str]]
```

Note that when printing Deck, it shows that it’s an alias for a list of 2-tuples of strings.

# Functions Without Return Values
You may know that functions without an explicit return still return None:
```
>>> def play(player_name):
...     print(f"{player_name} plays")
...

>>> ret_val = play("Jacob")
Jacob plays

>>> print(ret_val)
None
```
While such functions technically return something, that return value is not useful. You should add type hints saying as much by using None also as the return type:

# play.py
```
def play(player_name: str) -> None:
    print(f"{player_name} plays")

ret_val = play("Filip")
```
The annotations help catch the kinds of subtle bugs where you are trying to use a meaningless return value. Mypy will give you a helpful warning:
```
$ mypy play.py
play.py:6: error: "play" does not return a value
```
Note that being explicit about a function not returning anything is different from not adding a type hint about the return value:

# play.py
```
def play(player_name: str):
    print(f"{player_name} plays")

ret_val = play("Henrik")
```
In this latter case Mypy has no information about the return value so it will not generate any warning:
```
$ mypy play.py
Success: no issues found in 1 source file
```
As a more exotic case, note that you can also annotate functions that are never expected to return normally. This is done using NoReturn:

```
from typing import NoReturn

def black_hole() -> NoReturn:
    raise Exception("There is no going back ...")
```

Since black_hole() always raises an exception, it will never return properly.

# The Any Type
choose() works for both lists of names and lists of cards (and any other sequence for that matter). One way to add type hints for this would be the following:
```
import random
from typing import Any, Sequence

def choose(items: Sequence[Any]) -> Any:
    return random.choice(items)
```
This means more or less what it says: items is a sequence that can contain items of any type and choose() will return one such item of any type. Unfortunately, this is not that useful. Consider the following example:
```
# choose.py

import random
from typing import Any, Sequence

def choose(items: Sequence[Any]) -> Any:
    return random.choice(items)

names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

name = choose(names)
reveal_type(name)
```

While Mypy will correctly infer that names is a list of strings, that information is lost after the call to choose() because of the use of the Any type:

```
$ mypy choose.py
choose.py:10: error: Revealed type is 'builtins.list[builtins.str*]'
choose.py:13: error: Revealed type is 'Any'
```

You’ll see a better way shortly. First though, let’s have a more theoretical look at the Python type system, and the special role Any plays.

# Duck Types and Protocols
Recall the following example from the introduction:
```
def len(obj):
    return obj.__len__()
```
len() can return the length of any object that has implemented the .__len__() method. How can we add type hints to len(), and in particular the obj argument?

The answer hides behind the academic sounding term structural subtyping. One way to categorize type systems is by whether they are nominal or structural:

In a nominal system, comparisons between types are based on names and declarations. The Python type system is mostly nominal, where an int can be used in place of a float because of their subtype relationship.

In a structural system, comparisons between types are based on structure. You could define a structural type Sized that includes all instances that define .__len__(), irrespective of their nominal type.

There is ongoing work to bring a full-fledged structural type system to Python through PEP 544 which aims at adding a concept called protocols. Most of PEP 544 is already implemented in Mypy though.

A protocol specifies one or more methods that must be implemented. For example, all classes defining .__len__() fulfill the typing.Sized protocol. We can therefore annotate len() as follows:
```
from typing import Sized

def len(obj: Sized) -> int:
    return obj.__len__()
```
Other examples of protocols defined in the typing module include Container, Iterable, Awaitable, and ContextManager.

You can also define your own protocols. This is done by inheriting from Protocol and defining the function signatures (with empty function bodies) that the protocol expects. The following example shows how len() and Sized could have been implemented:
```
from typing_extensions import Protocol

class Sized(Protocol):
    def __len__(self) -> int: ...

def len(obj: Sized) -> int:
    return obj.__len__()
```
At the time of writing the support for self-defined protocols is still experimental and only available through the typing_extensions module. This module must be explicitly installed from PyPI by doing pip install typing-extensions
