# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt


def len_size(a, b, c, d):
    return sqrt(((b - a) ** 2) + ((d - c) ** 2))


class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay

        self.bx = bx
        self.by = by

        self.cx = cx
        self.cy = cy

        self.a = len_size(cx, bx, cy, by)
        self.b = len_size(cx, ax, cy, ay)
        self.c = len_size(ax, bx, ay, by)
        print(self.a, self.b, self.c)

        self.p = (self.a + self.b + self.c) / 2
        self.ha = (2 * sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / self.a
        self.hb = (2 * sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / self.b
        self.hc = (2 * sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / self.c

    def len_side(self):
        print('Длины сторон треугольника: ', self.a, self.b, self.c)

    def perimeter(self):
        print('Периметр треугольника: ', self.a + self.b + self.c)

    def square(self):
        return abs(((self.ax - self.cx) * (self.by - self.cy)) - ((self.bx - self.cx) * (self.ay - self.cy))) / 2

    def square_geron(self):
        return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    def height(self):
        print('Высота с точки А: ', self.ha)
        print('Высота с точки B: ', self.hb)
        print('Высота с точки C: ', self.hc)


# print('Введите координаты точки A')
# ax = float(input('x: '))
# ay = float(input('y: '))
# print('Введите координаты точки B')
# bx = float(input('x: '))
# by = float(input('y: '))
# print('Введите координаты точки C')
# cx = float(input('x: '))
# cy = float(input('y: '))

ax = -4
ay = 7
bx = -1
by = 2
cx = -7
cy = -4

n = Triangle(ax, ay, bx, by, cx, cy)

# n.len_side()
n.height()
n.perimeter()
print("Площадь треугольника по вершинам: ", n.square())
print("Площадь треугольника по формуле Герона: ", n.square_geron())

