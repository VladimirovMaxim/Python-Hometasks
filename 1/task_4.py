# 4 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
quarters = input("Введите четверть ")
 
if quarters =="1" or quarters =="I":
    print("Значение х находится от нуля до бесконечности, знчаение y нахолится от нуля до бесконечности")
elif quarters =="2"  or quarters =="II":
     print("Значение х находится от нуля до  минус бесконечности, знчаение y нахолится от нуля до бесконечности")
elif quarters =="3" or quarters =="III":
    print("Значение х находится от нуля до минус бесконечности, знчаение y нахолится от нуля до  минус бесконечности")
elif quarters =="4"  or quarters =="IV":
    print("Значение х находится от нуля до бесконечности, знчаение y нахолится от нуля до  минус 4бесконечности")
else:
    print( "Неверно указана четверть")