# n1 = 2
# n2 = n1
# n1 = 4
# неизменяемые объекты int float complex str tuple - Immutable objects
# Изменяемые объекты set list dict - Mutable objects
# print(f"n1 = {n1} n2 = {n2}")
# sp1 = [1, 2, 3]
# sp2 = sp1
# sp2.append(4)
# print("sp1 =", sp1, "sp2 =", sp2)

# def modify(lst):
#     lst.append("new")
#     return lst
# my_list = [1, 2, 3]
# mod_list = modify(my_list)  # my_list[:] - копия объекта
# # функция вернула измененный список
# print("mod_list =", mod_list)
# # но исходный код тоже изменился, подобное неявное поведение нежелательно для функций
# print("my_list =", my_list)
#
# my_list = [1, -2, -4, 0, 5, -2]
# # удаляем все отрицательные элементы
# for el in my_list:
#     if el < 0:
#         my_list.remove(el)
# # думаю это не тот результат который ожидался
# print("1) my_list after remove -->", my_list)
#
# for el in my_list[:]:
#     if el < 0:
#         my_list.remove(el)
# # итерируем по копии, удаляем из оригинала
# print("1) my_list after remove -->", my_list)


# изучить еще раз
import copy

# sp = [[2, 3], [4, 6, [7, 8]]]
# sp_copy = copy.deepcopy(sp)
# sp_copy = sp[:]
# print("sp_copy =", sp_copy)
# print("sp", sp)
# sp[0].append(10)
# sp_copy[0].append(12)
# print("sp", sp)
# print("sp_copy", sp_copy)

# matrix = \
#         [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
# print("matrix =", matrix)
#
# # красиво выводим
# print("matrix =")
# for line in matrix:
#     print(line)
#
# print("--- for in ---")
# for i, line in enumerate(matrix):
#     for j, el in enumerate(line):
#         print("matrix[{}][{}] = {}".format(i, j, matrix[i][j]))

# people = {}
# if people.get("name"):
#     name = people["name"]
# else:
#     name = "Безымянный"
# print(name)

# тернарный оператор конструкция -- истина if условие else иначе
# d = {"name": "Вася"}
# print(d.get("name") if d.get("name") else "Безымянный")

# is оператор "является, проверка на ссылку
# c = [1, 2]
# d = c
# e = [1, 2]
# c is d
# True
# c is e
# False

# import random
# lst_g = [random.randint(-10, 10) for _ in range(10)]
# print("lst_g", lst_g)
# # отбрасываем все отрицательные элементы списка
# only_positive = [el for el in lst_g if el >= 0]
# print("only_positive =", only_positive)

# генератор словаря
# keys = "abcdefg"
# values = range(10)
# dict_g = {key: value for key, value in zip(keys, values)}
# print("dict_g =", dict_g)
# # более простой пример создания словаря генератором
# dict2_g = {el: el+4 for el in [1, 4, 6, 8]}
# print("dict2_g =", dict2_g)

# import re
#
# string = "This is a simple test message for test"
# string2 = "test"
# pattern1 = "test$"
# pattern2 = "^test"
# pattern3 = "^test$"
# print(re.search(pattern1, string) is None)
# print(re.match(pattern2, string) is None)
# print(re.match(pattern3, string) is None)
# print(re.match(pattern3, string2) is None)

# import re
# string = "This is a simple test message for test"
# found = re.findall(r"test", string)
# print(found)

# import re
# pattern = '[0-9]+k'
# string = "If 300 spartsns werw so brave, so 500 spartans" \
#     "could destroy more than 10k warriors of Darius', but 15k and even 20k"
# print(re.findall(pattern, string))

import re

html = '<p style="margin-left: 10px;">sdfsd'
pattern = "<[^>]+>"
print(re.findall(pattern, html))
