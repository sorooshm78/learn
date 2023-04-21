import functools


def count_calls(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.count += 1
        print(f"Call {inner.count} of {func.__name__!r}")
        return func(*args, **kwargs)

    inner.count = 0
    return inner


@count_calls
def say_whee():
    print("Whee!")


say_whee()
# Call 1 of 'say_whee'
# Whee!

say_whee()
# Call 2 of 'say_whee'
# Whee!

say_whee()
# Call 3 of 'say_whee'
# Whee!

print(say_whee.count)
# 3

# ---------------------------------------------
