# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random


def seq(a):
    result = str()
    max_result = 0
    last = a[0]
    for i in a:
        if i == last:
            result += str(i)
        else:
            if len(result) > len(max_result):
                max_result = result
            last = i
            result = ""
    if result > max_result:
        max_result = result
    return max_result


with open('2500.txt', 'r+', encoding='UTF-8') as file:
    for _ in range(2500):
        file.write(str(random.randint(0, 9)))
    print(seq(file.read()))
