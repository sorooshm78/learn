from tasks import add


add.delay(1, 1)
add.apply_async([2, 2])
add.apply_async([3, 3], countdown=3)
add.apply_async([4, 4], expires=5)
