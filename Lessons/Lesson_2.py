# #Задание № 1
# num = 7
# num_1 = 4.8
# my_name = "Ольга"
# com = complex(10, 15)
# my_list = [num, num_1, my_name, com]
# print(my_list)
# for el in my_list:
#     print(f'{el} это {type(el)}')

#Задание №2
# val = (input("Введите любые символы через пробел:")).split()
# my_list = val
# if len(my_list) % 2 == 0:
#         a = 0
#         while a < len(my_list):
#             el = my_list[a]
#             my_list[a] = my_list[a + 1]
#             my_list[a + 1] = el
#             a += 2
# else:
#         a = 0
#         while a < len(my_list) - 1:
#             el = my_list[a]
#             my_list[a] = my_list[a + 1]
#             my_list[a + 1] = el
#             a += 2
# print(my_list)
'''#Задание № 3
seasons = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]
seasons_dict = {
    'Зима': ['12', '1', '2'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}
month_numeral = input('Пожалуйста, введите номер месяца: ')
if month_numeral > '12':
    print("Вы ввели неверное число")
else:
    for season, months in seasons:# с использованием списка
        if month_numeral in months:
            print(f'Вы ввели месяц с номером {month_numeral} это {season}')
    for season, months in seasons_dict.items():#с использованием словаря
        if month_numeral in months:
            print(f'Месяц с номером {month_numeral} это {season}')
'''
#Задание № 4
worlds = (input("Введите любые слова через пробел:")).split()
my_list = worlds
for idx, word in enumerate(my_list):
    print(idx + 1, (word, word[:11])[len(word) > 10])


