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
val = (input("Введите любые символы через пробел:")).split()
my_list = val
if len(my_list) % 2 == 0:
        a = 0
        while a < len(my_list):
            el = my_list[a]
            my_list[a] = my_list[a + 1]
            my_list[a + 1] = el
            a += 2
else:
        a = 0
        while a < len(my_list) - 1:
            el = my_list[a]
            my_list[a] = my_list[a + 1]
            my_list[a + 1] = el
            a += 2
print(my_list)
#Задание № 3

