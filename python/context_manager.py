# Managing Resources: In any programming language, the usage of resources like file operations or database connections is very common.
# But these resources are limited in supply. Therefore, the main problem lies in making sure to release these resources after usage.
# If they are not released then it will lead to resource leakage and may cause the system to either slow down or crash.
# It would be very helpful if users have a mechanism for the automatic setup and teardown of resources.
# In Python, it can be achieved by the usage of context managers which facilitate the proper handling of resources.
# The most common way of performing file operations is by using the keyword as shown below:

# .__enter__() is called by the with statement to enter the runtime context.
# .__exit__() is called when the execution leaves the with code block.


file = open("hello.txt", "w")
try:
    file.write("Hello, World!")
finally:
    file.close()


with open("test.txt") as f:
    data = f.read()

# --------------------------

file_descriptors = []
for x in range(100000):
    file_descriptors.append(open("test.txt", "w"))

# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/context_manager.py", line 16, in <module>
# OSError: [Errno 24] Too many open files: 'test.txt'


# --------------------------


class ContextManager:
    def __init__(self):
        print("init method called")

    def __enter__(self):
        print("enter method called")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit method called")


with ContextManager() as manager:
    print("with statement block")

# init method called
# enter method called
# with statement block
# exit method called


# --------------------------


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with FileManager("test.txt", "w") as f:
    f.write("Test")


# --------------------------
