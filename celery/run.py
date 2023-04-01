from tasks import add, add_when_binded, div, long_task


add.delay(1, 1)
add.apply_async([2, 2])
add.apply_async([3, 3], countdown=3)
add.apply_async([4, 4], expires=5)

add_when_binded.delay(5, 5)

div.delay(4, 2)
div.delay(4, 0)

long_task.delay()
