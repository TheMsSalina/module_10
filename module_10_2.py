import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int, enemies: int = 100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.enemies > 0:
            time.sleep(1)
            day += 1
            self.enemies -= self.power
            print(f'{self.name} сражается {day} день(дня)...,',
                  f'осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()



