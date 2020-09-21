# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a = 1
    b = 1
    lst = []
    for i in range(m - 2):
        a, b = b, a + b
        print(i, a)
        lst.append(a) if i >= n - 3 else None
    return lst


print(fibonacci(5, 12))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(a):
    n = len(a)
    for e in range(0, n - 1):
        for i in range(0, n - e - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def alter_filter(func, a):
    lst = []
    for i in a:
        if func(i) and func is not None:
            lst.append(i)
    return iter(lst)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math
import random


def distance(p1, p2):
    return round(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2), 2)


x = []
y = []
for _ in range(4):
    x.append(random.randint(0, 10))
    y.append(random.randint(0, 10))
# фигура является параллелограмом, если две пары разных сторон имеют равные длины
if distance((x[0], y[0]), (x[2], y[2])) == distance((x[1], y[1]), (x[3], y[3])) \
        and distance((x[0], y[0]), (x[1], y[1])) == distance((x[2], y[2]), (x[3], y[3])):
    print("Верно")
else:
    print("Не верно")