# 2* Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# version 1

print("x -      y -      z -¬(X ⋁ Y ⋁ Z) - ¬X ⋀ ¬Y ⋀ ¬Z")
for x in False,True:
    for y in False,True:
        for z in False,True:
            print(x,"-", y, "-", z,"-", not(x or y or z),"-       " ,not x and not y and not z )


# version 2.

# print("x - y -z -¬(X ⋁ Y ⋁ Z) - ¬X ⋀ ¬Y ⋀ ¬Z")
# a = 0
# b = 1
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             if not(x or y or z) == True :
#                 first_part= 1
#             else: 
#                 first_part = 0
#             if not x and not y and not z == True:
#                 second_part = 1
#             else:
#                  second_part = 0 
#             print(x,"-", y, "-", z,"-     ", first_part,"    -      " ,second_part  )
