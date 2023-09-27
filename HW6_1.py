# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
def calculation(list):
    product = 1
    for element in list:
        product *= element
    return product

number_list = [int(s) for s in input().split()]
result = calculation(number_list)
print(result)