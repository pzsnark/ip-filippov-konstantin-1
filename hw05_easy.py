# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


a = [random.randint(1, 10) for i in range(1, 10)]
b = [i ** 2 for i in a]
print(a, b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

import random


fruit_list = ["яблоко", "банан", "груша", "апельсин", "мандарин", "лимон", "персик", "абрикос", "ананас"]
print(len(fruit_list))
fruit1 = [fruit_list[(random.randint(0, len(fruit_list) - 1))] for _ in range(1, 5)]
fruit2 = [fruit_list[(random.randint(0, len(fruit_list) - 1))] for _ in range(1, 5)]

inter = list(set(fruit1) & set(fruit2))  # оператор амперсанд аналог intersection (с ограничениями)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random


def check(n):
    if float(n) % 3 == 0 and n >= 0 and float(n) % 4 != 0:
        return True
    else:
        return False


a = [random.randint(-10, 10) for i in range(1, 10)]
b = [a[i] for i in range(len(a)) if check(a[i]) == True]
print(a)
print(b)