# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
def calculate_min_nr(list):
    min_elem = list[0]
    for elem in list:
        if elem < min_elem:
            min_elem = elem
    return min_elem
number_list = [int(s) for s in input().split()]
print(calculate_min_nr(number_list))
