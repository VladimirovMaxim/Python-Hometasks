# Семинар 3
# задание 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний 
# , второй и предпоследний и т.д.

## Старая версия

# from random import randint
# def create_random_list(length = 10, stop=20):
#     new_list = []
#     for i in range(length):
#         new_list.append(randint(0,stop))
#     return new_list
# def multiply_list_values(current_list):
#     new_list= []
#     for i in range(len(current_list)//2):
#        new_list.append(current_list[i] * current_list[-i-1])
#     if len(current_list)%2 != 0:
#         new_list.append(current_list[(len(current_list)//2 )]**2)
#     return new_list
# length_list = randint(2,15)
# limit_list = randint(2,20)
# my_list = create_random_list(length_list,limit_list)
# print(my_list)
# print(multiply_list_values(my_list))

## Новая версия

from random import randint
from math import ceil
random_list= [randint(1,10)for _ in range(int(input("Введите длинну массива "))) ]  
print("Старый список : ", random_list)
reversed_lst=random_list.copy()
random_list.reverse()
multiply_list = [*map(lambda x, y:   x *  y, random_list, reversed_lst)]
print("Новый список :", multiply_list[0:ceil(len(multiply_list)/2)])

