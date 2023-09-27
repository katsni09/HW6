# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
from math import *
def calculate_numbers(list):
    count = 0
    p = 0
    for number in list:
        flag = True
        for number2 in range (2, 1 + int(sqrt(number))):
            if number % number2 != 0:
                flag = False
                break
        if flag:
            count+=1
    print (count)
list_of_new_numbers = [int(s) for s in input().split()]
calculate_numbers(list_of_new_numbers)