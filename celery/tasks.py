from celery import Celery
import time


BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = "redis://localhost"


app = Celery(
    main="tasks",
    broker=BROKER_URL,
    backend=BACKEND_URL,
)


@app.task
def add(x, y):
    return x + y


@app.task
def tsum(numbers):
    return sum(numbers)


@app.task
def sub(x, y):
    return x - y


@app.task(bind=True)
def add_when_binded(self, x, y):
    print(f"self -> {self}")
    print(f"self.request -> {self.request}")
    return x + y


@app.task(bind=True, default_retry_delay=60)
def div(self, x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error ZeroDivisionError")
        self.retry(countdown=5, max_retries=1)


@app.task
def long_task():
    time.sleep(10)


@app.task
def do_exception_task():
    raise Exception("Exception Error")
