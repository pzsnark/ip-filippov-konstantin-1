# string = "Hello"
# string_test = "asdasdasdasdasdasdyyy"
# # print(string[1:5:1])
# # print(string[:-1]) срез без последнего символа
# a = "Start"
# b = "Stop"
# c = "Step"
# # string[a:b:c] индексация начинается с 0
# # .title(), .upper(), .lower(), find() etc.
#
# print(string_test.find("yy"), len(string_test))


# name = "Eric"
# surname = "Smith"
# print("Welcome " + name + " " + surname + "!")
# print("Welcome %s %s !" % (name, surname))
# print("Welcome {} {} !".format(name, surname))
# print("Welcome {1} {0} !" .format(name, surname))
# print(f'Welcome {name} {surname} !')

# empty_list = [] # пустой список
my_list = [1, 3, 5, 3.45, 'ddd', 333]
# print('my_list = ', my_list)
#
# print(my_list[0]) # 1
# print(my_list[0:-3]) # [1, 3 ,5]
#
# my_list = [1, 3, 5, 3.45, 'ddd', 333]
# print("s" in my_list) # true
# print("sss" in my_list) # false
#
# my_list = [1, [1, [3]]]
# print(my_list[1][1][0]) # 3

# my_list.append(["1",3.2])
# print(my_list)

# lst = [1, 2, 3]
# lst.append(4) # бавить в конец списка
# lst.pop() # удалить последний элемент
# lst.pop(1) # удалить элемент с индексом 1
# del lst[0]
# print(lst)

# t = (2) # просто int
# print(t)
# t = (2,) # кортеж
# t = 2, # тоже кортеж

# fruits = ["apple", "banana", "mango"]
# i = 0
# while len(fruits) > i:
#     print("fruit = ", fruit[i])
#     i += i
#
# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print("fruit = ", fruit)
#
# for el in "Hello":          # со строкой тоже работает
#     print("el = ", el)
# print()
# for t_el in 1, 2, 3, 4, 5, 10: # и с кортежем
#     print("--------------")
#     print('t_el = ', t_el)
# print()

x = {} # пустой словарь
print(x)
x["y"] = "1"
print(x)
x["c"] = {"1": 1}
print(x)

for key, value in x.items():
    print(key, value)
for key in x.keys():
    print(key)
for value in x.values():
    print(value)
# удаляет элемент и возвращает его значение
print(x.pop("c"))
print(x)
# удаляет и возвращает пару (ключ, значение)
print(x.popitem()) # удаляет и возвращает произвольную пару (ключ, значение)

x = {"y", "z"}
print(x)
# x["y"] = 1
print(x)

# множества

a = set()
print('a =', a) # set()
print("b =", b)
c = set("hello")
print("c =", c)
d = {"a", "b", "c", "d"}
print("d = ", d)
f = {} # а так получится словарь
print("type({})-->", type(f)) # <class 'dict'>
# Операции с множествами
print(len(e))
print(""b" in b -->", "b" in b)
# s == t
c1 = {"e", "l", "o", "h"}
print(c == c1)


a = set(["a", "3", "5"])
b = set(["a", "3", 6])
print(a)
print(b.issubset(a))

myset = {1, 2, 3, 5}
second_set = {1, 2, 7} #
# print(myset.issubset) нахождение подмножества
# s.isuperset нахождение надмножества
# s.union объединение множеств
# s.intersection пересечение подмножеств
# s.difference различие
# symmetric_difference находит элементы которые есть либо в одном, либо в другом, но в обоих подмножествах
