# The Python Data Model
strange to use len(collection) instead of collection.len().

The Python interpreter invokes special methods to perform basic object
operations, often triggered by special syntax. The special method names are always
written with leading and trailing double underscores. For example, the syntax
obj[key] is supported by the __getitem__ special method. In order to evaluate
my_collection[key], the interpreter calls my_collection.__getitem__(key).

"double underscore before and after.” That’s
why the special methods are also known as dunder methods. The
“Lexical Analysis” chapter of The Python Language Reference warns
that “Any use of __*__ names"

"One reason to still use my_fmt.format() is when the definition of
my_fmt must be in a different place in the code than 
where the formatting operation needs to happen"


We use ***namedtuple*** to build classes of objects that
are just bundles of attributes with no custom methods, like a database record

```
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
```

```
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
```

We’ve just seen two advantages of using special methods to leverage the Python Data Model:

• Users of your classes don’t have to memorize arbitrary method names for standard operations.
(“How to get the number of items? Is it .size(), .length(), or what?”)

• It’s easier to benefit from the rich Python standard library and avoid reinventing
the wheel, like the random.choice function.

As implemented so far, a FrenchDeck cannot be shuffled because it is immutable (namedtuple, tuple : immutable): the cards and their positions cannot be changed

The first thing to know about special methods is that they are meant to be called by
the Python interpreter, and not by you. You don’t write my_object.__len__(). You
write len(my_object) and, if my_object is an instance of a user-defined class, then
Python calls the __len__ method you implemented.

But the interpreter takes a shortcut when dealing for built-in types like list, str,
bytearray, or extensions like the NumPy arrays. Python variable-sized collections
written in C include a struct2 called PyVarObject, which has an ob_size field holding
the number of items in the collection. So, if my_object is an instance of one of those
built-ins, then len(my_object) retrieves the value of the ob_size field, and this is
much faster than calling a method.

Normally, your code should not have many direct calls to special methods. Unless
you are doing a lot of metaprogramming, you should be implementing special meth‐
ods more often than invoking them explicitly. The only special method that is fre‐
quently called by user code directly is __init__ to invoke the initializer of the
superclass in your own __init__ implementation.

```
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

!r in fstring actually call __repr__ object for example : 

print("{obj!r}") == print("{obj.__repr__()"})
print("{obj"}) == print("{obj.__str__()}")

```
class A:
    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"


class B:
    def __init__(self, a_obj):
        self.obj = a_obj

    def show(self):
        print(f"{self.obj}")  # str
        print(f"{self.obj!r}")  # repr


a = A()
b = B(a)
b.show()
# str
# repr
```

implements two operators: + and *, to show basic usage of __add__ and
__mul__. In both cases, the methods create and return a new instance of Vector, and
do not modify either operand—self or other are merely read

```
a * b -> a.__mul__(b)
a * b -> b.__rmul__(a)
```

The __repr__ special method is called by the repr built-in to get the string represen‐
tation of the object for inspection. Without a custom __repr__, Python’s console
would display a Vector instance <Vector object at 0x10e100070>

The interactive console and debugger call repr on the results of the expressions eval‐
uated, as does the %r placeholder in classic formatting with the % operator, and the !r
conversion field in the new format string syntax used in f-strings the str.format
method

classic formatting
```
"old format %r" % ("str") -> "old format 'str'"
```

new formatting
```
"new format {'str'!r}" -> "new format 'str'"
```

Sometimes same string returned by __repr__ is user-friendly, and you don’t need to
code __str__ because the implementation inherited from the object class calls
__repr__ as a fallback.

Programmers with prior experience in languages with a toString
method tend to implement __str__ and not __repr__. If you only
implement one of these special methods in Python, choose
__repr__.

By default, instances of user-defined classes are considered truthy, unless either
__bool__ or __len__ is implemented. Basically, bool(x) calls x.__bool__() and uses
the result. If __bool__ is not implemented, Python tries to invoke x.__len__(), and
if that returns zero, bool returns False. Otherwise bool returns True.

```
class A:
    # must return True or False
    def __bool__(self):
        return true

    def __len__(self):
        return 0

a = A()

bool(a)
# call __bool__()
# if not exist __bool__() then call __len__() if return 0 bool func return False else return True 
```

## Collection API
documents the interfaces of the essential collection types in the language.
All the classes in the diagram are ABCs—abstract base classes.

![1](images/1.png)

UML class diagram with fundamental collection types. Method names in
italic are abstract, so they must be implemented by concrete subclasses such as list
and dict. The remaining methods have concrete implementations, therefore subclasses
can inherit them.

concrete method (normal method) != abstract method 
concrete class != abstract class 

every collection should implement:
• Iterable to support for, unpacking, and other forms of iteration
• Sized to support the len built-in function
• Container to support the in operator

Python does not require concrete classes to actually inherit from any of these ABCs.
Any class that implements __len__ satisfies the Sized interface.

Three very important specializations of Collection are:
• Sequence, formalizing the interface of built-ins like list and str
• Mapping, implemented by dict, collections.defaultdict, etc.
• Set, the interface of the set and frozenset built-in types

Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists

```
Syntax: defaultdict(default_factory)
Parameters:  

    default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
```

```
from collections import defaultdict

def def_value():
    return "Not Present"

d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
```

Output:
```
1
2
Not Present 
```

Inner Working of defaultdict
The __missing__(self, key) method defines the behavior of a dictionary subclass if you access a non-existent key. More specifically, Python’s __getitem__() dictionary method internally calls the __missing__() method if the key doesn’t exist. The return value of __missing__() is the value to be returned when trying to access a non-existent key.

Since Python 3.7, the dict type is officially “ordered,” but that only
means that the key insertion order is preserved. You cannot
rearrange the keys in a dict however you like.

https://www.fluentpython.com/extra/internals-of-sets-and-dicts/  or  [link](set_and_dict.html)
https://tenthousandmeters.com/

__init_subclass__

To have a clear understanding of using init_subclass, let’s have a look at a simple example. Imagine a base class, Animal, with diverse subclasses, along with Cat, Dog, and Fish. We want to ensure that each time a new Animal subclass is created, a category attribute called 'species' is assigned.
```
class Animal:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'species'):
            raise TypeError(f"{cls.__name__} must have a 'species' attribute")
   
class Cat(Animal):
    species = 'Feline'

class Dog(Animal):
    species = 'Canine'

class Fish(Animal):  # This will raise a TypeError
    pass
```

```
class Plugin:
    _registry = {}
   
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._registry[cls.__name__] = cls

class PluginA(Plugin):
    pass

class PluginB(Plugin):
    pass

print(Plugin._registry)
```

Output
```
{'PluginA': <class 'main.PluginA'>, 'PluginB': <class 'main.PluginB'>}
```

Always Invoke super().__init_subclass__()

When enforcing __init_subclass__, it is important to name the super().__init_subclass__(**kwargs) technique. This ensures that the base class's __init_subclass__ method is achieved, permitting the right inheritance and the ideal behavior of the method in multiple inheritance situations

__getattr__

```
class Dummy(object):
    pass

d = Dummy()
d.does_not_exist  # Fails with AttributeError
```

```
class Dummy(object):
    def __getattr__(self, attr):
        return attr.upper()

d = Dummy()
d.does_not_exist # 'DOES_NOT_EXIST'
d.what_about_this_one  # 'WHAT_ABOUT_THIS_ONE'
```

```
class Dummy(object):
    def __getattr__(self, attr):
        return attr.upper()

d = Dummy()
d.value = "Python"
print(d.value)  # "Python"
```

__getattribute__

__getattribute__ is similar to __getattr__, with the important difference that __getattribute__ will intercept EVERY attribute lookup, doesn’t matter if the attribute exists or not. Let me show you a simple example:
```
class Dummy(object):
    def __getattribute__(self, attr):
        return 'YOU SEE ME?'

d = Dummy()
d.value = "Python"
print(d.value)  # "YOU SEE ME?"
```

## bisect
he bisect module offers two main functions that use the binary search algorithm to quickly find and insert items in any sorted sequence.

* Searching with bisect
* Inserting with insort

### Searching with bisect

Example 1
```
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # (1)
        offset = position * '  |'  # (2)
        print(ROW_FMT.format(needle, position, offset))  # (3)

if __name__ == '__main__':
    if sys.argv[-1] == 'left':    # (4)
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # (5)
    print('haystack ->', ' '.join(f'{n:2}' for n in HAYSTACK))
    demo(bisect_fn)
```

![E2](./images/02.png)

Second, bisect is actually an alias for bisect_right, and there is a sister function called bisect_left. Their difference is apparent only when the needle compares equal to an item in the list: bisect_right returns an insertion point after the existing item, and bisect_left returns the position of the existing item, so insertion would occur before it. With simple types like int, inserting before or after makes no difference, but if the sequence contains objects that are distinct yet compare equal, then it may be relevant. For example, 1 and 1.0 are distinct, but 1 == 1.0 is True. Figure 2 shows the result of using bisect_left.

![E3](./images/03.png)

Example 1 with bisect_left in use (compare with Figure 1 and note the insertion points for the values 1, 8, 23, 29, and 30 to the left of the same numbers in the haystack).

An interesting application of bisect is to perform table lookups by numeric values—​for example, to convert test scores to letter grades, as in Example 2.
Example 2. Given a test score, grade returns the corresponding letter grade

```
>>> breakpoints = [60, 70, 80, 90]
>>> grades='FDCBA'
>>> def grade(score):
...     i = bisect.bisect(breakpoints, score)
...     return grades[i]
...
>>> [grade(score) for score in [55, 60, 65, 70, 75, 80, 85, 90, 95]]
['F', 'D', 'D', 'C', 'C', 'B', 'B', 'A', 'A']
```

The code in Example 2 is from the bisect module documentation, which also lists functions to use bisect as a faster replacement for the index method when searching through long ordered sequences of numbers.

When used for table lookups, bisect_left produces very different results[1]. Note the letter grade results in Example 3.
Example 3. bisect_left maps a score of 60 to grade 'F', not 'D' as in Example 2.

```
>>> breakpoints = [60, 70, 80, 90]
>>> grades='FDCBA'
>>> def grade(score):
...     i = bisect.bisect_left(breakpoints, score)
...     return grades[i]
...
>>> [grade(score) for score in [55, 60, 65, 70, 75, 80, 85, 90, 95]]
['F', 'F', 'D', 'D', 'C', 'C', 'B', 'B', 'A']
```

### Inserting with insort

Sorting is expensive, so once you have a sorted sequence, it’s good to keep it that way. That is why bisect.insort was created.

insort(seq, item) inserts item into seq so as to keep seq in ascending order. See Example 4 and its output in Figure 3.
Example 4. Insort keeps a sorted sequence always sorted

```
import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print(f'{new_item:2d} -> {my_list}')
```
![E4](./images/04.png)

Figure 3. Output of Example 4
Like bisect, insort takes optional lo, hi arguments to limit the search to a sub-sequence. There is also an insort_left variation that uses bisect_left to find insertion points.

