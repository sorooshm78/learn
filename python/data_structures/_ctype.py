import ctypes


# class ctypes.py_object
#     Represents the C PyObject* datatype. Calling this without an argument creates a NULL PyObject* pointer.

# -------------------------------------

obj = ctypes.py_object()

print(obj)
print(type(obj))
# py_object(<NULL>)
# <class 'ctypes.py_object'>

# -------------------------------------

obj = ctypes.py_object(10)

print(obj)
print(type(obj))
# py_object(10)
# <class 'ctypes.py_object'>

# -------------------------------------

obj = ctypes.py_object()

print(obj)
print(type(obj))
print(obj.value)

# py_object(<NULL>)
# <class 'ctypes.py_object'>
# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/data_structures/_py_object.py", line 31, in <module>
#     print(obj.value)
# ValueError: PyObject is NULL


# -------------------------------------

obj = ctypes.py_object(10)

print(obj)
print(type(obj))
print(obj.value)

# py_object(10)
# <class 'ctypes.py_object'>
# 10

# -------------------------------------

obj = ctypes.py_object(10)

print(obj)
print(type(obj))
print(obj.value)

# py_object(10)
# <class 'ctypes.py_object'>
# 10

obj.value = 5

print(obj)
print(type(obj))
print(obj.value)
# py_object(5)
# <class 'ctypes.py_object'>
# 5

# -------------------------------------

obj = ctypes.py_object(10)

print(obj)
print(obj.value)
# py_object(10)
# 10

# change byte size
obj.value = "string"

print(obj)
print(obj.value)
# py_object('string')
# string

# -------------------------------------

obj = ctypes.py_object(10)

print(obj)
print(obj.value)
print(id(obj))
# py_object(10)
# 10
# 140128685994944

obj.value = "string"

print(obj)
print(obj.value)
print(id(obj))
# py_object('string')
# string
# 140128685994944

# -------------------------------------

arr = (10 * ctypes.py_object)()

print(arr)
print(type(arr))
# <__main__.py_object_Array_10 object at 0x7f7a39a600c0>
# <class '__main__.py_object_Array_10'>

# -------------------------------------

arr = (5 * ctypes.py_object)()

arr[0] = 0
arr[1] = 1
arr[2] = 2
arr[3] = 3
arr[4] = 4

print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print(arr[5])
# <__main__.py_object_Array_5 object at 0x7fe26de8fb40>
# 0
# 1
# 2
# 3
# 4
# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/data_structures/_py_object.py", line 136, in <module>
#     print(arr[5])
# IndexError: invalid index

# -------------------------------------

arr = (5 * ctypes.py_object)()

arr[0] = 0
arr[1] = 1
arr[2] = "str"
arr[3] = True
arr[4] = 1.0

print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
# <__main__.py_object_Array_5 object at 0x7f94c5117b40>
# 0
# 1
# str
# True
# 1.0

# -------------------------------------

# create a 3-int array
int_arr = (3 * ctypes.c_int)()
int_arr[0] = 1
int_arr[1] = 2
int_arr[2] = 3

print(int_arr)
print(int_arr[0])
print(int_arr[1])
print(int_arr[2])
# <__main__.c_int_Array_3 object at 0x7f1619d073c0>
# 1
# 2
# 3

# -------------------------------------

int_arr = (3 * ctypes.c_int)()
int_arr[0] = 1
int_arr[1] = 2
int_arr[2] = "str"

# Traceback (most recent call last):
#   File "/home/sm/src/learn/python/data_structures/_ctype.py", line 193, in <module>
#     int_arr[2] = "str"
# TypeError: 'str' object cannot be interpreted as an integer

# -------------------------------------

# create a 3-(20-char array) array
char_arr = ((ctypes.c_char * 20) * 3)()
char_arr[0].value = b"mehran"
char_arr[1].value = b"soroosh"
char_arr[2].value = b"gholi"

print(char_arr[0])
print(char_arr[1])
print(char_arr[2])
# <__main__.c_char_Array_20 object at 0x7f6b0fda0140>
# <__main__.c_char_Array_20 object at 0x7f6b0fda0140>
# <__main__.c_char_Array_20 object at 0x7f6b0fda0140>

# -------------------------------------

# create a 3-(20-char array) array
char_arr = ((ctypes.c_char * 20) * 3)()
char_arr[0].value = b"mehran"
char_arr[1].value = b"soroosh"
char_arr[2].value = b"gholi"

print(char_arr[0].value)
print(char_arr[1].value)
print(char_arr[2].value)
# b'mehran'
# b'soroosh'
# b'gholi'
