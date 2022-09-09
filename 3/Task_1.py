# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
from random import randint
def create_random_list(length = 10, stop=20):
    new_list = []
    for i in range(length):
        new_list.append(randint(0,stop))
    return new_list
def odd_index_sum (current_list):
    result_sum = 0
    for i in range(len(current_list)):
        if i % 2 !=0 :
            result_sum+=current_list[i]
    return result_sum

length_list = randint(1,10)
limit_list = randint(3,30)
my_list = create_random_list(length_list,limit_list)
print(my_list)
print(odd_index_sum(my_list))

