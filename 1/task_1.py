# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.

day_number = input("Введите день недели цифрой: ")
work_days = "1","2","3","4","5"
weekend = "6", "7"
if day_number in work_days:
    print("НЕТ")
elif day_number in weekend:
    print("ДА,это выходной! ")
else:
    print("Вы ввели некорректный символ")