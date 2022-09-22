from random import randint
sweets = 2021
while True:
    print (f"Количество конфет {sweets}")
    number = input( "Заберите от 1 до 28 конфет ")
    if not(0<int(number)<29):
        print("Вы забрали неверное количесвто конфет или ввели неправильный символ ")
        break
    sweets -=int(number)
    print (f"Количество конфет {sweets}")
    if sweets<= 0 :
        print("Вы победил!")
        break
    random_number = randint(1,28)
    sweets-= random_number
    print (f"Бот забрал {random_number} конфет ")
    if sweets<= 0 :
        print("Победил бот!")
        break