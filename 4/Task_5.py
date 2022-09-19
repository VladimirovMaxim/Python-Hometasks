# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# ЗАДАЯА НЕ РЕШЕНА . БУДЕТ РЕШЕНА в течение 19.09 -20.09 !!!


# file1 = "40x^7 + 26x^6 + 62x^5 + 79x^4 + 57x^3 + 90x^2 + 80x + 75"
# file2 = "15x^3 + 70x^2 + 94x + 24 "
#
#
# def get_monomial(line):
#     tmp = []
#     last = 0
#     positive = True
#     for i, item in enumerate(line):
#         if item in {"+", "-"}:
#             if positive:
#                 tmp.append(line[last:i])
#             else:
#                 tmp.append("-" + line[last:i])
#             last = i+1
#             positive = item == "+"
#     if positive:
#         tmp.append(line[last:])
#     else:
#         tmp.append("-" + line[last:])
#     return tmp
#
#
# def get_coef(monomial):
#     for i, item in enumerate(monomial):
#         if item == "x":
#             return int(monomial[:i], monomial [:i])
#
#
# lst = get_monomial(file1.replace(" ", ""), file2.replace(" ", ''))
# tmp = map(get_coef, lst)
# print(tmp)
