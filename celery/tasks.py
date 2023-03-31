from celery import Celery
import time

BROKER_URL = "redis://localhost:6379/0"

app = Celery(
    main="tasks",
    broker=BROKER_URL,
)


@app.task
def add(x, y):
    return x + y


# Run Celery
# celery --app tasks worker --loglevel INFO
# celery -A tasks worker -l INFO


# Calling Tasks
# The API defines a standard set of execution options, as well as three methods:
#   - apply_async(args[, kwargs[, …]])
#       Sends a task message.
#   - delay(*args, **kwargs)
#       Shortcut to send a task message, but doesn’t support execution options.


# Countdown
# The task is guaranteed to be executed at some time after the specified date and time, but not necessarily at that exact time
# this takes at least 3 seconds to return
# >>> result = add.apply_async((2, 2), countdown=3)
# >>> result.get()


# Expiration
# The expires argument defines an optional expiry time, either as seconds after task publish, or a specific date and time using datetime:
# >>> # Task expires after one minute from now.
# >>> add.apply_async((10, 10), expires=60)
# >>> # Also supports datetime
# >>> from datetime import datetime, timedelta
# >>> add.apply_async((10, 10), kwargs,
# ...                 expires=datetime.now() + timedelta(days=1)
# When a worker receives an expired task it will mark the task as REVOKED (TaskRevokedError).
