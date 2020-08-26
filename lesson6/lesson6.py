# f = open("1.txt")
# ints = []
# try:
#     for line in f:
#         ints.append(int(line))
# except ValueError as ve:
#     print("Это не число, выходим {0}".format(ve))
# except Exception:
#     print("Это еще что такое?")
# else:
#     print("Все хорошо")
# finally:
#     f.close()
#     print("Файл закрыт")
# # именно в таком порядке, try, группа except, затем else, и только потом finally
#
# # принудительный вызов исключения
# try:
#     raise Exception("Some exception")
# except Exception as e:
#     print("Exception exception " + str(e))
#
# import math
# print(math.sqrt(4))
#
# from math import sqrt # подключаем напрямую функцию, можно использовать без math, напрямую
# print(sqrt(4))
#
# from math import sqrt, sin, cos  # импортируем несколько функция сразу
# print(sin(0.2))

# def do_something():
#     return "Тырыпыры"
# def more_than_one(num):
#     return num > 1

# import demo as my_lib
# print(my_lib.do_something())
# print(my_lib.more_than_one(6))

# import os
# print("os.name =", os.name)
# print("os.getcwd() =", os.getcwd)
#
# dir_path = os.path.join(os.getcwd(), "NewDir")
# try:
#     os.mkdir(dir_path)
# except FileExistsError:
#     print("Такая директория существует")
#
# import sys
# # список аргументов запуска скрипта,
# # первым аргументом является полный путь к файлу скрипта
# print("sys.argv =", sys.argv)
# # список путей для поиска модулей
# print("sys.path =", sys.path)
# # полный путь к интерпритатору
# print("sys.executable =", sys.executable)
# # словарь имен загруженых модулей
# print("sys.modules =", sys.modules)
# # информация о операционной системе
# print("sys.platform =", sys.platform)
# while True:
#     key = input("press 'q' to exit")
#     if key == "q":
#         sys.exit()
#         # вызов данной функции мгновенно завершает работу модуля (скрипта)
#
#
# import sys
# import argparse
#
# def createParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument ("name", nargs="?", default="мир")
#     return parser
#
# if __name__ == "__main__":
#     parser = createParser()
#     namespace = parser.parse_args(sys.argv[1:])
#
#     # print name space
#     print("Привет, {}!".format(namespace.name))

