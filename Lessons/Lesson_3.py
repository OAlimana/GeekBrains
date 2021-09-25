""" Задание 1
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль."""

def my_numbers(num_1, num_2):
    return num_1 / num_2

num1 = int(input("Введите любое число:>>"))
num2 = int(input("Введите еще одно число, кроме 0:>>"))
while True:
    if num2 == 0:
        num2 = int(input("Вы ввели 0. Введите другое число:>>"))
    else:
        print(f"Результат деления равен {my_numbers(num1, num2)}")
        exit()

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

''' Задание 4
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
'''

def power(a, n):

    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

x = 5
y = -3
print(power(x, y))

''' Задание 5
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу
'''

def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('введите любые число через пробел или нажмите n для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'n' or number[el] == 'n':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел равна {sum_res}')
    print(f'Итоговая сумма равна {sum_res}')
my_sum()

''' Задание 6
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(*args):
    word = input("Введите любое слово ")
    print(word.title())
    return
int_func()

# Задание 5 другой вариант
num_sum = 0
flag = True
while flag:
    nums = input("Введите строку чисел, для завершения введите ! : ")
    nums = nums.split(" ")
    for el in nums:
        if el == "!":
            flag = False
            break
        num_sum = num_sum+int(el)
    print(num_sum)