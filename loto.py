# игра лото

import random


class Card:
    """Класс описывающий карты лото"""

    def __init__(self):
        pass

    @staticmethod
    def generator():
        card = [[0] * 9] * 3
        rnd = list(range(1, 30))
        random.shuffle(rnd)

        for x in range(3):
            for y in range(9):
                card[x][y] = (rnd[(x * 10) + y])
            card[x] = sorted(card[x])
            true = 0
            false = 0
            for y in range(9):
                if random.choice([True, False]) is True and true <= 4 or false >= 4:
                    true += 1
                else:
                    (card[x][y]) = '  '
                    false += 1
        return card

    @staticmethod
    def game():
        Card.move()

    @staticmethod
    def move():
        keg = list(range(1, 90))
        random.shuffle(keg)
        count = 0

        print(f'Новый бочонок: {keg[count]} (Осталось {89 - count})')
        print('----- Ваша карточка ------')
        for x in range(3):
            for y in range(9):
                if len(str(card_gamer[x][y])) < 2:
                    card_gamer[x][y] = ' ' + str(card_gamer[x][y])
                print(f'{str(card_gamer[x][y])}', end=' ')
            print('\r')
        print('--------------------------')

        print('-- Карточка компьютера ---')
        for x in range(3):
            for y in range(9):
                if len(str(card_computer[x][y])) < 2:
                    card_computer[x][y] = ' ' + str(card_computer[x][y])
                print(f'{str(card_computer[x][y])}', end=' ')
            print('\r')
        print('--------------------------')


card_gamer = (Card.generator())
card_computer = (Card.generator())
Card.move()
