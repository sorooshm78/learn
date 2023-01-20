def add():
    cdef int num = 0
    cdef int i = 0 
    for i in range(1000000):
        num += i
    
    return num