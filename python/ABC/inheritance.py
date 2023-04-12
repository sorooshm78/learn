# class Person:
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber

#     def display(self):
#         print(self.name)
#         print(self.idnumber)


# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post

#         Person.__init__(self, name, idnumber)


# a = Employee("Rahul", 886012, 200000, "Intern")
# a.display()
# # Rahul
# # 886012

# --------------------------------------------------------


# class A:
#     def __init__(self, n="Rahul"):
#         self.name = n


# class B(A):
#     def __init__(self, roll):
#         self.roll = roll


# object = B(23)
# print(object.name)
# # Traceback (most recent call last):
# #   File "/home/sm/src/learn/python/ABC/inheritance.py", line 38, in <module>
# #     print(object.name)
# # AttributeError: 'B' object has no attribute 'name'


# --------------------------------------------------------


# class Base1(object):
#     def __init__(self):
#         self.str1 = "Geek1"
#         print("Base1")


# class Base2(object):
#     def __init__(self):
#         self.str2 = "Geek2"
#         print("Base2")


# class Derived(Base1, Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")

#     def printStrs(self):
#         print(self.str1, self.str2)


# ob = Derived()
# ob.printStrs()
# # Base1
# # Base2
# # Derived
# # Geek1 Geek2

# --------------------------------------------------------


# class Base1:
#     def print(self):
#         print("base1")


# class Base2:
#     def print(self):
#         print("base2")


# class Child(Base1, Base2):
#     def display(self):
#         super().print()


# c = Child()
# c.display()
# # base1

# --------------------------------------------------------
