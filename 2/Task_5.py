# Задание 5 Реализуйте алгоритм перемешивания списка.

import random

import random
def create_list (length):
    new_list= []
    for i in range(length):
        new_list.append(input("Введите элемент списка "))
    return new_list
def mix_list ( first_list):
    second_list = []
    index_list = []
    for i in range(len(first_list)):
        index_list.append(random.randint(0,len(first_list)-1))
       
    for i in range(len(index_list)):
        for j in range(i+1, len(index_list)):
           if index_list[i] == index_list[j]:
                k = 0
                while k < len(index_list):
                    if index_list[k] == index_list[j] and k != j:
                        index_list[j] = random.randint(0,len(first_list))
                        k = 0
                    else:
                        k+=1
           
    for i in range(len(first_list)):
        second_list.append(first_list[index_list[i]])
    return second_list

length = int(input("Введите длинну списка "))    
my_list = create_list (length)
print(my_list)
print(mix_list(my_list))
