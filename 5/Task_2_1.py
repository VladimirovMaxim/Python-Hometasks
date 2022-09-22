sweets = 2021
first_player = True
while True:
    if first_player:
        username = "Первый игрок "
    else:
        username = "Второй игрок "
    print (f"Количество конфет {sweets}")
    number = input(f"{username} заберите от 1 до 28 конфет ")
    if not(0<int(number)<29):
        print("Вы забрали неверное количесвто конфет или ввели неправильный символ ")
        break
    sweets -=int(number)
    if sweets<= 0 :
        print(f"{username} победил!")
        break
    first_player = not first_player