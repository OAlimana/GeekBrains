# ''' Задание 1.
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об  окончании
# ввода данных свидетельствует пустая строка.
# '''
#
# my_f = open("my_file.txt", "w")
# my_f.write("Это мой файл")
# my_f.close()

''' Задание 2
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
'''
my_f = open("new_file.txt")
line_count = 0

for line in my_f:
    line_count += 1
    s= str(line).split()
    words = len(s)
    print(f'Количество слов в {line_count} строке равно {words}')

print(f'Колиество строк в файле равно {line_count}')
my_f.close()



