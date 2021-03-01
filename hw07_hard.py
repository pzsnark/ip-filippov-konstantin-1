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


def create_worker(path):
    with open(path, mode='r', encoding='utf-8') as f:
        worker_list = []
        for line in f:
            worker_list.append(Worker(*line.split()))
        return worker_list


class Worker:

    def __init__(self, name, surname, salary, position, clock_rate):
        self.__name = name
        self.__surname = surname
        self.__salary = salary
        self.__position = position
        self.__clock_rate = clock_rate
        self.__path = './hw7_hard/data/workers'

    def info(self):
        return self.__name, self.__surname, self.__salary, self.__position, self.__clock_rate

    def add_worker(self, value):
        with open(self.__path, mode='r', encoding='utf-8') as f:
            worker_list = []
            for line in f:
                worker_list.append(Worker(*line.split()))
            return worker_list[value]


# for worker in create_worker('./hw7_hard/data/workers')[1:]:
#     print(worker.info())
#
# worker1 = create_worker('./hw7_hard/data/workers')[1]
# print(worker)

worker1 = Worker.add_worker('self', 2)
print(worker1)
