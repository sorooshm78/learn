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

# Keeping Results
If you want to keep track of the tasks’ states, Celery needs to store or send the states somewhere. There are several built-in result backends to choose from: SQLAlchemy/Django ORM, MongoDB, Memcached, Redis, RPC (RabbitMQ/AMQP), and – or you can define your own.

Or if you want to use Redis as the result backend, but still use RabbitMQ as the message broker (a popular combination):

```
app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
```
Now with the result backend configured, close the current python session and import the tasks module again to put the changes into effect. This time you’ll hold on to the AsyncResult instance returned when you call a task:
```
>>> from tasks import add    # close and reopen to get updated 'app'
>>> result = add.delay(4, 4)
```
The ready() method returns whether the task has finished processing or not:
```
>>> result.ready()
False
```
You can wait for the result to complete, but this is rarely used since it turns the asynchronous call into a synchronous one:
```
>>> result.get(timeout=1)
8
```
```
result.get() 
# this is block until get result 
```
```
# do work 10 second 
result.get(timeout=5) 
# this is block until for timeout=5 and throw exception

raceback (most recent call last):
  File "/home/sm/src/learn/celery/run.py", line 26, in <module>
    print(result.get(timeout=5))
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/result.py", line 224, in get
    return self.backend.wait_for_pending(
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/backends/asynchronous.py", line 221, in wait_for_pending
    for _ in self._wait_for_pending(result, **kwargs):
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/backends/asynchronous.py", line 293, in _wait_for_pending
    raise TimeoutError('The operation timed out.')
celery.exceptions.TimeoutError: The operation timed out.

```

In case the task raised an exception, get() will re-raise the exception, but you can override this by specifying the propagate argument:
```
>>> result.get(propagate=False)
```
Do task what get exception
```
>>> result = do_exception_task.delay()
>>> result.get() # default result.get(propagate=True) 

# raise exception
Traceback (most recent call last):
  File "/home/sm/src/learn/celery/run.py", line 30, in <module>
    result.get()
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/result.py", line 224, in get
    return self.backend.wait_for_pending(
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/backends/asynchronous.py", line 223, in wait_for_pending
    return result.maybe_throw(callback=callback, propagate=propagate)
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/result.py", line 336, in maybe_throw
    self.throw(value, self._to_remote_traceback(tb))
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/result.py", line 329, in throw
    self.on_ready.throw(*args, **kwargs)
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/vine/promises.py", line 234, in throw
    reraise(type(exc), exc, tb)
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/vine/utils.py", line 30, in reraise
    raise value
Exception: Exception Error

```
```
>>> result = do_exception_task.delay()
>>> result.get(propagate=False)

Exception Error # print exception error
```

If the task raised an exception, you can also gain access to the original traceback:
```
>>> result.traceback
```
```
>>> result = do_exception_task.delay()
>>> result.get(propagate=False)

>>> result.traceback

# print exception 
Traceback (most recent call last):
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/app/trace.py", line 451, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/home/sm/src/learn/celery/.venv/lib/python3.10/site-packages/celery/app/trace.py", line 734, in __protected_call__
    return self.run(*args, **kwargs)
  File "/home/sm/src/learn/celery/tasks.py", line 44, in do_exception_task
    raise Exception("Exception Error")
Exception: Exception Error
```

failed() : Return True if the task failed.
```
>>> result = do_exception_task.delay()
>>> result.get(propagate=False)
>>> result.failed()

True
```
forget() : Forget the result of this task and its parents.
```
>>> r = add.delay(1,1).forget()
>>> r.get()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'get'
```

## Built-in States
PENDING : 
Task is waiting for execution or unknown. Any task id that’s not known is implied to be in the pending state.

STARTED : 
Task has been started. Not reported by default, to enable please see app.Task.track_started.

SUCCESS : 
Task has been successfully executed.

FAILURE : 
Task execution resulted in failure.

RETRY : 
Task is being retried.

REVOKED : 
Task has been revoked.

```
>>> result = do_exception_task.delay()
>>> result.get(propagate=False)
>>> result.status

FAILURE
```
```
>>> result = add.delay(9, 9)
>>> result.get(propagate=False)
>>> result.status

SUCCESS
```

# Configuration
Celery, like a consumer appliance, doesn’t need much configuration to operate. It has an input and an output. The input must be connected to a broker, and the output can be optionally connected to a result backend. However, if you look closely at the back, there’s a lid revealing loads of sliders, dials, and buttons: this is the configuration.

The default configuration should be good enough for most use cases, but there are many options that can be configured to make Celery work exactly as needed. Reading about the options available is a good idea to familiarize yourself with what can be configured.

The configuration can be set on the app directly or by using a dedicated configuration module. As an example you can configure the default serializer used for serializing task payloads by changing the task_serializer setting:
```
app.conf.task_serializer = 'json'
```
If you’re configuring many settings at once you can use update:
```
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)
```
For larger projects, a dedicated configuration module is recommended. Hard coding periodic task intervals and task routing options is discouraged. It is much better to keep these in a centralized location. This is especially true for libraries, as it enables users to control how their tasks behave. A centralized configuration will also allow your SysAdmin to make simple changes in the event of system trouble.

You can tell your Celery instance to use a configuration module by calling the app.config_from_object() method:
```
app.config_from_object('celeryconfig')
```
This module is often called “celeryconfig”, but you can use any module name.

In the above case, a module named celeryconfig.py must be available to load from the current directory or on the Python path. It could look something like this:

celeryconfig.py:
```
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

```

To verify that your configuration file works properly and doesn’t contain any syntax errors, you can try to import it:
```
$ python -m celeryconfig
```

## Global Config
```
app.conf.task_ignore_result = True

or 

app.conf.update(

)
```
## Locally close return task results:
```
@app.task(ignore_result=True)
def add(...):
```

## task_time_limit
Task hard time limit in seconds. The worker processing the task will be **killed** and replaced with a new one when this is exceeded.

## task_soft_time_limit
Task soft time limit in seconds.
The **SoftTimeLimitExceeded** exception will be raised when this is exceeded. For example, the task can catch this to clean up before the hard time limit comes:

```
app.conf.update(
    task_time_limit=100,
    task_soft_time_limit=60,
)
```
```
from celery.exceptions import SoftTimeLimitExceeded

@app.task
def mytask():
    try:
        return do_work()
    except SoftTimeLimitExceeded:
        cleanup_in_a_hurry()
```

## worker_concurrency
The number of concurrent worker processes/threads/green threads executing tasks.

If you’re doing mostly I/O you can have more processes, but if mostly CPU-bound, try to keep it close to the number of CPUs on your machine. If not set, the number of CPUs/cores on the host will be used.

## worker_prefetch_multiplier
Default: 4.
How many messages to prefetch at a time multiplied by the number of concurrent processes. The default is 4 (four messages for each process). The default setting is usually a good choice, however – if you have very long running tasks waiting in the queue and you have to start the workers, note that the first worker to start will receive four times the number of messages initially. Thus the tasks may not be fairly distributed to the workers.
To disable prefetching, set worker_prefetch_multiplier to 1. Changing that setting to 0 will allow the worker to keep consuming as many messages as it wants.

## task_ignore_result
Whether to store the task return values or not (tombstones). If you still want to store errors, just not successful return values, you can set task_store_errors_even_if_ignored.

```
>>> app.conf.update(
  task_ignore_result=True,
)

>>> result = add.delay(1, 1)
>>> print(result.get())

None
```

## task_store_errors_even_if_ignored
If set, the worker stores all task errors in the result store even if Task.ignore_result is on.

```
>>> app.conf.update(
  task_store_errors_even_if_ignored=True,
)

>>> result = add.delay(1, 1)
>>> print(result.get())
None

>>> result = do_exception_task.delay()
>>> print(result.get(propagate=False))
Exception Error
```

## task_acks_late
Late ack means the task messages will be acknowledged after the task has been executed, not just before (the default behavior).


# Signatures
You just learned how to call a task using the tasks delay method in the calling guide, and this is often all you need, but **sometimes you may want to pass the signature of a task invocation to another process or as an argument to another function.**
**A signature() wraps the arguments, keyword arguments, and execution options of a single task invocation in a way such that it can be passed to functions or even serialized and sent across the wire.**

You can create a signature for the add task using its name like this:
```
>>> from celery import signature
>>> signature('tasks.add', args=(2, 2), countdown=10)

tasks.add(2, 2)
```

or you can create one using the task’s signature method:
```
>>> add.signature((2, 2), countdown=10)
tasks.add(2, 2)
```

There’s also a shortcut using star arguments:
```
>>> add.s(2, 2)
tasks.add(2, 2)
```
Keyword arguments are also supported:
```
>>> add.s(2, 2, debug=True)
tasks.add(2, 2, debug=True)
```

Calling the signature will execute the task inline in the current process:
```
>>> add(2, 2)
4
>>> add.s(2, 2)()
4
```

## Partials

Specifying additional args, kwargs, or options to apply_async/delay creates partials:
Any arguments added will be prepended to the args in the signature:
```
>>> partial = add.s(2)          # incomplete signature
>>> partial.delay(4)            # 4 + 2
>>> partial.apply_async((4,))  # same
```

Any keyword arguments added will be merged with the kwargs in the signature, with the new keyword arguments taking precedence:
```
>>> s = add.s(2, 2)
>>> s.delay(debug=True)                    # -> add(2, 2, debug=True)
>>> s.apply_async(kwargs={'debug': True})  # same
```

Any options added will be merged with the options in the signature, with the new options taking precedence:
```
>>> s = add.signature((2, 2), countdown=10)
>>> s.apply_async(countdown=1)  # 
```

## Callbacks
Callbacks can be added to any task using the link argument to apply_async:
```
add.apply_async((2, 2), link=other_task.s())
```
The callback will only be applied if the task exited successfully, and it will be applied with the return value of the parent task as argument.

As I mentioned earlier, any arguments you add to a signature, will be prepended to the arguments specified by the signature itself!

If you have the signature:
```
>>> sig = add.s(10)
```
then sig.delay(result) becomes:
```
>>> add.apply_async(args=(result, 10))
```
…

Now let’s call our add task with a callback using partial arguments:
```
>>> add.apply_async((2, 2), link=add.s(8))
```
As expected this will first launch one task calculating 2 + 2, then another task calculating 4 + 8.

```
from tasks import sum
​
sum.apply_async((8,8), link=sum.s(10)) # Result of the first task is 16 so the second task will be called with 16 and 10
```

```
from tasks import sum, increase_counter
​
sum.apply_async((8,8), link=increase_counter.si()) # Calculate 8 + 8 and increase counter of sum task calls
```

## Immutability
Partials are meant to be used with callbacks, any tasks linked, or chord callbacks will be applied with the result of the parent task. Sometimes you want to specify a callback that doesn’t take additional arguments, and in that case you can set the signature to be immutable:
```
>>> add.apply_async((2, 2), link=reset_buffers.signature(immutable=True))
```
The .si() shortcut can also be used to create immutable signatures:
```
>>> add.apply_async((2, 2), link=reset_buffers.si())
```
Only the execution options can be set when a signature is immutable, so it’s not possible to call the signature with partial args/kwargs.

# The Primitives
Overview
* group : The group primitive is a signature that takes a list of tasks that should be applied in parallel.

* chain : The chain primitive lets us link together signatures so that one is called after the other, essentially forming a chain of callbacks.

* chord : A chord is just like a group but with a callback. A chord consists of a header group and a body, where the body is a task that should execute after all of the tasks in the header are complete.

## Simple chain
Here’s a simple chain, the first task executes passing its return value to the next task in the chain, and so on.
```
>>> from celery import chain

>>> # 2 + 2 + 4 + 8
>>> res = chain(add.s(2, 2), add.s(4), add.s(8))()
>>> res.get()
16
```
This can also be written using pipes:
```
>>> (add.s(2, 2) | add.s(4) | add.s(8))().get()
16
```

## Immutable signatures
Signatures can be partial so arguments can be added to the existing arguments, but you may not always want that, for example if you don’t want the result of the previous task in a chain.

In that case you can mark the signature as immutable, so that the arguments cannot be changed:
```
>>> add.signature((2, 2), immutable=True)
```
There’s also a .si() shortcut for this, and this is the preferred way of creating signatures:
```
>>> add.si(2, 2)
```
Now you can create a chain of independent tasks instead:
```
>>> res = (add.si(2, 2) | add.si(4, 4) | add.si(8, 8))()
>>> res.get()
16

>>> res.parent.get()
8

>>> res.parent.parent.get()
4
```

## Simple group
You can easily create a group of tasks to execute in parallel:
```
>>> from celery import group
>>> res = group(add.s(i, i) for i in range(10))()
>>> res.get(timeout=1)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Simple chord

The chord primitive enables us to add a callback to be called when all of the tasks in a group have finished executing. This is often required for algorithms that aren’t embarrassingly parallel:
```
>>> from celery import chord
>>> res = chord((add.s(i, i) for i in range(10)), xsum.s())()
>>> res.get()
90
```
The above example creates 10 task that all start in parallel, and when all of them are complete the return values are combined into a list and sent to the xsum task.

The body of a chord can also be immutable, so that the return value of the group isn’t passed on to the callback:
```
>>> chord((import_contact.s(c) for c in contacts),
...       notify_complete.si(import_id)).apply_async()
```
Note the use of .si above; this creates an immutable signature, meaning any new arguments passed (including to return value of the previous task) will be ignored.

Blow your mind by combining

Chains can be partial too:
```
>>> c1 = (add.s(4) | mul.s(8))

# (16 + 4) * 8
>>> res = c1(16)
>>> res.get()
160
```
this means that you can combine chains:
```
# ((4 + 16) * 2 + 4) * 8
>>> c2 = (add.s(4, 16) | mul.s(2) | (add.s(4) | mul.s(8)))

>>> res = c2()
>>> res.get()
352
```
Chaining a group together with another task will automatically upgrade it to be a chord:
```
>>> c3 = (group(add.s(i, i) for i in range(10)) | xsum.s())
>>> res = c3()
>>> res.get()
90
```
Groups and chords accepts partial arguments too, so in a chain the return value of the previous task is forwarded to all tasks in the group:
```
>>> new_user_workflow = (create_user.s() | group(
...                      import_contacts.s(),
...                      send_welcome_email.s()))
... new_user_workflow.delay(username='artv',
...                         first='Art',
...                         last='Vandelay',
...                         email='art@vandelay.com')
```
If you don’t want to forward arguments to the group then you can make the signatures in the group immutable:
```
>>> res = (add.s(4, 4) | group(add.si(i, i) for i in range(10)))()
>>> res.get()
<GroupResult: de44df8c-821d-4c84-9a6a-44769c738f98 [
    bc01831b-9486-4e51-b046-480d7c9b78de,
    2650a1b8-32bf-4771-a645-b0a35dcc791b,
    dcbee2a5-e92d-4b03-b6eb-7aec60fd30cf,
    59f92e0a-23ea-41ce-9fad-8645a0e7759c,
    26e1e707-eccf-4bf4-bbd8-1e1729c3cce3,
    2d10a5f4-37f0-41b2-96ac-a973b1df024d,
    e13d3bdb-7ae3-4101-81a4-6f17ee21df2d,
    104b2be0-7b75-44eb-ac8e-f9220bdfa140,
    c5c551a5-0386-4973-aa37-b65cbeb2624b,
    83f72d71-4b71-428e-b604-6f16599a9f37]>

>>> res.parent.get()
8
```
```
>>> res = chord(group(tasks.add.s(5, 5), tasks.sub.s(25, 10)))(tasks.tsum.s())
# or
>>> res = chord([tasks.add.s(5, 5), tasks.sub.s(25, 10)])(tasks.tsum.s())

>>> print(res.get())

# [10, 15] -> tsum([10, 15]) -> 25
25
```

# Signals

* before_task_publish : 

Dispatched before a task is published. Note that this is executed in the process sending the task.

* after_task_publish

Dispatched when a task has been sent to the broker. Note that this is executed in the process that sent the task

```
@app.task
def do_signal_task():
    time.sleep(5)
    return "work..."


@signals.before_task_publish.connect(sender="tasks.do_signal_task")
def print_before_task_publish(sender=None, **kwargs):
    print("befor task published")


@signals.after_task_publish.connect(sender="tasks.do_signal_task")
def print_after_task_publish(sender=None, **kwargs):
    print("after task published")


>>> do_signal_task.delay()

befor task published
after task published
work...
```

* task_prerun

Dispatched before a task is executed.

* task_postrun

Dispatched after a task has been executed.

```
@signals.task_prerun.connect(sender=do_signal_task)
def print_task_prerun(sender=None, **kwargs):
    print("befor task run")


@signals.task_postrun.connect(sender=do_signal_task)
def print_task_postrun(sender=None, **kwargs):
    print("after task run")


>>> tasks.do_signal_task.delay().get()

[: WARNING/ForkPoolWorker-4] befor task run
[: INFO/ForkPoolWorker-4] Task tasks.do_signal_task[96e54373-ebd9-44fc-bf97-47493dfbecd0] succeeded in 0 003380734999154811s: 'work...'
[: WARNING/ForkPoolWorker-4] after task run

```


* task_retry

Dispatched when a task will be retried

* task_success

Dispatched when a task succeeds.

* task_failure

Dispatched when a task fails.
 
* task_internal_error

Dispatched when an internal Celery error occurs while executing the task.

* task_received

Dispatched when a task is received from the broker and is ready for execution.

* task_revoked

Dispatched when a task is revoked/terminated by the worker.

* task_unknown

Dispatched when a worker receives a message for a task that’s not registered.

* task_rejected

Dispatched when a worker receives an unknown type of message to one of its task queues.

# Periodic Tasks

Introduction

celery beat is a scheduler; It kicks off tasks at regular intervals, that are then executed by available worker nodes in the cluster.

By default the entries are taken from the beat_schedule setting, but custom stores can also be used, like storing the entries in a SQL database.

You have to ensure only a single scheduler is running for a schedule at a time, otherwise you’d end up with duplicate tasks. Using a centralized approach means the schedule doesn’t have to be synchronized, and the service can operate without using locks

## Available Fields*task

The name of the task to execute.
* schedule

The frequency of execution.

This can be the number of seconds as an integer, a timedelta, or a crontab. You can also define your own custom schedule types, by extending the interface of schedule.

* args

Positional arguments (list or tuple).

* kwargs

Keyword arguments (dict).

* options

Execution options (dict).

This can be any argument supported by apply_async() – exchange, routing_key, expires, and so on.

* relative

If relative is true timedelta schedules are scheduled “by the clock.” This means the frequency is rounded to the nearest second, minute, hour or day depending on the period of the timedelta.

By default relative is false, the frequency isn’t rounded and will be relative to the time when celery beat was started.

## Crontab schedules

If you want more control over when the task is executed, for example, a particular time of day or day of the week, you can use the crontab schedule type:

```
from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}
```

The syntax of these Crontab expressions are very flexible.

* crontab() : Execute every minute.

* crontab(minute=0, hour=0) : Execute daily at midnight.

* crontab(minute=0, hour='*/3') : Execute every three hours: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.

* crontab(minute=0, hour='0,3,6,9,12,15,18,21') : Same as previous.

* crontab(minute='*/15') : Execute every 15 minutes.

* crontab(day_of_week='sunday') : Execute every minute (!) at Sundays.

* crontab(minute='*', hour='*', day_of_week='sun') : Same as previous. 

* crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri') : Execute every ten minutes, but only between 3-4 am, 5-6 pm, and 10-11 pm on Thursdays or Fridays.

* crontab(minute=0, hour='*/2,*/3') : Execute every even hour, and every hour divisible by three. This means: at every hour except: 1am, 5am, 7am, 11am, 1pm, 5pm, 7pm, 11pm

* crontab(minute=0, hour='*/5') : Execute hour divisible by 5. This means that it is triggered at 3pm, not 5pm (since 3pm equals the 24-hour clock value of “15”, which is divisible by 5).

* crontab(minute=0, hour='*/3,8-17') : Execute every hour divisible by 3, and every hour during office hours (8am-5pm).

* crontab(0, 0, day_of_month='2') : Execute on the second day of every month.

* crontab(0, 0, day_of_month='2-30/2') : Execute on every even numbered day.

* crontab(0, 0, day_of_month='1-7,15-21') : Execute on the first and third weeks of the month.

* crontab(0, 0, day_of_month='11', month_of_year='5') : Execute on the eleventh of May every year.

* crontab(0, 0, month_of_year='*/3') : Execute every day on the first month of every quarter.

## Starting the Scheduler
To start the celery beat service:
```
$ celery -A proj beat
```
You can also embed beat inside the worker by enabling the workers -B option, this is convenient if you’ll never run more than one worker node, but it’s not commonly used and for that reason isn’t recommended for production use:
```
$ celery -A proj worker -B
```
Beat needs to store the last run times of the tasks in a local database file (named celerybeat-schedule by default), so it needs access to write in the current directory, or alternatively you can specify a custom location for this file:
```
$ celery -A proj beat -s /home/celery/var/run/celerybeat-schedule
```