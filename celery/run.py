import tasks
from celery import chain, group, chord


# tasks.add.delay(1, 1)
# tasks.add.apply_async([2, 2])
# tasks.add.apply_async([3, 3], countdown=3)
# tasks.add.apply_async([4, 4], expires=5)

# tasks.add_when_binded.delay(5, 5)

# tasks.div.delay(4, 2)
# tasks.div.delay(4, 0)

# tasks.long_task.delay()

# result = tasks.add.delay(8, 8)
# print(result.get())

# result = tasks.long_task.delay()
# print(result.get())

# result = tasks.long_task.delay()
# print(result.get(timeout=5))

# result = tasks.do_exception_task.delay()
# print(result.get(propagate=False))
# print(result.traceback)

# result = tasks.do_exception_task.delay()
# result.get(propagate=False)
# print(result.status)

# result = tasks.add.delay(9, 9)
# result.get(propagate=False)
# print(result.status)

# result = tasks.do_exception_task.delay()
# result.get(propagate=False)
# print(result.failed())

# result = tasks.add.delay(10, 10).forget()
# print(result.get())

# task = tasks.add.signature((1, 2))
# result = task.delay()
# print(result.get())

# task = tasks.add.signature((1, 2))
# result = task.apply_async(countdown=3)
# print(result.get())

# task = tasks.add.signature((1, 2))
# task()  # executable signature task

# tasks.add.apply_async((10, 10), link=tasks.div.signature((2,)))
# # or
# tasks.add.apply_async((10, 10), link=tasks.div.s(2))

# tasks.add.apply_async((10, 10), link=tasks.div.signature((50, 5), immutable=True))
# # or
# tasks.add.apply_async((10, 10), link=tasks.div.si(50, 5))

# res = chain(tasks.add.s(10, 10), tasks.sub.s(5), tasks.div.s(3))()
# print(res.get())

# res = chain(tasks.add.s(10, 10), tasks.sub.s(5), tasks.div.s(3)).apply_async()
# print(res.get())

# res = (tasks.add.s(2, 2) | tasks.add.s(4) | tasks.add.s(8))()
# print(res.get())

# res = (tasks.add.si(2, 2) | tasks.add.si(4, 4) | tasks.add.si(8, 8))()
# print(res.get())
# print(res.parent.get())
# print(res.parent.parent.get())

# res = chord(group(tasks.add.s(5, 5), tasks.sub.s(25, 10)))(tasks.tsum.s())
# print(res.get())

res = chord([tasks.add.s(5, 5), tasks.sub.s(25, 10)])(tasks.tsum.s())
print(res.get())
