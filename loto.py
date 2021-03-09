# игра лото, второй вариант (более ООП)
import random
import os


class Card:
    """Класс определеющий свойства карт"""

    def __init__(self):
        self.card = [[0] * 9] * 3

    def generator(self):

        rnd = list(range(1, 90))
        random.shuffle(rnd)

        for x in range(3):
            for y in range(9):
                self.card[x][y] = (rnd[(x * 10) + y])
            self.card[x] = sorted(self.card[x])
            true = 0
            false = 0
            for y in range(9):
                if random.choice([True, False]) is True and true <= 4 or false >= 4:
                    true += 1
                else:
                    (self.card[x][y]) = '  '
                    false += 1
        return self.card

    @property
    def get_name(self):
        return self.name

    def info(self):
        """Отображение карты"""
        print(f'{self.get_name}')
        print('--------------------------')
        for x in range(3):
            for y in range(9):
                # if len(str(self.card[x][y])) < 2:
                #     self.card[x][y] = ' ' + str(self.card[x][y])
                print(f'{str(self.card[x][y])}', end=' ')
            print('\t')
        print('--------------------------\n')

    def set_keg(self, value):
        """Зачеркиваем номер в карте"""
        count = 0
        for x in range(3):
            for y in range(9):
                if self.card[x][y] == value:
                    self.card[x][y] = '--'
                    count += 1
                    return count
                else:
                    continue
        if count == 0:
            quit('Такого числа не было. Игра остановлена.')

    def check_keg(self, value):
        for x in range(3):
            for y in range(9):
                if self.card[x][y] == value:
                    quit('Такое число было. Игра окончена')

    def is_win(self):
        """Проверяем критерий победы"""
        string_card = str()
        for x in range(3):
            for y in range(9):
                string_card += str(self.card[x][y])
        if string_card.count('--') >= 15:
            print('Победил игрок ', self.name)
            quit('Игра остановлена')


class CardPlayer(Card):
    """Карта игрока"""
    def __init__(self):
        super().__init__()
        self.name = 'Player'


class CardComputer(Card):
    """Карта компьютера"""
    def __init__(self):
        super().__init__()
        self.name = 'Computer'

    def set_keg(self, value):
        """Зачеркиваем номер в карте"""
        for x in range(3):
            for y in range(9):
                if self.card[x][y] == value:
                    self.card[x][y] = '--'
                else:
                    continue


class Keg:
    """Класс бочонков"""
    def __init__(self):
        self.keg_list = list(range(1, 91))
        random.shuffle(self.keg_list)
        self._var_count = 1

    @property
    def current(self):
        return self.keg_list[self.count]

    @property
    def count(self):
        return self._var_count

    @count.setter
    def count(self, value):
        self._var_count = value

    def info(self):
        print(f'Новый бочонок: {self.current} (осталось {90 - self.count})')


card_player = CardPlayer()
card_computer = CardComputer()
card_player.generator()
card_computer.generator()
keg = Keg()


def game():
    """Игра начинается"""

    os.system('cls')  # for windows cmd
    keg.info()
    card_player.info()
    card_computer.info()
    quest = input('Зачеркнуть число? y/n\n')

    if quest == 'y':
        card_player.set_keg(keg.current)

    else:
        card_computer.set_keg(keg.current)
        card_player.check_keg(keg.current)

    card_player.is_win()
    card_computer.is_win()

    keg.count += 1
    game()


game()
