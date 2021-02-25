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

        self.p = (self.a + self.b + self.c) / 2

        self.ha = (2 * self.area_geron) / self.a
        self.hb = (2 * self.area_geron) / self.b
        self.hc = (2 * self.area_geron) / self.c

    @property
    def len_side(self):
        return self.a, self.b, self.c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return abs(((self.ax - self.cx) * (self.by - self.cy)) - ((self.bx - self.cx) * (self.ay - self.cy))) / 2

    @property
    def area_geron(self):
        return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    @property
    def height(self):
        return self.ha, self.hb, self.hc


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

    @property
    def perimeter(self):
        if self.is_isosceles:
            return self.ab + self.bc + self.cd + self.da
        else:
            print('Это не трапеция')

    @property
    def area(self):
        if self.is_isosceles:
            return (self.ab + self.cd / 4) * sqrt(4 * (self.bc ** 2) - ((self.ab - self.cd) ** 2))
        else:
            print('Это не трапеция')


# выполняем

example_tri = Triangle(-4, 7, -1, 2, -7, -4)
example_trap = Trap(1, 1, 2, 6, 7, 6, 8, 1)


print("Высоты треугольника: ", example_tri.height)
print("Периметр треугольника: ", example_tri.perimeter)
print("Площадь треугольника по вершинам: ", example_tri.area)
print("Площадь треугольника по формуле Герона: ", example_tri.area_geron)

print("Это трапеция? ", example_trap.is_isosceles)
print("Периметр трапеции: ", example_trap.perimeter)
print("Площадь трапеции", example_trap.area)
