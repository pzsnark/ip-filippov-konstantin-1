import random


class MusicGenre:
    """Базовый класс жанра для музыкальной библиотеки
       Определяет название жанра и его рейтинг в библиотеке
    """
    genre_count = 0

    def __init__(self, name, rating):
        self._name = name
        self._rating = rating
        MusicGenre.genre_count += 1

    def __del__(self):
        MusicGenre.genre_count -= 1

    def rate_up(self, point):
        self._rating += point

    def rate_down(self, point):
        self._rating -= point

    def rating(self):
        return self._rating


class DrumAndBass(MusicGenre):
    def rating(self):
        # случайная накрутка рейтинга
        if random.randint(0, 4) == 1:
            return self._rating + 1
        else:
            return self._rating


group = DrumAndBass("Pendulum", 65.7)
group.rate_up(5.5)
print("рейтинг исполнителя {}: {}".format(group._name, group.rating()))


class PromoConcert:
    """Промо-концерт - улучшает рейтинг исполнителя"""
    points = 5.00

    def go_up(self):
        self.rate_up(self.points)


class Gossip:
    """Сплетни, слухи - снижают рейтинг"""
    points = 2.70

    def go_down(self):
        self.rate_down(self.points)


# класс использующий механизм множественного наследования
class SuperDrums(DrumAndBass, PromoConcert, Gossip):
    def rate_up(self, points):
        super().rate_up(points)

    def rate_down(self, points):
        super().rate_down(points)


artist = SuperDrums("RonWellsJS", 90.00)
artist.go_up()
print(artist.rating())
artist.go_down()
print(artist.rating())
