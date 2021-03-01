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

    students_list = []
    teachers_list = []

    def __init__(self, number='undefined', index='undefined'):
        self.__number = number
        self.__index = index

    @property
    def get_name(self):
        return self.__number + self.__index

    def set_name(self, value):
        self.__number = value

    def add_student(self, student):
        self.students_list.append(student)

    def add_teacher(self, teacher):
        self.teachers_list.append(teacher)

    def get_students_list(self):
        return self.students_list


class Human:
    """Класс описывающий людей"""

    def __init__(self, surname, name, patronymic, father=None, mother=None):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__father = father
        self.__mother = mother

    def get_object(self):
        return self.surname, self.name, self.patronymic, self.father, self.mother

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def father(self):
        return self.__father

    def set_father(self, father):
        self.__father = father

    @property
    def mother(self):
        return self.__mother

    def set_mother(self, mother):
        self.__mother = mother


class Parent(Human):
    """Класс описывающий родителей учеников"""

    def __init__(self, surname, name, patronymic):
        super().__init__(surname, name, patronymic)


class Student(Human):
    """Класс описывающий учащихся школы"""

    def __init__(self, *args):
        super().__init__(*args)


class Teacher(Human):
    """Класс описывающий переподавателей школы"""

    school_subjects = []

    def add_school_objects(self, *args):
        for school_object in args:
            self.school_subjects.append(school_object)

    def get_object(self):
        return self.surname, self.name, self.patronymic, self.school_subjects


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

parent1 = Parent('Иванов', 'Иван', 'Васильевич')
parent2 = Parent('Иванова', 'Светлана', 'Анатольевна')

student1 = Student('Иванов', 'Иван', 'Иванович')
student2 = Student('Петров', 'Петр', 'Петрович')
teacher1 = Teacher('Тарханов', 'Архип', 'Евграфьевич')

student2.set_father(parent1)
student2.set_mother(parent2)

subj1 = SchoolSubject('Русский язык')
subj2 = SchoolSubject('Математика')
subj3 = SchoolSubject('История')

class1.add_student(student1)
class1.add_student(student2)
class1.add_teacher(teacher1)

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

class1.get_students_list()
print(student1.get_object())
print(student2.get_object())
