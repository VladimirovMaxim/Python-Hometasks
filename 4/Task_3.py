#  Задайте последовательность чисел. Напишите программу, которая выведет
#  список неповторяющихся элементов исходной последовательности.

from random import randint


def create_random_list(length=10, stop=20):
    new_list = []
    for i in range(length):
        new_list.append(randint(0,stop))
    return new_list


def find_unique_values(current_list):
    new_list = []
    for i in range(len(current_list)):
        repeat = 0
        for j in range(len(current_list)):
            if current_list[i] == current_list[j]:
                repeat += 1
        if repeat == 1:
            new_list.append(current_list[i])
    return new_list


my_list = create_random_list()
print("Ваш список: ", my_list)
print("Ваш отредактированный список: ", find_unique_values(my_list))
