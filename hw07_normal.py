# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Classes:
    """Класс описывающий школьные классы"""

    student_list = []

    def __init__(self, number='undefined', index='undefined'):
        self.__number = number
        self.__index = index

    @property
    def get_name(self):
        print(f'Класс: {self.__number + self.__index}')
        return self.__number + self.__index

    def set_name(self, value):
        self.__number = value

    def add_student(self, student):
        self.student_list.append(student)
        student = student.get_object()

    def get_student_list(self):
        return Classes.student_list


class Human:
    """Класс описывающий людей"""

    def __init__(self, surname, name, patronymic, father=None, mother=None):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__father = father
        self.__mother = mother

    def get_object(self):
        return self.get_surname, self.get_name, self.get_patronymic, self.get_father, self.get_mother

    @property
    def get_surname(self):
        return self.__surname

    @property
    def get_name(self):
        return self.__name

    @property
    def get_patronymic(self):
        return self.__patronymic

    @property
    def get_father(self):
        return self.__father

    @property
    def get_mother(self):
        return self.__mother


class Parent(Human):
    """Класс описывающий родителей учеников"""

    def __init__(self, surname, name, patronymic):
        super().__init__(surname, name, patronymic)


class Student(Human):
    """Класс описывающий учащихся школы"""

    def __init__(self, surname, name, patronymic, father=None, mother=None):
        super().__init__(surname, name, patronymic, father, mother)


class Teacher(Human):
    """Класс описывающий переподавателей школы"""

    school_subjects = []

    def add_school_objects(self, *args):
        for school_object in args:
            self.school_subjects.append(school_object)

    def get_object(self):
        return self.get_surname, self.get_name, self.get_patronymic, self.school_subjects


class SchoolSubject:
    """Класс описывающий школьные предметы"""

    def __init__(self, name):
        self.__name = name

    @property
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value


class1 = Classes('4', 'A')

student1 = Student('Иванов', 'Иван', 'Иванович')
student2 = Student('Петров', 'Петр', 'Петрович')
teacher1 = Teacher('Тарханов', 'Архип', 'Евграфьевич')

subj1 = SchoolSubject('Русский язык')
subj2 = SchoolSubject('Математика')
subj3 = SchoolSubject('История')

class1.add_student(student1)
class1.add_student(student2)

teacher1.add_school_objects(subj1)
teacher1.add_school_objects(subj2)
teacher1.get_object()
# n = teacher1.get_object()
# print(f'Фамилия: {n[0]}')
# print(f'Имя: {n[1]}')
# print(f'Отчество: {n[2]}')
# m = 1
# for i in n[3]:
#     print(f"Предмет #{m}: {i.get_name}")
#     m += m

class1.get_student_list()
