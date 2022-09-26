#Семинар 3
# Задание 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

# старое решение

# from random import randint
# def create_random_list(length = 10, stop=20):
#     new_list = []
#     for i in range(length):
#         new_list.append(randint(0,stop))
#     return new_list
# def odd_index_sum (current_list):
#     result_sum = 0
#     for i in range(len(current_list)):
#         if i % 2 !=0 :
#             result_sum+=current_list[i]
#     return result_sum

# length_list = randint(1,10)
# limit_list = randint(3,30)
# my_list = create_random_list(length_list,limit_list)
# print(my_list)
# print(odd_index_sum(my_list))

#новое решение

from random import randint
length  = int(input("Введите длинну массива "))
random_list= [randint(0,5)for _ in range(length) ]  # list comprehension  
print(random_list)
print("Сумма равна ", sum([  x for i , x in enumerate(random_list)  if i % 2 == 1]))   #list comrehension and enumearate

