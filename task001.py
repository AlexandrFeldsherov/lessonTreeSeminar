# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
#  списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from pickle import APPEND
from random import random
from re import I
import function


list=function.CreatingListInt()
oddList=[]
j=0
sum=0
for i in list:
    if j!=0:
        if (j%2!=0):
            oddList.append(i)
            sum=sum+i
    j=j+1
     
print(f"{list} -> на нечётных позициях элементы {oddList}, ответ: {sum}")
