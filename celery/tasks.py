from celery import Celery, signals
from celery.schedules import crontab
import time


BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = "redis://localhost"


app = Celery(
    main="tasks",
    broker=BROKER_URL,
    backend=BACKEND_URL,
)

# app.conf.update(
#     event_serializer="pickle",
#     task_serializer="pickle",
#     result_serializer="pickle",
#     accept_content=["application/json", "application/x-python-serialize"],
# )

# app.conf.update(
#     task_default_queue="default_queue",
#     task_routes={
#         "tasks.add": {"queue": "math"},
#         "tasks.long_task": {"queue": "long"},
#     },
# )

# app.config_from_object("celery_conf")


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


@app.task
def do_signal_task():
    return "work..."


@app.task
def do_schedules_task():
    print("say hellow...")


@app.task
def call_print_method(obj):
    return obj.print()


# ------------------ Signals ------------------


@signals.before_task_publish.connect(sender="tasks.do_signal_task")
def print_before_task_publish(sender=None, **kwargs):
    print("befor task published")


@signals.after_task_publish.connect(sender="tasks.do_signal_task")
def print_after_task_publish(sender=None, **kwargs):
    print("after task published")


@signals.task_prerun.connect(sender=do_signal_task)
def print_task_prerun(sender=None, **kwargs):
    print("befor task run")


@signals.task_postrun.connect(sender=do_signal_task)
def print_task_postrun(sender=None, **kwargs):
    print("after task run")


# ------------------ Schedules Tasks ------------------

app.conf.beat_schedule = {
    "print_hellow_every_minute": {
        "task": "tasks.do_schedules_task",
        "schedule": crontab(),
    },
}
app.conf.timezone = "Asia/Tehran"
