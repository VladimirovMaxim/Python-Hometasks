# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
       
        return fibonacci(num-1) + fibonacci(num-2)
def fibonacci_list(num):
    new_list = []
    for i in range(num, 1 , -1):
        if i % 2 == 0:
            new_list.append(-(fibonacci(i)))
        else :
            new_list.append(fibonacci(i))
    new_list.append(1)
    new_list.append(0)
    for i in range(1,num+1):
         new_list.append(fibonacci(i))
    return new_list  
number = int(input("Введите число "))    
print(fibonacci(number))    
print(fibonacci_list(number))
