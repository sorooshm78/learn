# A word on abstract Meta class
# You may have come across metaclasses when learning about abstract classes.
# A class defines how an instance of the class behaves (e.g. Animal describes how Lion will behave). On the other hand a metaclass defines how a class behaves (ABCMeta describes how every ABC class will behave). A class is an instance of a metaclass.
# The abc module comes with a metaclass ABCMeta. back in the days we had to use it to define metaclasses with metaclass=abc.ABCMeta.
# Nowadays, just inheriting from ABC does the same thing—so you don't have to worry about metaclasses at all!


class MyClass:
    pass


obj = MyClass()

print(type(obj))
# <class '__main__.MyClass'>

print(type(MyClass))
# <class 'type'>

print(isinstance(obj, MyClass))
# True

print(isinstance(MyClass, type))
# True

print(type(int))
# <class 'type'>

print(type(list))
# <class 'type'>

print(type(type))
# <class 'type'>

# --------------------------------------------------


class MetaClass(type):
    def __call__(self, *args, **kwargs):
        print("\n------->>> MetaClass __call__")
        print("self: ", self)
        print("args: ", args)
        print("kwargs: ", kwargs)

        obj = self.__new__(self, *args, **kwargs)

        obj.__init__(*args, **kwargs)

        return obj


class Sample(metaclass=MetaClass):
    def __new__(cls, *args, **kwargs):
        print("\n------->>> Sample __new__")
        print("cls: ", cls)
        print("args: ", args)
        print("kwargs: ", kwargs)

        obj = super().__new__(cls)
        return obj

    def __init__(self, x=0, y=0, z=0):
        print("\n------->>> Sample __init__")
        print("self: ", self)
        print("x: ", x)
        print("y: ", y)
        print("z: ", z)

        self.x = x
        self.y = y
        self.z = z


sample_obj = Sample("p_arg_1", "p_arg_2", z="k_arg")
# ------->>> MetaClass __call__
# self:  <class '__main__.Sample'>
# args:  ('p_arg_1', 'p_arg_2')
# kwargs:  {'z': 'k_arg'}

------->>> Sample __new__
cls:  <class '__main__.Sample'>
args:  ('p_arg_1', 'p_arg_2')
kwargs:  {'z': 'k_arg'}

------->>> Sample __init__
self:  <__main__.Sample object at 0x7f578772f3d0>
x:  p_arg_1
y:  p_arg_2
z:  k_arg

# --------------------------------------------------


class MetaClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print("\n------->>> MetaClass __prepare__")
        print("metaclass: ", metacls)
        print("name: ", name)
        print("superclasses: ", bases)
        print("extra arguments: ", kwargs)

        return {"class_code": 1633}


class Sample(metaclass=MetaClass):
    @classmethod
    def print_extra_info(cls):
        print("\n------->>> Sample print_extra_info")

        print("class_code:", cls.__dict__["class_code"])


print("Sample.__dict__:\n", Sample.__dict__)
Sample.print_extra_info()

# ------->>> MetaClass __prepare__
# metaclass:  <class '__main__.MetaClass'>
# name:  Sample
# superclasses:  ()
# extra arguments:  {}

# Sample.__dict__:
#  {'class_code': 1633, '__module__': '__main__', 'print_extra_info': <classmethod(<function Sample.print_extra_info at 0x7f2f54e264d0>)>, '__dict__': <attribute '__dict__' of 'Sample' objects>, '__weakref__': <attribute '__weakref__' of 'Sample' objects>, '__doc__': None}

# ------->>> Sample print_extra_info
# class_code: 1633

# --------------------------------------------------


class MyABCMetaClass(type):
    def __call__(self, *args, **kwargs):
        raise Exception("not intance from it")


class MyAbstractClass(metaclass=MyABCMetaClass):
    pass


o = MyAbstractClass()
# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/object_oriented/meta_class.py", line 141, in <module>
#     o = MyAbstractClass()
#   File "/home/sm/src/learn/python/object_oriented/meta_class.py", line 134, in __call__
#     raise Exception("not intance from it")
# Exception: not intance from it


# --------------------------------------------------
