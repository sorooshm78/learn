# The name Duck Typing comes from the phrase:
# “If it looks like a duck and quacks like a duck, it’s a duck”
# The object’s type itself is not significant in this we do not declare the argument in method prototypes.
# This means that compilers can not do type-checking.
# Therefore, what really matters is if the object has particular attributes at run time.
# Duck typing is hence implemented by dynamic languages

# ---------------------------------------

class Specialstring:
    def __len__(self):
        return 21


string = Specialstring()
# len call __len__ of object pass to it
print(len(string))

# ---------------------------------------

# in static type language

interface Flying:
    function fly()

class Bird(Flying):
    function fly():
        print("fly with wings")


class Airplane(Flying):
    function fly():
        print("fly with fuel")


class Fish(Swimming):
    function swim():
        print("fish swim in sea")


void flying(Flying obj):
    obj.fly()


flying(Bird())
flying(Airplane())
flying(Fish()) # This line gives a compile error

# ---------------------------------------

class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")


def flying(obj):
    obj.fly()


flying(Bird())
flying(Airplane())
flying(Fish())

# fly with wings
# fly with fuel
# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/ABC/duck_typing.py", line 42, in <module>
#     flying(Fish())
#   File "/home/sm/src/learn/python/ABC/duck_typing.py", line 37, in flying
#     obj.fly()
# AttributeError: 'Fish' object has no attribute 'fly'

# ---------------------------------------

# EAFP -> it’s easier to ask for forgiveness than permission

class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")


def flying(obj):
    try:
        obj.fly()
    except Exception:
        print("Can not flying")


flying(Bird())
flying(Airplane())
flying(Fish())

# fly with wings
# fly with fuel
# Can not flying


# ---------------------------------------

# LBYL -> Look Before You Leap


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")


def flying(obj):
    if hasattr(obj, "fly"):
        obj.fly()
    else:
        print("Can not flying")


flying(Bird())
flying(Airplane())
flying(Fish())

# fly with wings
# fly with fuel
# Can not flying

# ---------------------------------------
