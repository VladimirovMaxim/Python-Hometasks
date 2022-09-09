# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

from random import randint, random
def create_random_float_list(length = 10, stop=20):
    new_list = []
    for i in range(length):
        new_list.append(float(randint(0,stop)) + round(random(),2))
    return new_list
def fractional_part_difference(current_list):
    new_list = []
    for i in range(len(current_list)):
        new_list.append(round(current_list[i]%1, 2))
    max_value = 0
    min_value = 1
    for i in new_list:
        if i > max_value:
            max_value = i
        if i< min_value:
            min_value = i
    return  round(max_value - min_value, 2)
length_list = randint(2,20)
limit_list = randint(1,20)  
my_list = create_random_float_list(length_list,limit_list)
print(my_list)
print(fractional_part_difference(my_list))