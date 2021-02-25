# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt


def len_size(a, b, c, d):
    return sqrt(((b - a) ** 2) + ((d - c) ** 2))


class Trap:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay

        self.bx = bx
        self.by = by

        self.cx = cx
        self.cy = cy

        self.cx = dx
        self.cy = dy

        self.ab = len_size(bx, ax, by, ay)
        self.bc = len_size(cx, bx, cy, by)
        self.cd = len_size(dx, cx, dy, cy)
        self.da = len_size(dx, ax, dy, ay)
        self.ac = len_size(cx, ax, cy, ay)
        self.bd = len_size(dx, bx, dy, by)

        if self.is_isosceles:
            print('Фигура является трапецией')
        else:
            print('Фигура не является трапецией')

    @property
    def is_isosceles(self):
        if self.ac == self.bd:
            return True
        else:
            return False

    def perimeter(self):
        if self.is_isosceles:
            print('Периметр трапеции: ', self.ab + self.bc + self.cd + self.da)
        else:
            print('Это не трапеция')

    def area(self):
        if self.is_isosceles:
            print('Площадь трапеции: ', (self.ab + self.cd / 4) * sqrt(4 * (self.bc ** 2) - ((self.ab - self.cd) ** 2)))
        else:
            print('Это не трапеция')


ax = 1
ay = 1
bx = 2
by = 6
cx = 7
cy = 6
dx = 8
dy = 1

n = Trap(ax, ay, bx, by, cx, cy, dx, dy)

n.check()
n.perimeter()
n.area()
