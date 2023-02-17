# class Data:
#     def __new__(cls):
#         cls.user = None
#         print("new")
#         return super(Data, cls).__new__(cls)

#     def __init__(self, user):
#         self.user = user
#         print("init")


# d1 = Data("user1")
# d2 = Data("user2")
# d3 = Data("user3")


class A(object):
    def __new__(cls):
        cls.user = None
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self):
        # self.user = user
        print("Init is called")


A()
A()
