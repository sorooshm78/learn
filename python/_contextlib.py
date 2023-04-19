from contextlib import ContextDecorator, contextmanager, closing, suppress


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

# --------------------------------


class MyContextManager:
    def __enter__(self):
        print("enter ...")

    def __exit__(self, exc_type, value, traceback):
        if exc_type == ZeroDivisionError:
            print("handle ZeroDivisionError exception")
        print("exit ...")
        return True


with MyContextManager() as m:
    num = 10 / 0

# enter ...
# handle ZeroDivisionError exception
# exit ...

# --------------------------------


class MyContextManager:
    def __enter__(self):
        print("enter ...")

    def __exit__(self, exc_type, value, traceback):
        print("exit ...")

    def close(self):
        print("closing ...")


with closing(MyContextManager()) as m:
    print("do work")

# do work
# closing ...

# --------------------------------

with suppress(ZeroDivisionError):
    print("before exception")
    num = 100 / 0
    print("after exection")

# before exception
# Hint : not exection raised
