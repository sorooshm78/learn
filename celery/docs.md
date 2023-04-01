# [celery docs](https://docs.celeryq.dev/)

# Run Celery
celery --app tasks worker --loglevel INFO

celery -A tasks worker -l INFO


# Calling Tasks
The API defines a standard set of execution options, as well as three methods:
  - apply_async(args[, kwargs[, …]])
      
      Sends a task message.
  - delay(*args, **kwargs)
      
      Shortcut to send a task message, but doesn’t support execution options.


# Countdown
The task is guaranteed to be executed at some time after the specified date and time, but not necessarily at that exact time
this takes at least 3 seconds to return
```
>>> result = add.apply_async((2, 2), countdown=3)
>>> result.get()
```

# Expiration
The expires argument defines an optional expiry time, either as seconds after task publish, or a specific date and time using datetime:
```
>>> Task expires after one minute from now.
>>> add.apply_async((10, 10), expires=60)
>>> Also supports datetime
>>> from datetime import datetime, timedelta
>>> add.apply_async((10, 10), kwargs,
...                 expires=datetime.now() + timedelta(days=1)
```
When a worker receives an expired task it will mark the task as REVOKED (TaskRevokedError).


# Bound tasks
A task being bound means the first argument to the task will always be the task instance (self), just like Python bound methods:
```
logger = get_task_logger(__name__)
@app.task(bind=True)
def add(self, x, y):
    logger.info(self.request.id)
```
Bound tasks are needed for retries (using app.Task.retry()), for accessing information about the current task request, and for any additional
functionality you add to custom task base classes.

# Task Request
when you print(self.request) in bound task

id : The unique id of the executing task.

args  : Positional arguments.

kwargs : Keyword arguments.

retries : How many times the current task has been 

retried. An integer starting at 0.

expires : The original expiry time of the task (if any). This is in UTC time (depending on the enable_utc setting).

...
```
@app.task(bind=True)
def add_when_binded(self, x, y):
    print(f"self -> {self}")
    print(f"self.request -> {self.request}")
    return x + y

add_when_binded.delay(5,5)

self -> <@task: tasks.add_when_binded of tasks at 0x7f9d75232ef0>
self.request -> <Context: {'lang': 'py', 'task': 'tasks.add_when_binded', 'id': '63ae17f1-f1ee-40d5-9c78-e1db3f0607e1', 'shadow': None, 'eta': None, 'expires': None, 'group': None, 'group_index': None, 'retries': 0, 'timelimit': [None, None], 'root_id': '63ae17f1-f1ee-40d5-9c78-e1db3f0607e1', 'parent_id': None, 'argsrepr': '(5, 5)', 'kwargsrepr': '{}', 'origin': 'gen5697@sm', 'ignore_result': False, 'properties': {'correlation_id': '63ae17f1-f1ee-40d5-9c78-e1db3f0607e1', 'reply_to': 'e60526b7-ab38-3eb0-af75-05cf9579c2a9', 'delivery_mode': 2, 'delivery_info': {'exchange': '', 'routing_key': 'celery'}, 'priority': 0, 'body_encoding': 'base64', 'delivery_tag': 'a53030e5-1f7a-4363-b40d-8b8391aa8cfc'}, 'reply_to': 'e60526b7-ab38-3eb0-af75-05cf9579c2a9', 'correlation_id': '63ae17f1-f1ee-40d5-9c78-e1db3f0607e1', 'hostname': 'celery@sm', 'delivery_info': {'exchange': '', 'routing_key': 'celery', 'priority': 0, 'redelivered': None}, 'args': [5, 5], 'kwargs': {}, 'is_eager': False, 'callbacks': None, 'errbacks': None, 'chain': None, 'chord': None, 'called_directly': False, '_protected': 1}>
```

# Retrying
app.Task.retry() can be used to re-execute the task, for example in the event of recoverable errors.
When you call retry it’ll send a new message, using the same task-id, and it’ll take care to make sure the message is delivered to the same queue as the originating task.
When a task is retried this is also recorded as a task state, so that you can track the progress of the task using the result instance (see States).
Here’s an example using retry:

```
@app.task(bind=True)
def send_twitter_status(self, oauth, tweet):
    try:
        twitter = Twitter(oauth)
        twitter.update_status(tweet)
    except (Twitter.FailWhaleError, Twitter.LoginError) as exc:
        raise self.retry(exc=exc)
```

## Using a custom retry delay
When a task is to be retried, it can wait for a given amount of time before doing so, and the default delay is defined by the default_retry_delay attribute. By default this is set to 3 minutes. Note that the unit for setting the delay is in seconds (int or float).
You can also provide the countdown argument to retry() to override this default.
```
@app.task(bind=True, default_retry_delay=30 * 60)  # default retry in 30 minutes.
def add(self, x, y):
    try:
        something_raising()
    except Exception as exc:
        # overrides the default delay to retry after 1 minute
        raise self.retry(exc=exc, countdown=60)
```
## Task.max_retries
A number. Maximum number of retries before giving up. A value of None means task will retry forever.By default, this option is set to 3.

```
@app.task(bind=True, default_retry_delay=60)
def div(self, x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error ZeroDivisionError")
        self.retry(countdown=5, max_retries=1)

div.delay(4, 0)

[2023-04-01 15:07:14,793: WARNING/ForkPoolWorker-4] Error ZeroDivisionError
[2023-04-01 15:07:14,799: ERROR/ForkPoolWorker-4] Task tasks.div[e6d14086-21c3-4e8c-99e7-fbbe37d8dfc0] raised unexpected: MaxRetriesExceededError("Can't retry tasks.div[e6d14086-21c3-4e8c-99e7-fbbe37d8dfc0] args:(4, 0) kwargs:{}")
Traceback (most recent call last):
  File "/home/sm/src/learn/celery/tasks.py", line 27, in div
    return x / y
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/app/trace.py", line 451, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/app/trace.py", line 734, in __protected_call__
    return self.run(*args, **kwargs)
  File "/home/sm/src/learn/celery/tasks.py", line 30, in div
    self.retry(countdown=5, max_retries=1)
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/app/task.py", line 718, in retry
    raise self.MaxRetriesExceededError(
celery.exceptions.MaxRetriesExceededError: Can't retry tasks.div[e6d14086-21c3-4e8c-99e7-fbbe37d8dfc0] args:(4, 0) kwargs:{}

```

# Monitoring and Management Guide¶
## Commands
* shell: Drop into a Python shell.

The locals will include the celery variable: this is the current app. Also all known tasks will be automatically added to locals (unless the --without-tasks flag is set).

Uses Ipython, bpython, or regular python in that order if installed. You can force an implementation using --ipython, --bpython, or --python.

* status: List active nodes in this cluster
```
$ celery -A proj status
```
* result: Show the result of a task
```
$ celery -A proj result -t tasks.add 4e196aa4-0141-4601-8138-7aa33db0f577
```
Note that you can omit the name of the task as long as the task doesn’t use a custom result backend.

* purge: Purge messages from all configured task queues.
This command will remove all messages from queues configured in the CELERY_QUEUES setting:
```
$ celery -A proj purge
```
* inspect active: List active tasks
```
$ celery -A proj inspect active
```
These are all the tasks that are currently being executed.

* inspect scheduled: List scheduled ETA tasks
```
$ celery -A proj inspect scheduled
```
These are tasks reserved by the worker when they have an eta or countdown argument set.

* inspect reserved: List reserved tasks
```
$ celery -A proj inspect reserved
```
This will list all tasks that have been prefetched by the worker, and is currently waiting to be executed (doesn’t include tasks with an ETA value set).

* inspect revoked: List history of revoked tasks
```
$ celery -A proj inspect revoked
```

* inspect stats: Show worker statistics (see Statistics)
```
$ celery -A proj inspect stats
```

* inspect query_task: Show information about task(s) by id.

Any worker having a task in this set of ids reserved/active will respond with status and information.
```
$ celery -A proj inspect query_task e9f6c8f0-fec9-4ae8-a8c6-cf8c8451d4f8
```
You can also query for information about multiple tasks:

```
$ celery -A proj inspect query_task id1 id2 ... idN
```

# Flower: Real-time Celery web-monitor
## Usage

You can use pip to install Flower:
```
$ pip install flower
```
Running the flower command will start a web-server that you can visit:
```
$ celery -A proj flower
```
The default port is http://localhost:5555, but you can change this using the –port argument:
```
$ celery -A proj flower --port=5555
```
Broker URL can also be passed through the --broker argument :
```
$ celery flower --broker=amqp://guest:guest@localhost:5672//
or
$ celery flower --broker=redis://guest:guest@localhost:6379/0
```
Then, you can visit flower in your web browser :
```
$ open http://localhost:5555
```
Flower has many more features than are detailed here, including authorization options. Check out the official documentation for more information.
