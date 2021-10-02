'''
Задание 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

name, time, salary, bonus = argv

try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Заработная плата сотрудника  {res}')
except ValueError:
    print('Упс, чего-то не хватает')

'''
Задание 2
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента
'''
my_list = [7, 4, 6, 15, -8, 0, 36]
n_List = list(enumerate(my_list))
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f"Исходный список: {my_list}")
print(f"Новый список такой: {new_list}")

'''
Задание 3
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
'''

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

'''
Задание 4
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор
'''
my_list = [10, 5, 0, 65, -29, 15, 128, 0, 65, 129, 10]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)

'''
Задание 5
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа
от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
'''
from functools import reduce


def my_func(number, el):
    return number * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения четных значений равен: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

'''
Задание 6
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
'''
# вариант а
from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el) # внимание - беконечный цикл!

# вариант б
from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el) # внимание - беконечный цикл!

'''
Задание 7
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
'''
from itertools import count
from math import factorial

def f_gen():
    for el in count(1):
        yield factorial(el)

num = f_gen()
a = 0
for i in num:
    if a < 15:
        print(i)
        a += 1
    else:
        break