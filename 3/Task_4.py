# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def convert_to_binar(number):
    i =1
    bin_number = 0
    while number!=0:
        if number % 2 != 0:
            bin_number+= i
        i*=10
        number//=2
    return str(bin_number)
my_number= int(input("Введите число "))
print(convert_to_binar(my_number))