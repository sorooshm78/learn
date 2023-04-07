def foo(bar=[]):
    bar.append("baz")
    return bar


print(foo())
# ['baz']

print(foo())
# ['baz', 'baz']

print(foo())
# ['baz', 'baz', 'baz']

# ----------------------------


def foo(bar=[]):
    bar.append("baz")
    return bar


print(foo())
# ['baz']

print(foo())
# ['baz', 'baz']

print(foo(["a"]))
# ['a', 'baz']

print(foo())
# ['baz', 'baz', 'baz']


# ----------------------------


def foo(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar


foo()
# ["baz"]

foo()
# ["baz"]

foo()
# ["baz"]
