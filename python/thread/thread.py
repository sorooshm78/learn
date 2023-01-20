from threading import Thread
from time import sleep


def show(name):
    print(f"st {name}")
    sleep(3)
    print(f"en {name}")


t = Thread(target=show, args=["one"], daemon=True)
tt = Thread(target=show, args=["two"], daemon=True)


t.start()
tt.start()

# t.join()
# tt.join()

print("end main")
