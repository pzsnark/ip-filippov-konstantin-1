from math import sqrt
from abc import ABC, abstractmethod
# a = {'x': 4, 'y': 7}
# b = {'x': 7, 'y': 4}


class Figure(ABC):
    """Абстрактный класс для геометрических фигур"""

    @staticmethod
    def side_lengths(a, b):
        return sqrt(((b['x'] - a['x']) ** 2) + ((b['y'] - a['y']) ** 2))

    @property
    def perimeter(self):
        return sum(self.sides)

    @property
    def area(self):
        return


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.side_a = self.side_lengths(b, c)
        self.side_b = self.side_lengths(a, c)
        self.side_c = self.side_lengths(a, b)
        self.sides = [self.side_a, self.side_b, self.side_c]


tri = Triangle({'x': 4, 'y': 7}, {'x': 1, 'y': 2}, {'x': 7, 'y': 4})
print(tri.side_a, tri.side_b, tri.side_c)
print(tri.perimeter)
