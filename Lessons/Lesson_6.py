# '''
# Задание 1
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
# реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
# зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# '''
#
# import time
#
# class TrafficLight:
#     color_time = {'Красный': 2,
#                    'Желтый': 2,
#                    'Зеленый': 4}
#     __color = None
#     __index = 0
#     counter = 1
#
#     def __init__(self, init_color='Красный', counter=1):
#         self.__color = init_color if self.color_time.get(init_color) else list(self.color_time.keys())[self.__index]
#         self.__index = list(self.color_time.keys()).index(self.__color)
#         self.counter = counter
#
#     def running(self):
#         print(self.__color)
#         while self.counter:
#             time.sleep(self.color_time.get(self.__color))
#             self.__index = (self.__index + 1) % 3
#             self.__color = list(self.color_time.keys())[self.__index]
#             print(self.__color)
#             self.counter -= 1
#
#
# if __name__ == '__main__':
#     while True:
#         counter = input('Сколько раз поменяем цвета?')
#         try:
#             counter = int(counter)
#             break
#         except ValueError as e:
#             print('Ожидаем целое число')
#     lights = TrafficLight(counter=counter)
#     lights.running()

# '''
# Задание 2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
# '''
# class Road:
#     weight = 25  # вес одного м2 полотна
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def road_weight(self, depth):
#         return self._length * self._width * self.weight * depth
#
#
# if __name__ == '__main__':
#     road_Krasnoyrsk_Novosibirsk = Road(8000, 7)
#     w = road_Krasnoyrsk_Novosibirsk.road_weight(20)
#     print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна равна '
#           f'{w} кг (или {w/1000} тонн)')
#     print(f'Длина дороги Красноярск-Новосибирск равна {road_Krasnoyrsk_Novosibirsk._length} м')
#     print(f'Ширина дороги Красноярск-Новосибирск равна {road_Krasnoyrsk_Novosibirsk._width} м')

'''
Задание 3
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
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