# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.
def powers (list,power):
    new_list = []
    for elem in list:
        new_list.append(elem**power)
    print(' '.join([str(i) for i in new_list]))
list = [int(s) for s in input().split()]
power = int(input())
powers(list,power)

