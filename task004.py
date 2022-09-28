# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

from function import CheckInputIntNumbers


def binar_sys (number:int,list:list) -> int:
    """
    Преобразовывает десятичное число в двоичное
    """
    if number<1:
        return number
    else:
        list.append(int(int(number)%2))
        binar_sys(int(int(number)/2),list)
        return int (number)

    
number=input("Введите челое число : ")
number=CheckInputIntNumbers(number)
number=int(number)
list=[]
binar_sys(number,list)
list.reverse()
strOut=""
for i in list:
    strOut=str(strOut)+str(i)
print(f"{number} -> {strOut}")


