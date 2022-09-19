# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# ЗАДАчА НЕ РЕШЕНА . БУДЕТ РЕШЕНА в течение 19.09 -20.09 !!!





from asyncore import read


def get_monomial(line):
    tmp = []
    last = 0
    positive = True
    for i, item in enumerate(line):
        if item in {"+", "-"}:
            if positive:
                tmp.append(line[last:i])
            else:
                tmp.append("-" + line[last:i])
            last = i+1
            positive = item == "+"
    if positive:
        tmp.append(line[last:])
    else:
        tmp.append("-" + line[last:])
    return tmp


def get_coef(monomial):
    for i, item in enumerate(monomial):
        if item == "x":
            return [int(monomial[:i]), monomial [i:]]

def sum_of_polynomial(first_list, second_list):
    for i in range(len(first_list)):
        for j in range(len(second_list)):
            if first_list[i][1] == second_list[j][1]:
                first_list[i][0] = int(first_list[i][0]) + int(second_list[j][0])
    return first_list

def uniform_polynomial(current_list):
    new_string = ""
    for i in range(len(current_list)-1):
        new_string += str(current_list[i][0]) + str(current_list[i][1]) + " + "
    new_string = new_string[:-2]
    return new_string

file1 = open("file_1.txt","r")
file2 = open("file_2.txt","r")

data_1 = file1.readline()
data_2 = file2.readline()
lst_1 = get_monomial(data_1.replace(" ", "").replace("*", ''))
lst_2 = get_monomial(data_2.replace(" ", "").replace("*", ''))
file1.close()
file2.close()
tmp_1 = map(get_coef, lst_1)
tmp_2 = map(get_coef, lst_2)
list_coef_1 = [*tmp_1]
list_coef_1.append(lst_1[len(lst_1)-1])
list_coef_2 = [*tmp_2]
list_coef_2.append(lst_2[len(lst_2)-1])
file3 = open("file_3.txt","w")
file3.write(uniform_polynomial(sum_of_polynomial(list_coef_1, list_coef_2)))
file3.close()
print(uniform_polynomial(sum_of_polynomial(list_coef_1, list_coef_2)))
