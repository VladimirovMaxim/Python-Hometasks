# Подумайте как наделить бота ""интеллектом"".

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
        print("Вы победили!")
        break
    smart_choise= sweets%29
    if smart_choise ==0:
        smart_choise = 1
    sweets-= smart_choise
    print (f"Бот забрал { smart_choise} конфет ")
    if sweets<= 0 :
        print("Победил бот!")
        break