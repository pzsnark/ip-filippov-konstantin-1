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
from operator import itemgetter
PATH_WORKER = './hw7_hard/data/workers'
PATH_CLOCK = './hw7_hard/data/hours_of'


def set_clock(path):
    with open(path, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        clock_list = []
        del lines[0]
        lines.sort(key=itemgetter(1 + 2))
        for line in lines:
            clock_list.append(line.split()[2])
        return clock_list


def paylist(path):
    with open(path, mode='r', encoding='utf-8') as f:
        worker_list = []
        lines = f.readlines()
        del lines[0]
        lines.sort(key=itemgetter(1 + 2))
        n = 0
        for line in lines:
            line = line.split()
            line.append(set_clock(PATH_CLOCK)[n])
            worker_list.append(Worker(*line))
            n += 1
        return worker_list


class Worker:

    def __init__(self, name, surname, salary, position, clock_rate, clock_fact):
        self.__name = name
        self.__surname = surname
        self.__salary = int(salary)
        self.__position = position
        self.__clock_rate = int(clock_rate)
        self.__clock_fact = int(clock_fact)

    def info(self):
        return self.__name, self.__surname, self.__salary, self.__position, self.__clock_rate, self.__clock_fact

    @property
    def pay(self):
        pay_per_clock = self.__salary / self.__clock_rate
        if self.__clock_fact == self.__clock_rate:
            return self.__salary
        elif self.__clock_fact < self.__clock_rate:
            return self.__salary - ((self.__clock_rate - self.__clock_fact) * pay_per_clock)
        else:
            return self.__salary + ((self.__clock_fact - self.__clock_rate) * (pay_per_clock * 2))


for worker in paylist(PATH_WORKER):
    print(worker.info())
    print(round(worker.pay, 2))
