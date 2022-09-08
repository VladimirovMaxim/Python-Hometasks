# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11

import math

def find_fractional_part(float_number):
    for i in range(len(float_number)):
        if float_number[i] == ".":
            fractional_part = float_number[i+1:len(float_number)]
    return fractional_part
   
def sum_of_digit(str_number):
    number = float(str_number)
    number = int(number)
    digit_sum = 0
    while number != 0:
        digit_sum= digit_sum + number%10
        number = number //10
    return digit_sum
num = input("Введите число ")
first_sum = sum_of_digit(num)
if float(num) != int(float(num)):
    fractional_part = find_fractional_part(num)
    second_sum = sum_of_digit( fractional_part)
    print("Сумма всех цифр равна", first_sum+second_sum)
else :
    print("Сумма всех цифр равна", first_sum)

