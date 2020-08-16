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
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print("x1 = ", x1)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
