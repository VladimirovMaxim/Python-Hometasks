# Создайте программу для игры в ""Крестики-нолики"".

line1 = " |___|___|___|"  # номера индексов для символа3,7,11
line2, line3 = line1, line1
print(" _____________")
print(line1)
print(line2)
print(line3)
first_player = True
win_line1 = " |_x_|_x_|_x_|" 
win_line2= " |_o_|_o_|_o_|"
while True:
    if first_player == True:
        char = "x"
        phrase = "Первый игрок "
    else:
        char ="o"
        phrase = "Второй игрок "
    string = input (f"{phrase}введите номер строки ")
    row = int(input (f"{phrase}введите номер столбца "))
    if row == 1:
        position_in_string = 3
    elif row == 2:  
        position_in_string = 7
    elif row == 3:  
        position_in_string = 11
    else:
        print("Вы ввели непраивльный номер столбца ")
        break
    print(string)
    if string == "1":
        line1 = line1[:position_in_string] + char + line1[position_in_string+1:]
    elif string == "2":
        line2 = line2[:position_in_string] + char + line2[position_in_string+1:]
    elif string == "3":
        line3 = line3[:position_in_string] + char + line3[position_in_string+1:]
    else:
        print("Вы ввели непраивльный номер строки ")
        break
    print(" _____________")
    print(line1)
    print(line2)
    print(line3)
    if (line1 == win_line1 or line2 == win_line1 or line3 == win_line1 or
            line1 == win_line2 or line2 == win_line2 or line3 == win_line2
            or (line1[position_in_string] == char
            and line2[position_in_string] == char
            and line3[position_in_string] == char)
            or (line1[3] == char and line2[7] == char and line3[11] == char)
            or (line1[11] == char and line2[7] == char and line3[3] == char)):
        print(f"{phrase} победил!")
        break
    first_player = not first_player