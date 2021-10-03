''' Задание 1.
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об  окончании
ввода данных свидетельствует пустая строка.
'''

my_f = open("my_file.txt", "w")
line = input('Введите текст \n')

while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()

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

''' Задание 3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк)
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''

with open('salary.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

''' Задание 4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

my_dict = dict(One='Один', Two='Два', Three='Три', Four='Четыре')
result = []
with open('fugure.txt', 'r', encoding='UTF-8-sig') as file_obj:
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in my_dict:
            word = my_dict[tokens[0]]
            result.append(word + ' - ' + tokens[1])
    print(result)
with open('new_fugure.txt', 'w', encoding='UTF-8-sig') as file_obj_2:
    file_obj_2.writelines(result)

''' Задание 5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
'''
line = input("введите числа через пробел")
with open("my_file5.txt", "w") as my_f:
    my_f.write(line)
    num = line.split()
    int_lst = [int(x) for x in num]
print(sum(int_lst))

''' Задание 6
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
with open('subjects.txt', 'r', encoding='UTF-8-sig') as init_f:
    for line in init_f:
        num = line.split()
        subject = num[0]
        hours = 0
        for r, i in enumerate(num):
            x = num[r].split("(")
            if len(x) > 1:
                #print(x[0])
                hours += int(x[0])
                #subj[subject] = rrr + ccc + int(lab)
        print(f'Общее количество часов по предмету {subject} составляет {hours} часов')

''' Задание 7
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила 
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
'''
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('company.txt', 'r', encoding='UTF-8-sig') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w', encoding='UTF-8-sig') as write_js:
    json.dump(profit, write_js,  ensure_ascii=False)

    js_str = json.dumps(profit, ensure_ascii=False)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')