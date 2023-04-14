import abc

# Abstract classes are classes that contain one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
# Our example implemented a case of simple inheritance which has nothing to do with an abstract class.
# In fact, Python on its own doesn't provide abstract classes.
# Yet, Python comes with a module which provides the infrastructure for defining Abstract Base Classes (ABCs).


class A(abc.ABC):
    def show(self):
        pass


class B(A):
    pass


a = A()
b = B()
# not error

# ---------------------------------------

from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def arrive_at_work(self, arrival_time):
        pass


class Staff(Employee):
    def arrive_at_work(self):
        print("Arriving at datagy.io headquarters at 7:30!")


class Manager(Employee):
    def arrive_at_work(self, arrival_time):
        print(f"Arriving at datagy.io headquarters at {arrival_time}!")


class Supervisor(Employee):
    def arrive_at_work(self, arrival_time, location):
        print(f"Reporting at datagy.io at {arrival_time} at the {location} office!")


stf = Staff()
stf.arrive_at_work()
# Arriving at datagy.io headquarters at 7:30!

nik = Manager()
nik.arrive_at_work(8)
# Arriving at datagy.io headquarters at 8!


katie = Supervisor()
katie.arrive_at_work(9, "Toronto")
# Reporting at datagy.io at 9 at the Toronto office!


# ---------------------------------------
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass


class Manager(Employee):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


nik = Manager("Nik")
print(nik.name)

# Nik

# ---------------------------------------
from abc import ABC, abstractproperty


# Abstract class
class Hero(ABC):
    @abstractproperty
    def hero_name(self):
        return self.hname

    @abstractproperty
    def reel_name(self):
        return self.rname


# Derived class
class RDJ(Hero):
    def __init__(self):
        self.hname = "IronMan"
        self.rname = "Tony Stark"

    @property
    def hero_name(self):
        return self.hname

    @property
    def reel_name(self):
        return self.rname


data = RDJ()
print(f"The hero name is: {data.hero_name()}")
print(f"The reel name is: {data.reel_name}")

# The hero name is: IronMan
# The reel name is: Tony Stark


# ---------------------------------------
from abc import ABC, abstractproperty


# Abstract class
class Hero(ABC):
    # @property
    # @abstractmethod
    # def hero_name(self):
    #     return self.hname

    @abstractproperty
    def hero_name(self):
        return self.hname

    @abstractproperty
    def reel_name(self):
        return self.rname


# Derived class
class RDJ(Hero):
    def __init__(self):
        self.hname = "IronMan"
        self.rname = "Tony Stark"

    def hero_name(self):
        return self.hname

    def reel_name(self):
        return self.rname


data = RDJ()
print(f"The hero name is: {data.hero_name()}")
print(f"The reel name is: {data.reel_name()}")

# The hero name is: IronMan
# The reel name is: Tony Stark
