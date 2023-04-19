from contextlib import ContextDecorator, contextmanager

@contextmanager
def example():
    print("starting ...")  # __enter__
    yield {}
    print("ending ...")  # __exit__


with example():
    print("do work")

# starting ...
# do work
# ending ...

# --------------------------------

class Network:
    def send(self):
        print("send message...")


@contextmanager
def example():
    print("starting ...")  # __enter__
    yield Network()
    print("ending ...")  # __exit__


with example() as n:
    print("do work")
    n.send()

# starting ...
# do work
# send message...
# ending ...


# --------------------------------


class mycontext(ContextDecorator):
    def __enter__(self):
        print("Starting")

    def __exit__(self, *exc):
        print("Finishing")


@mycontext()
def my_work():
    print("working ...")


my_work()
# Starting
# working ...
# Finishing

with mycontext():
    print("The bit in the middle")
# Starting
# The bit in the middle
# Finishing


# --------------------------------


class MyContextManager:
    def __enter__(self):
        print("enter ...")
        return self

    def __exit__(self, *exc):
        print("exit ...")
        return False

    def show_name(self):
        print("MyContextManager")


with MyContextManager() as m:
    m.show_name()

# enter ...
# MyContextManager
# exit ...
