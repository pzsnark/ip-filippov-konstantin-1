# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


def create_workers_from_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        worker_list = []
        for line in f:
            worker_list.append(Worker(*line.split()))
        return worker_list


class Worker:

    def __init__(self, name, surname, salary, position, clock_rate):
        self.__name = name
        self.__surname = surname
        self.__salary = int(salary)
        self.__position = position
        self.__clock_rate = int(clock_rate)
        self.__path = './hw7_hard/data/workers'
        self.__clock_fact = None
        self.__pay = None

    def info(self):
        return self.__name, self.__surname, self.__salary, self.__position, self.__clock_rate

    @property
    def clock_fact(self):
        return self.__clock_fact

    def set_clock_fact(self):
        if self.__clock_fact is None:
            print('Значение не установлено')
            self.__clock_fact = input('Введите новое значение: ')
        else:
            print(f'Текущее значение: {self.__clock_fact}')
            self.__clock_fact = input('Введите новое значение: ')

    def payroll(self):
        pay_per_clock = self.__salary / self.__clock_rate
        if self.__clock_fact == self.__clock_rate:
            self.__pay = self.__salary
        elif self.__clock_fact < self.__clock_rate:
            self.__pay = self.__salary - (self.__clock_fact * pay_per_clock)
        else:
            self.__pay = self.__salary + (self.__clock_fact * (pay_per_clock * 2))


# for worker in create_workers_from_file('./hw7_hard/data/workers')[1:]:
#     print(worker.info())
#
# worker1 = create_workers_from_file('./hw7_hard/data/workers')[1]
# print(worker1)


workers = create_workers_from_file('./hw7_hard/data/workers')
workers[1].set_clock_fact()
print(workers[1].clock_fact)
