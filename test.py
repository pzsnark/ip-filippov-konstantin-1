# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random
import math

lst = []
lst_new = []
while len(lst) <= 6:
    lst.append(random.randint(1, 25))
print("Произвольный список:", lst)
i = 0
while i <= 6:
    print("Корень из", lst[i], "равен:", math.sqrt(lst[i]), type(math.sqrt(lst[i])))
    if math.sqrt(lst[i]) > 0 and math.sqrt(lst[i]).is_integer == True:
        lst_new.append(math.sqrt(lst[i]))
    else:
        print("Элемент", lst[i], "не отвечает условию")
    i += 1
print("Новый список", lst_new)
