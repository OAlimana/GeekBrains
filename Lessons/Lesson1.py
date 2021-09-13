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
sec = int(input("Введите время в секундах: "))
min = sec // 60
if min < 60:
    sec = sec - (min * 60)
    print('%.0f: %.0f: %.0f' % (00, min, sec))
else:
   hour = sec // 3600
   a = 3600 * hour
   min1 = sec-a
   min = min1 // 60
   sec = sec - a - min * 60
   print('%.0f: %.0f: %.0f' % (hour, min, sec))



