# for i in range(0, 8, 2):
#       print(i)
# abs(-2)  # вывод абсолютной величины

# print(max([1, 2, 3, 4, 5])) # максимальный элемент последовательности, аналогична min

# x = round(2.56, 1)  # округление до N знаков
# x = sum([2.56, 1, 12])  # суммирует все элементы последовательности
# x = type('')  # возвращает тип объекта
# print(x)
# x = [1, 2, 3, 4, 5]
# for i, y in enumerate(x):  # возвращает пару индекс и значение
#     print(i, y)

def summ(a, b):
    """
    документирование функции
    """
    return a + b
x = 5
y = 6
s = summ(x, y)
print(s)

# f = lambda x: x ** 2
# print(f(4))
# print((lambda x: x ** 2)(4))

# x = 5  # глобальная переменная, доступна в любом месте данного модуля(файла)
# def outside():
#     y = 10  # доступна в теле данной функции + во всех вложенных
#     def inside():
#         z = 15
#         print("inside x: {}, y: {}, z: {}".format(x, y. z))
#     inside()
#     print("outside x: {}, y: {}, z: {}".format(x, y, "z недоступна"))
# x = 5
# def wrapper():
#     def test1():
#         x = 10  # локальная переменная x перекрывает видимость глобальной х
#         print("test1 x =", x)
#     def test2():
#         print("test2 x =", x)
# # x = 22 # ошибка, выше используем переменную объявленную позднее
#     def test3():
#         global x # инструкция global - поиск переменной в глобальной области
#                  # есть инструкция nonlocal - поиск переменной в объемлющей функции
#         print("test3 x =", x)
#         x = 25
#     test1()
#     test2()
#     test3()
# wrapper()
# print("after wrapper x =", x)

# def average(*args):  # вычисляем среднее арифметическое
#     summ = 0
#     for arg in args:
#         summ += arg
#     return summ/len(args)
# print(average(1, 2, 3))

# def print_info(**kwargs):
#     print("You name is %s %s. You age is %s. And your address is: %s"%
#                (kwargs["name"],kwargs["surname"],kwargs["age"],kwargs["adress"]))
# print_info(name="Василий", surname="Иванов", age="12", adress="ул.Белана 22")

# def welcome(name="Инкогнито"):
#     print("Приветствую тебя, %s"%(name))
# # def print(*args, sep='', end="\n", file = None):
# print("Иван", "Иванович", "Иванов", sep="//", end = "!!!")

# a = [1, 2, 4]
# b = [3, 4]
# c = [5, 6, 0]
# print(zip(a, b, c))
# for i in zip(a, b, c):
#     print(i)

# # применяет функцию к каждому элементу последовательности, результат функции возвращает в виде итератора
# print(list(map(lambda x: x*x, [2, 5, 12, -2])))  # использовать для домашки
# print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
# print(list(filter(len, ["", "not null", "bla", "10"])))
# # filter() отбрасывает те элементы, для которых функция возвращает False

import os
path = "files/text.txt"  # не самый хороший способ задания пути
path = os.path.join("files", 'text.txt')  # хороший кроссплатформенный способ
f = open(path, "r", encoding="UTF-8")
# считываем всю информацию из файла в виде списка строк
print(f.readlines())
f.close()

my_file = open("some.txt", "w")
my_file.write("Some text")
my_file.close

# наиболее правильный способ работы с файлами
# по окончанию инструкции файл будет гарантировано закрыт , даже если произойдет ошибка
with open(path, "r", encoding="UTF-8") as f:
    print(f.readlines())