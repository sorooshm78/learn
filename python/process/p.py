import time
from multiprocessing import Process
from threading import Thread


def show(name):
    print(f"start {name}")
    time.sleep(3)
    counter = 0

    for i in range(100000000):
        counter += 1
    print(f"end {name}")


start = time.perf_counter()

# without any concrency
# show("name")
# show("name2")
# time : 17 second


# thread
# t1 = Thread(target=show, args=["name"])
# t2 = Thread(target=show, args=["name2"])

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# time : 13 second


# process
t1 = Process(target=show, args=["name"])
t2 = Process(target=show, args=["name2"])

t1.start()
t2.start()

t1.join()
t2.join()
# time : 9 second


end = time.perf_counter()


print(round(end - start))
