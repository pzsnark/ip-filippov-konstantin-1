"""
Ошибки (номера строк через пробел): 15 18 19
"""


def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.

    Исключения:
        - ValueError: вычисление не возможно.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Одно или оба числа не являются положительным/и.")


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as err:
    print("Ошибка:", err, "Проверьте введенные числа.")
except Exception as err:
    print("Ошибка:", err)
