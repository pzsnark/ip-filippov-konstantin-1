# class - шаблон для создания объектов
# классы содержат аттрибуты - данные, и методы - функции для обработки данных
class Student:
    # функция-конструктор - запускается автоматически при создании объекта
    # (экземпляра класса)
    def __init__(self, name, surname, age, school, class_room):
        self.name = name
        self.surname = surname
        self.age = age
        self.school = school
        self.class_room = class_room

    # метод
    # def next_class(self):
    # self.class_room = str(int(self.class_room.split()[0]) + 1) + ' ' +\
    #                   self.class_room.split()[1]
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


student1 = Student("Александр", "Иванов", "10.11.1998", "8 гимназия", "5 А")
student2 = Student("Петр", "Сидоров", "10.01.1995", "8 гимназия", "8 А")

print(student1.get_full_name())
print(student2.get_full_name())

student1.name = "Вася"
