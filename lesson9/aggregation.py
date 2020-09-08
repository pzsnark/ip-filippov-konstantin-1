class A:
    def f(self):
        print("A: вызываем метод f")

    def g(self):
        print("A: вызываем метод g")


class C:
    def __init__(self):
        self.A = A()

    def f(self):
        return self.A.f()

    def g(self):
        return self.A.g()


c = C()
c.f()  # вызываем метод f
c.g()  # вызываем метод g