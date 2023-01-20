import time
from multiprocessing import Process, Queue, current_process


# def show(q):
#     num = q.get()
#     num += 1
#     q.put(num)


# def show(num):
#     num += 1


def add_item_to_list(_list):
    p = current_process()
    _list.append(f"new item {p.pid}")
    print(_list)


l = ["item"]


p1 = Process(target=add_item_to_list, args=(l,))
p2 = Process(target=add_item_to_list, args=(l,))

p1.start()
p2.start()

p1.join()
p2.join()

print(f"finally {l}")
