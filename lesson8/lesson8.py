# super().__init__() вызов метода от родительского класса
# self.model = model
# self.maxSpeed = maxSpeed


class Transport:
    __type = "default"
    def __init__(self, params = "default"):
        """

        :param params: возможно с какими то параметрами
        """
    pass

    def move(self):
        print("Я транспорт типа: {}. Я умею перемещаться".format(self.__type))

class Car(Transport):
    __type = "car"
    def __init__(self, model, maxSpeed):
        """
        """
        super().__init__()
        self.model = model
        self.maxSpeed = maxSpeed

    def move(self):
        print("Я транспорт типа: {}. Модель: {}. "
              "Я могу ехать со скоростью {} км/ч"
              .format(self.__type, self.model, self.maxSpeed))

def polimorfism(transport):
    if hasattr(transport, "move"):  # проверить на наличие метода и аттрибута в классе (true/false)
        transport.move()
    else:
        print("я не знаю move")

transportDefault = Transport()
car = Car("Tesla model X", 440)

polimorfism(transportDefault)
polimorfism(car)

class Vector:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

# перегружаем оператор +
    def __iadd__(self, other):
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
# #  самом деле это работает так:
# v3 = v1.__add__(v2)
# благодаря перегрузке мы можем использовать более удобную и привычную запись:
# v3 = v1 + v2
