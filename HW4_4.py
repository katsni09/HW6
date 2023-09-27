# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.
def removed_elements(list, number_to_remove):
    count = 0
    for i in list:
        if i == number_to_remove:
            count +=1
    print(count)
list = input()
number_to_remove = input()
removed_elements(list, number_to_remove)


# list = input()
# number_to_remove = input()
# quantity = list.count(number_to_remove)
# for i in range(quantity):
#     index = list.find(number_to_remove)
#     list = list[:index] + list[index + 1:]
# print(list)
# print(quantity)

