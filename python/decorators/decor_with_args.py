import functools


def repeat(count):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper_repeat

    return decorator_repeat


@repeat(count=2)
def say_hi():
    print("hi")


# f = repeat(count=1)
# f(say_hello)

say_hi()  # repeat(count=2)(say_hi)

# hi
# hi

# ----------------------------------


# def name(_func=None, *, kw1=val1, kw2=val2, ...):
#     def decorator_name(func):
#         ...  # Create and return a wrapper function.

#     if _func is None:
#         return decorator_name
#     else:
#         return decorator_name(_func)


def repeat(_func=None, count=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(count):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat
def say_hello():
    print("hello")


say_hello()
# hello
# hello


@repeat(count=3)
def say_great():
    print("great")


say_great()
# great
# great
# great

# ----------------------------------
