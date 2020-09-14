from abc import ABCMeta, abstractmethod, abstractproperty


class Foo(metaclass=ABCMeta):
    @abstractmethod
    def spam(self, a, b):
        pass
    @abstractproperty
    def name(self):
        pass


class Grok:
    def spam(self, a, b):
        print("Grok.spam")


Foo.register(Grok)  # зарегистрирует Grok, как наследующий абстрактный базовый класс Foo

# f = Foo()


class Account(object):
    __slots__ = ("name", "balance", "x")  # ограничения по аттрибутам
    ...


acc = Account()
acc.x = 13