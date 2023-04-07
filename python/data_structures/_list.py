import ctypes


class SMList:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.array = (self.capacity * ctypes.py_object)()

    def append(self, item):
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.length] = item
        self.length += 1

    def _resize(self, new_cap):
        new_arr = (new_cap * ctypes.py_object)()
        for idx in range(self.length):
            new_arr[idx] = self.array[idx]
        self.array = new_arr
        self.capacity = new_cap

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        return self.array[idx]

    def __str__(self):
        output = ""
        for i in range(self.length):
            output += f" {self.array[i]} "

        return f"[{output}]"


l = SMList()

l.append(0)
l.append(1)
l.append(2)
l.append(3)


print(l)

print(l[0])
print(l[1])
print(l[2])
print(l[3])

# [ 0  1  2  3 ]
# 0
# 1
# 2
# 3
