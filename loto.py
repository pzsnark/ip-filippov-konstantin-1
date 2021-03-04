# игра лото

import random


class Card:
    """Класс описывающий карты лото"""

    def __init__(self):
        self.__card = [['  '] * 9] * 3
        self.__point = [self.__card[0][2]]

    def generator(self):
        pass
        return self.__card


