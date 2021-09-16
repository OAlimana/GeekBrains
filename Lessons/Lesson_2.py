# #Задание № 1
# num = 7
# num_1 = 4.8
# my_name = "Ольга"
# my_list = [num, num_1, my_name]
# print(my_list)
# for el in my_list:
#     print(f'{el} это {type(el)}')

#Задание №2
val = input("введите целое число:")
try:
    val != int(val)
except ValueError:
    print("Вы ввели не целое число, попробуйте еще раз")
val = input("введите целое число")
while val != int(val):
    print("Идите учить математику раз вы не знаете, что такое целое число. Пока")
print("Хотите ввести еще одно число? Да/нет")


