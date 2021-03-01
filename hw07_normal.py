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


class School:
    """Класс описывающий школы"""

    def __init__(self, number):
        self.__classes_list = []
        self.__number = number

    def __str__(self):
        return self.__number

    @property
    def name(self):
        return self.__number

    def add_classes(self, class_):
        self.__classes_list.append(class_)
        class_.set_school(self)

    def get_classes(self):
        return self.__classes_list


class Classes:
    """Класс описывающий школьные классы"""

    def __init__(self, number=None, index=None):
        self.__number = number
        self.__index = index
        self.__school = None
        self.__students_list = []
        self.__teachers_list = []

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__number + self.__index

    def set_school(self, school):
        self.__school = school

    def add_student(self, student):
        self.__students_list.append(student)
        student.set_class(self)

    def add_teacher(self, teacher):
        self.__teachers_list.append(teacher)

    def get_students_list(self):
        return self.__students_list

    def get_teachers_list(self):
        return self.__teachers_list


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

        self.__class_ = None

    @property
    def class_(self):
        return self.__class_

    def set_class(self, class_):
        self.__class_ = class_


class Teacher(Human):
    """Класс описывающий переподавателей школы"""

    def __init__(self, *args):
        super().__init__(*args)

        self.__school_subject = None

    @property
    def school_subject(self):
        return self.__school_subject

    def set_school_subject(self, school_subject):
        self.__school_subject = school_subject

    @property
    def school_subject(self):
        return self.__school_subject


class SchoolSubject:
    """Класс описывающий школьные предметы"""

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value


class1 = Classes('4', 'A')
class2 = Classes('4', 'Б')

parent1 = Parent('Иванов', 'Иван', 'Васильевич')
parent2 = Parent('Иванова', 'Светлана', 'Анатольевна')

student1 = Student('Иванов', 'Иван', 'Иванович')
student2 = Student('Петров', 'Петр', 'Петрович')
student3 = Student('Сидоров', 'Сидор', 'Сидорович')

teacher1 = Teacher('Тарханов', 'Архип', 'Евграфьевич')
teacher2 = Teacher('Морозова', 'Мария', 'Ивановна')
teacher3 = Teacher('Разумовский', 'Аристарх', 'Аполлинарьевич')

student2.set_father(parent1)
student2.set_mother(parent2)

subj1 = SchoolSubject('Русский язык')
subj2 = SchoolSubject('Математика')
subj3 = SchoolSubject('История')

class1.add_student(student1)
class1.add_student(student2)
class2.add_student(student3)

class1.add_teacher(teacher1)
class1.add_teacher(teacher2)
class1.add_teacher(teacher3)
class2.add_teacher(teacher1)
class2.add_teacher(teacher3)

teacher1.set_school_subject(subj1)
teacher2.set_school_subject(subj2)
teacher3.set_school_subject(subj3)

school1 = School('6')
school1.add_classes(class1)
school1.get_classes()

# вывод предметов ученика:
# for teacher in student2.class_.get_teachers_list():
#     print(teacher.school_subject.name)

# вывод список учеников
print(f'Список учеников {class1} класса:')
for student in class1.get_students_list():
    print(f'{student.surname} {student.name[0]}. {student.patronymic[0]}.')


# n = teacher1.get_object()
# print(f'Фамилия: {n[0]}')
# print(f'Имя: {n[1]}')
# print(f'Отчество: {n[2]}')
# m = 1
# for i in n[3]:
#     print(f"Предмет #{m}: {i.get_name}")
#     m += m

