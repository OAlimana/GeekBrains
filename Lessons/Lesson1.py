##Задание № 1
#a = 10
#b = 25
#c = a + b
#print('c=', c)
#
#name = input ("Ввеите ваше имя: ")
#age = int(input('Введите ваш возраст: '))
#print('Меня зовут ', name, 'мне', age, 'лет')
#Задание № 2
# sec = int(input("Введите время в секундах: "))
# m, s = divmod(sec, 60)
# h, m = divmod(m, 60)
# print(f'{h:d}:{m:02d}:{s:02d}')
#Задание № 3
# num = int(input("Введите целое число:"))
# n = str(num)
# n1 = n + n
# n2 = n + n + n
# rez = num + int(n1) + int(n2)
# print ('результат равен: ', rez)
#Задание № 4
# num = abs(int(input("Введите целое положительное число ")))
# max = num % 10
# while num >= 1:
#     num = num // 10
#     if num % 10 > max:
#         max = num % 10
#     if num > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max)
#         break
#Задание № 5
# profit = float(input("Введите выручку фирмы "))
# costs = float(input("Введите издержки фирмы "))
# if profit > costs:
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы "))
#     print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
# elif profit == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")
#Задание № 6
a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)