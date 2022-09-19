# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

def find_simple_multipliers(number):
    new_list = []
    for i in range(2, number + 1):
        while number % i == 0:
            new_list.append(i)
            number /= i
    return new_list


my_num = int(input("Введите число "))
print("Число ", my_num, "состоит из множителей ", find_simple_multipliers(my_num))
