# игра лото

import random
import os


class Card:
    """Класс описывающий карты лото"""
    count = 1

    def __init__(self):
        pass

    @staticmethod
    def generator():
        card = [[0] * 9] * 3
        rnd = list(range(1, 90))
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
        Card.move(count=Card.count)

    @staticmethod
    def move(count):
        keg = list(range(1, 90))
        random.shuffle(keg)

        print(f'Новый бочонок: {keg[count]} (Осталось {90 - count})')
        print('----- Ваша карточка ------')
        for x in range(3):
            for y in range(9):
                # if len(str(card_gamer[x][y])) < 2:
                #     card_gamer[x][y] = ' ' + str(card_gamer[x][y])
                print(f'{str(card_gamer[x][y])}', end=' ')
            print('\t')
        print('--------------------------')

        print('-- Карточка компьютера ---')
        for x in range(3):
            for y in range(9):
                if len(str(card_computer[x][y])) < 2:
                    card_computer[x][y] = ' ' + str(card_computer[x][y])
                print(f'{str(card_computer[x][y])}', end=' ')
            print('\t')
        print('--------------------------')
        quest = input('Зачеркнуть число? (y/n) \n')

        if quest == 'y' or '':
            if keg[count] in card_gamer[0]:
                index = card_gamer[0].index(keg[count])
                card_gamer[0][index] = '--'
            elif keg[count] in card_gamer[1]:
                index = card_gamer[1].index(keg[count])
                card_gamer[1][index] = '--'
            elif keg[count] in card_gamer[2]:
                index = card_gamer[2].index(keg[count])
                card_gamer[2][index] = '--'
            else:
                print('Вы проиграли')
                quit()
        else:
            if keg[count] in card_computer[0]:
                index = card_computer[0].index(keg[count])
                card_computer[0][index] = '--'
            elif keg[count] in card_computer[1]:
                index = card_computer[1].index(keg[count])
                card_computer[1][index] = '--'
            elif keg[count] in card_computer[2]:
                index = card_computer[2].index(keg[count])
                card_computer[2][index] = '--'

        os.system('cls')  # for windows cmd
        Card.move(count + 1)


card_gamer = (Card.generator())
card_computer = (Card.generator())
Card.game()
