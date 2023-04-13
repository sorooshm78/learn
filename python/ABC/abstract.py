from abc import ABC, abstractmethod


# class A(ABC):
#     def print(self):
#         pass


# class B(A):
#     def dispaly(self):
#         print("display")


# a = A()
# a.print()
# # not output and error


# b = B()
# b.print()
# b.dispaly()
# # display

# ---------------------------------------------

# class AbstractClass(ABC):
#     @abstractmethod
#     def abstractMethod(self):
#         pass


# class MyClass(AbstractClass):
#     def abstractMethod(self):
#         print("hellow")


# class MyClass2(AbstractClass):
#     pass


# i = AbstractClass()
# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/ABC/abstract.py", line 19, in <module>
#     i = AbstractClass()
# TypeError: Can't instantiate abstract class AbstractClass with abstract method abstractMethod


# o = MyClass()
# o.abstractMethod()
# # hellow


# o2 = MyClass2()
# # Traceback (most recent call last):
# #   File "/home/sm/src/learn/python/ABC/abstract.py", line 22, in <module>
# #     o2 = MyClass2()
# # TypeError: Can't instantiate abstract class MyClass2 with abstract method abstractMethod

# ---------------------------------------------


# class AbstractClass(ABC):
#     @abstractmethod
#     def abstractMethod(self):
#         print("abstract class")


# class MyClass(AbstractClass):
#     def abstractMethod(self):
#         print("sub class")


# class MyClass2(AbstractClass):
#     def abstractMethod(self):
#         super().abstractMethod()
#         print("sub class")


# o = MyClass()
# o.abstractMethod()
# # sub class

# o2 = MyClass2()
# o2.abstractMethod()
# # abstract class
# # sub class

# ---------------------------------------------


# class Animal(ABC):
#     @abstractmethod
#     def say(self):
#         pass


# class Reptiles(Animal):
#     @abstractmethod
#     def crawl(self):
#         pass


# class Dog(Animal):
#     def say(self):
#         print("hop hop")


# class Snake(Reptiles):
#     def say(self):
#         print("snake noise")

#     def crawl(self):
#         print("snake is crawl")


# a = Animal()
# # Traceback (most recent call last):
# #   File "/home/sm/src/learn/python/ABC/abstract.py", line 86, in <module>
# #     a = Animal()
# # TypeError: Can't instantiate abstract class Animal with abstract method say

# r = Reptiles()
# # Traceback (most recent call last):
# #   File "/home/sm/src/learn/python/ABC/abstract.py", line 92, in <module>
# #     r = Reptiles()
# # TypeError: Can't instantiate abstract class Reptiles with abstract methods crawl, say

# d = Dog()
# d.say()
# # hop hop

# s = Snake()
# s.say()
# s.crawl()
# # snake noise
# # snake is crawl


# ---------------------------------------------
