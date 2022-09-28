# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

    
from function import DifferenceFractionalPartListElement


list = [4.07, 5.1, 8.2444, 6.98]
dif= DifferenceFractionalPartListElement(list)
print(f"{list} => 0.{dif} или {dif}")