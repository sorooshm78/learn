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

## Python Programs
If you want to create a program that you can run repeatedly, put statements in a text file.
For example:
```
# hello.py
print('Hello World')
```

To execute the hello.py file, provide the filename to the interpreter as follows:
```
shell % python3 hello.py
Hello World
shell %
```
It is common to use #! to specify the interpreter on the first line of a program, like this:
```
#!/usr/bin/env python3
print('Hello World')
```
On UNIX, if you give this file execute permissions (for example, by chmod +x
hello.py), you can run the program by typing hello.py into your shell.

