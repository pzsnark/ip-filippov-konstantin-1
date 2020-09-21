class DocMeta(type):
    def __init__(self, clsname, bases, clsdict):
        for key, value in clsdict.items():
            # пропустить специальные и частные методы
            if key.startswith("__"): continue

            # пропустить любые невызываемые объекты
            if not hasattr(value, "__call__"): continue

            # проверить наличие строки документирования
            if not getattr(value, "__doc__"):
                raise TypeError("%s must have a docstring" % key)

        type.__init__(self, clsname, bases, clsdict)


class Documented(metaclass=DocMeta):
    pass


class Foo(Documented):
    def spam(self, a, b):
        """метод spam делает что-то"""
        pass

    def boo(self):
        print("A little problem")
