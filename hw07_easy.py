# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt


class Triangle:
    def __init__(self, xa, ya, xb, yb, xc, yc):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.xc = xc
        self.yc = yc
        self.c = sqrt(((xb - xa) ** 2) + ((yb - ya) ** 2))
        self.b = sqrt(((xc - xa) ** 2) + ((yc - ya) ** 2))
        self.a = sqrt(((xc - xb) ** 2) + ((yc - yb) ** 2))
        self.p = (self.a + self.b + self.c) / 2
        self.ha = (2 * sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / self.a
        self.hb = (2 * sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / self.b
        self.hc = (2 * sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / self.c

    def len_side(self):
        print('Длины сторон треугольника: ', self.a, self.b, self.c)

    def perimeter(self):
        print('Периметр треугольника: ', self.a + self.b + self.c)

    def square(self):
        return abs(((self.xa - self.xc) * (self.yb - self.yc)) - ((self.xb - self.xc) * (self.ya - self.yc))) / 2

    def square_geron(self):
        return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    def height(self):
        print('Высота с точки А: ', self.ha)
        print('Высота с точки B: ', self.hb)
        print('Высота с точки C: ', self.hc)


print('Введите координаты точки A')
xa = float(input('x: '))
ya = float(input('y: '))
print('Введите координаты точки B')
xb = float(input('x: '))
yb = float(input('y: '))
print('Введите координаты точки C')
xc = float(input('x: '))
yc = float(input('y: '))

n = Triangle(xa, ya, xb, yb, xc, yc)

n.len_side()
n.height()
n.perimeter()
print("Площадь треугольника по вершинам: ", n.square())
print("Площадь треугольника по формуле Герона: ", n.square_geron())

