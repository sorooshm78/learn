# Python Basics

## Running Python
Python programs are executed by an interpreter. There are many different environments
in which the Python interpreter might run —an IDE, a browser, or a terminal window.
However, underneath all that, the core of the interpreter is a text-based application that
can be started by typing python in a command shell such as bash

```
>>> 6000 + 4523.50 + 134.25
10657.75
>>> _ + 8192.75
18850.5
>>>

```
When you use Python interactively, the variable _ holds the result of the last operation.
This is useful if you want to use that result in subsequent statements. This variable only
gets defined when working interactively, so don’t use it in saved programs.
You can exit the interactive interpreter by typing quit() or the EOF (end of file)
character. On UNIX, EOF is Ctrl+D; on Windows, it’s Ctrl+Z.