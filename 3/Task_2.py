# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний 
# , второй и предпоследний и т.д.

from random import randint
def create_random_list(length = 10, stop=20):
    new_list = []
    for i in range(length):
        new_list.append(randint(0,stop))
    return new_list
def multiply_list_values(current_list):
    new_list= []
    for i in range(len(current_list)//2):
       new_list.append(current_list[i] * current_list[-i-1])
    if len(current_list)%2 != 0:
        new_list.append(current_list[(len(current_list)//2 )]**2)
    return new_list
length_list = randint(2,15)
limit_list = randint(2,20)
my_list = create_random_list(length_list,limit_list)
print(my_list)
print(multiply_list_values(my_list))