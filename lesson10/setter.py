# class C:
#     _x = None
#
#     def __init__(self):
#         self._x = None
#
#     @property
#     def x(self):
#         """I'm the 'x' property"""
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         del self._x

# как работает декоратор @property
class C:
    _x = None


    def _get_x(self):
        """I'm the 'x' property"""
        return self._x

    def _set_x(self, value):
        self._x = value

    def _del_x(self):
        del self._x

    x = property(_get_x, _set_x, _del_x)

test = C()
test.x = 12
print(test.x)
del test.x
print(test.x)