# class Student:
#     def __init__(self, name, surname, age, school, class_room):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.school = school
#         self.class_room = class_room
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def set_name(self, new_name):
#         self.name = new_name
#
# class Teacher:
#     def __init__(self, name, surname, age, school, class_room, class_list):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.school = school
#         self.class_room = class_room
#         self.class_list = class_list

class Person:
    def __init__(self, name, surname, age, school):
        self.name = name
        self.surname = surname
        self.age = age
        self.school = school
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name

class Student(Person):
    def __init__(self, surname, age, school, class_room, name="Ivan"):
        Person.__init__(self, name, surname, age, school)
        self._class_room = class_room

    def set_new_class_room(self, class_room):
        self._class_room = class_room

    # @property - позваоляет обратиться к методу как к аттрибуту
    # self.get_class_room() --> .class_room
    @property
    def get_class_room(self):
        return self._class_room


class Teacher(Person):
    def __init__(self, name, surname, age, school, class_list):
        Person.__init__(self, name, surname, age, school)
        self._class_list = class_list

    def set_new_class_list(self, class_list):
        self._class_list = class_list

    def get_class_list(self):
        return self._class_list

student_1 = Student("Ivan", "Ivanov", "23", "school", "2d")
teacher_1 = Teacher("Petr", "Petrov", "43", "schools", "2d,2c,2a")

print(teacher_1.get_full_name())
print(teacher_1.get_class_list())
teacher_1.set_new_class_list("2a")
print(teacher_1.get_class_list())

# @property - позваоляет обратиться к методу как к аттрибуту
# .class_room() --> .class_room
