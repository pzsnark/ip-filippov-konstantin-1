
__author__ = 'Филиппов Константин Николаевич'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...
import sys
name = "Konstantin"
age = int(input("Введите возраст:"))
age2 = age - 18
print("Значение:", age2)
if age2 > 0:
    text2 = "старше"
elif age2 == 0:
    print("Константину 18 лет")
    sys.exit()
else:
    text2 = "младше"
age2 = abs(age2)
if age2 >= 5 and age2 <= 20:
    text = "лет"
else:
    if (age2 % 10) == 1:
        text = "год"
    elif (age2 % 10) >= 2 and (age2 % 10) <= 4:
        text = "года"
    else:
        text = "лет"
print("Константин на", abs(age2), text, text2, "18")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...
a = input("Введите значение переменной а:")
b = input("Введите значение переменной b:")
a, b = b, a
print("Значение а:", a)
print("Значение b:", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...
# https://www.berdov.com/docs/equation/quadratic_equations/
import math
import sys
a = int(input("Введите первый коэффициент а:"))
b = int(input("Введите второй коэффициент b:"))
c = int(input("Введите свободный член c:"))
if a == 0:
    sys.exit("a не должно равняться нулю")

# вычисляем дискриминант по формуле D = b2 − 4ac
d = (b ** 2) - (4 * a * c)
print("Дискриминант =", d)
if d < 0:
    print("Корней нет")
elif d == 0:
    x1 = -b / (2 * a)
    print("x1 = ", x1)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)



