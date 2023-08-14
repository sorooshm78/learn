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