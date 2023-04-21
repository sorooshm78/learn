# A great convenience when working with Python, especially in the interactive shell, is its powerful introspection ability.
# Introspection is the ability of an object to know about its own attributes at runtime.
# For instance, a function knows its own name and documentation:


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_hello():
    print("hello")


print(say_hello)
# <function do_twice.<locals>.wrapper_do_twice at 0x7fb6fe78a4d0>

print(say_hello.__name__)
# wrapper_do_twice

print(help(say_hello))
# Help on function wrapper_do_twice in module __main__:
# wrapper_do_twice(*args, **kwargs)


# To fix this, decorators should use the @functools.wraps decorator,
# which will preserve information about the original function.

import functools

# The @functools.wraps decorator uses the function functools.update_wrapper()
# to update special attributes like __name__ and __doc__ that are used in the introspection


def new_do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@new_do_twice
def new_say_hello():
    print("new hellow")


print(new_say_hello)
# <function new_say_hello at 0x7f61bc8e3d00>

print(new_say_hello.__name__)
# new_say_hello

print(help(new_say_hello))
# Help on function new_say_hello in module __main__:
# new_say_hello()
