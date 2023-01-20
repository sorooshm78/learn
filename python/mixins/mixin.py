class Father:
    def query(self):
        # super().query()
        print("father")


class Mixin2:
    def query(self):
        super().query()
        print("MIXIN2")


class Mixin1:
    def query(self):
        super().query()
        print("MIXIN1")


# class Child(Mixin1, Mixin2, Father):
#     def query(self):
#         super().query()
#         print("child")


class Child(Mixin1):
    def query(self):
        super().query()
        print("child")


c = Child()
c.query()
