def outer(x):
    def inner(y):
        return x + y

    return inner


add_five = outer(5)
result = add_five(6)
print(result)

# 11

# ------------------------------------


def greeting(name):
    def hello():
        print(f"Hello, {name}")

    return hello


greet = greeting("Sm")
greet()

# Hello, Sm

# ------------------------------------


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


decorated_func = make_pretty(ordinary)
decorated_func()

# I got decorated
# I am ordinary

# ------------------------------------


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()  # make_pretty(ordinary)()

# ------------------------------------


def make_pretty(func):
    def inner(name):
        print("I got decorated")
        func(name)

    return inner


@make_pretty
def say_hellow(name):
    print(f"hello {name}")


say_hellow("soroosh")  # make_pretty(say_hellow)("soroosh")

# I got decorated
# hello soroosh

# ------------------------------------


def make_pretty(func):
    def inner(*args, **kwargs):
        print("I got decorated")
        func(*args, **kwargs)

    return inner


@make_pretty
def say_hellow(name):
    print(f"hello {name}")


say_hellow("soroosh")
# I got decorated
# hello soroosh


# ------------------------------------


def my_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("can not")
            return

        return func(a, b)

    return inner


@my_divide
def divide(a, b):
    print(a / b)


divide(2, 5)
# I am going to divide 2 and 5
# 0.4

divide(2, 0)
# I am going to divide 2 and 0
# can not

# ------------------------------------


def attach_data(func):
    func.data = "data"
    return func


@attach_data
def add(x, y):
    return x + y


print(add(2, 3))
# 5

print(add.data)
# data


@attach_data
def print_twice_data():
    print(2 * print_twice_data.data)


print_twice_data()
# datadata


# ------------------------------------


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello") # star(percent(printer("Hello")))
# ***************
# %%%%%%%%%%%%%%%
# Hello
# %%%%%%%%%%%%%%%
# ***************

# ------------------------------------
