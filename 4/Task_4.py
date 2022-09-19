# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

from random import randint


def create_random_polynomial(degree):
    polynomial_string = "= 0"
    for i in range(degree+1):
        if i == 0 :
            polynomial_string = str(randint(0, 100))  + " " + polynomial_string
        elif i == 1:
            polynomial_string = str(randint(0, 100)) + "x" + " + " + polynomial_string
        else:
            polynomial_string = str(randint(0, 100)) + "x^" + str(i) + " + " + polynomial_string
    return polynomial_string


k = int(input("Введите предельную степень многочлена "))

file = open("file.txt", "a")
file.write(f"\n Polynomial with {k} degree : " + create_random_polynomial(k))
file.close()

print(create_random_polynomial(k))
