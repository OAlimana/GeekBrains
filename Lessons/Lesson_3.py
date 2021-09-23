""" Задание 1
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль."""

# def my_numbers(num_1, num_2):
#     return num_1 / num_2
#
# num1 = int(input("Введите любое число:>>"))
# num2 = int(input("Введите еще одно число, кроме 0:>>"))
# while True:
#     if num2 == 0:
#         num2 = int(input("Вы ввели 0. Введите другое число:>>"))
#     else:
#         print(f"Результат деления равен {my_numbers(num1, num2)}")
#         exit()

''' Задание 2
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
'''
def person(name, surname, year, city, email, fon_number):
    print(f'{name} {surname} {year} {city} {email} {fon_number}')
person(name="Наталья", surname="Смирнова", year=1985, city="Мурманск", email="jfdkjfd@kdvn.ru",
fon_number=81253648569)

''' Задание 3
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
'''

def my_func(num_1, num_2, num_3):
    
    if num_1 >= num_2 and num_2 >= num_3:
        return num_1 + num_2
    elif num_1 > num_2 and num_2 < num_3:
        return num_1 + num_3
    else:
        return num_2 + num_3

num1, num2, num3 = 5, 2, 1
print(my_func(num1, num2, num3))