'''
Задание 1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

import time

class TrafficLight:
    color_time = {'Красный': 2,
                   'Желтый': 2,
                   'Зеленый': 4}
    __color = None
    __index = 0
    counter = 1

    def __init__(self, init_color='Красный', counter=1):
        self.__color = init_color if self.color_time.get(init_color) else list(self.color_time.keys())[self.__index]
        self.__index = list(self.color_time.keys()).index(self.__color)
        self.counter = counter

    def running(self):
        print(self.__color)
        while self.counter:
            time.sleep(self.color_time.get(self.__color))
            self.__index = (self.__index + 1) % 3
            self.__color = list(self.color_time.keys())[self.__index]
            print(self.__color)
            self.counter -= 1


if __name__ == '__main__':
    while True:
        counter = input('Сколько раз поменяем цвета?')
        try:
            counter = int(counter)
            break
        except ValueError as e:
            print('Ожидаем целое число')
    lights = TrafficLight(counter=counter)
    lights.running()

'''
Задание 2
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''
class Road:
    weight = 25  # вес одного м2 полотна

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self, depth):
        return self._length * self._width * self.weight * depth


if __name__ == '__main__':
    road_Krasnoyrsk_Novosibirsk = Road(8000, 7)
    w = road_Krasnoyrsk_Novosibirsk.road_weight(20)
    print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна равна '
          f'{w} кг (или {w/1000} тонн)')
    print(f'Длина дороги Красноярск-Новосибирск равна {road_Krasnoyrsk_Novosibirsk._length} м')
    print(f'Ширина дороги Красноярск-Новосибирск равна {road_Krasnoyrsk_Novosibirsk._width} м')

'''
Задание 3
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"оклад": wage, "бонус": bonus}


class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    me = Position('Ольга', 'Непомнящая', 'Руководитель отдела продаж', 135000, 10000)
    me2 = Position('Петр', 'Николаев', 'Коммерческий директор', 250000, 30000)
    print(me.get_full_name())
    print(f'Общий доход: {me.get_total_income()} руб')
    print(me.position)
    print(me._income)
    print(me2.get_full_name())
    print(f'Общий доход: {me2.get_total_income()} руб')
    print(me2.position)
    print(me2._income)

'''
Задание 4
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''
class Car:
    __speed = 0
    __direction = None

    def __init__(self, speed, color, name, is_police):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = self.__speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        pass

    def show_speed(self):
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'ВНИМАНИЕ!!! Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    MAX_SPEED = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'ВНИМАНИЕ!!! Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    pc = PoliceCar(100, 'синий', 'ВАЗ')
    wc1 = WorkCar(70, 'белый', 'Рено')
    wc2 = WorkCar(95, 'серый', 'Газель')
    sc = SportCar(250, 'красный', 'Ауди')
    tc1 = TownCar(45, 'черный', 'Мазда')
    tc2 = TownCar(63, 'желтый', 'Тойота')
    pc.show_speed()
    pc.go()
    pc.show_speed()
    pc.stop()
    print(pc.color)
    pc.go()
    print(pc.name)
    wc1.go()
    wc2.go()
    sc.go()
    tc1.go()
    tc2.go()
    wc1.show_speed()
    wc2.show_speed()
    sc.show_speed()
    tc1.show_speed()
    tc2.show_speed()

'''
Задание 5
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw 
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), 
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого 
экземпляра.
'''

class Stationery:

    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):

    def __init__(self):
        super().__init__('ручка')
    def draw(self):
        print(f'Запуск отрисовки. {self.title}')

class Pencil(Stationery):

    def __init__(self):
        super().__init__('карандаш')
    def draw(self):
        print(f'Запуск отрисовки. {self.title}')

class Handle(Stationery):

    def __init__(self):
        super().__init__('маркер')
    def draw(self):
        print(f'Запуск отрисовки. {self.title}')

if __name__ == '__main__':
    p = Pen()
    n = Pencil()
    h = Handle()

    p.draw()
    n.draw()
    h.draw()

