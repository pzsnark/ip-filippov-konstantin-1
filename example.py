class Property(object):

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if self.fget is None:
            raise AttributeError("нечитаемый атрибут")

        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("не могу установить атрибут")

        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("не могу удалить атрибут")

        self.fdel(obj)


class Example:

    x = 0

    def area(self):
        self.x = self.x ** 2
        return self.x
    area = Property(area)

    @area.fset
    def area(self, value):
        self.x = value


n = Example(5)
print(n.area)

