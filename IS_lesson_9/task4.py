# task4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Warning! Your speed is more than max!')


class PoliceCar(Car):
    pass


Ferrari = SportCar(100, 'Красная', 'Спортивная машина', False)
Kia = TownCar(80, 'Белая', 'Городская машина', False)
Kamaz = WorkCar(60, 'Желтая', 'Рабочая машина', False)
Ford = PoliceCar(110, 'Синяя', 'Полицейская машина', True)

Ferrari.show_speed()
Kia.show_speed()
Kamaz.show_speed()
Ford.show_speed()
Ferrari.turn('left')
Ford.turn('right')
print(Ford.is_police)
print(Ferrari.is_police)
