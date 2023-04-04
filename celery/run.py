from tasks import add, add_when_binded, div, long_task, do_exception_task


add.delay(1, 1)
add.apply_async([2, 2])
add.apply_async([3, 3], countdown=3)
add.apply_async([4, 4], expires=5)

add_when_binded.delay(5, 5)

div.delay(4, 2)
div.delay(4, 0)

long_task.delay()

result = add.delay(8, 8)
print(result.get())

result = long_task.delay()
print(result.get())

result = long_task.delay()
print(result.get(timeout=5))

result = do_exception_task.delay()
print(result.get(propagate=False))
print(result.traceback)

result = do_exception_task.delay()
result.get(propagate=False)
print(result.status)

result = add.delay(9, 9)
result.get(propagate=False)
print(result.status)

result = do_exception_task.delay()
result.get(propagate=False)
print(result.failed())

result = add.delay(10, 10).forget()
print(result.get())

task = add.signature((1, 2))
result = task.delay()
print(result.get())

task = add.signature((1, 2))
result = task.apply_async(countdown=3)
print(result.get())

task = add.signature((1, 2))
task()  # executable signature task

add.apply_async((10, 10), link=div.signature((2,)))
# or
add.apply_async((10, 10), link=div.s(2))

add.apply_async((10, 10), link=div.signature((50, 5), immutable=True))
# or
add.apply_async((10, 10), link=div.si(50, 5))
