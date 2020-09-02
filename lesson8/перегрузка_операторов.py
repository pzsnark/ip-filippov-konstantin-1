class Vector:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

# перегружаем оператор +
    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    def as_point(self):
        return self.x, self.y

# формируем удобное отображение объекта при выводе функции print()
    def __str__(self):
        return "V(x:{} y:{})".format(self.x, self.y)

# создаем экземпляры клласса
v1 = Vector((10, 15))
v2 = Vector((12, 10))
# наши объекты учавствуют в операции сложения (+)
v3 = v1 + v2
print(v3)
# #  самом деле это работает так:
# v3 = v1.__add__(v2)
# благодаря перегрузке мы можем использовать более удобную и привычную запись:
# v3 = v1 + v2
