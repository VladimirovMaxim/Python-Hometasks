# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# Пример

# -Для "abababb" и "aba" -> 2

my_str1 = input("Введите строку ")
my_str2 = input("Введите строку ")

if len(my_str2) > len(my_str1):
    temp = my_str1
    my_str1 = my_str2
    my_str2= temp
length = len(my_str2)
count = 0
for i in range(len(my_str1)):
    if my_str2 == my_str1[i:i+length]:
      count+=1
print ( count )