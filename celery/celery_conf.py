from kombu import Queue, Exchange


default_exchange = Exchange("default", type="direct")
work_exchange = Exchange("work", type="direct")

task_queues = {
    Queue(name="default", exchange=default_exchange, routing_key="default"),
    Queue(name="math", exchange=work_exchange, routing_key="math"),
    Queue(name="long", exchange=work_exchange, routing_key="long"),
}

task_default_queue = "default"
task_default_exchange = "default"
task_default_routing_key = "default"


task_routes = {
    "tasks.add": {"queue": "math"},
    "tasks.long_task": {"queue": "long"},
}
