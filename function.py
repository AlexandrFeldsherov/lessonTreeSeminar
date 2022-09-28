from pickle import APPEND
import function
from random import random
import time
import math


def CheckInputIntNumbers(a):
    index = True
    while index:
        try:
            number = int(a)
            index = False
        except ValueError:
            print("Это не целое число.")
            a = input("Введите число :")
    return a


def SumNumberInputInt(num):
    sumNumber = 0
    num = str(num)
    for i in num:
        if i != '.' and i != '-' and i != ',':
            sumNumber = sumNumber + int(i)
    return sumNumber


def Factorial(number):
    if number > 1:
        number = number*Factorial(number-1)
    return number


def ReversNumber(num):
    num = str(num)
    listNum = []
    for i in num:
        listNum.append(i)
    revListNum = listNum
    revListNum.reverse()
    return int(''.join(map(str, revListNum)))


def RandomNumberInt(a, x) -> int:
    randDelta = x-a
    count = 0
    while randDelta > 1:
        randDelta = randDelta/10
        count = count+1
    randArray = []
    i = 0
    while i < count:
        j = 10000
        while j > 0:
            j = j-1
            numberRandom = RND()
        randArray.append(numberRandom)
        i = i+1
    rand = int(''.join(map(str, randArray)))
    rand = float(rand/(10**count))
    rand = int((x-a)*rand)
    return a+rand


def RND():
    rnd = int(time.time_ns()/100 % 10)
    return rnd


def CreatingListInt() -> list:
    """
    Создает список INT случайных чисел с запросом размера
    #Есть проверка ввода размера
    """

    size = (input("Введите размер списка: "))
    size = int(CheckInputIntNumbers(size))
    list = []
    j = 0
    while j < size:
        i = RandomNumberInt(1, 10)
        list.append(i)
        j = j+1
    return list


"""
Если искать не повторяющиеся элементы и находить их сумму

j=0
sum=0
for i in list:
    if (j%2==0):
        oddList.add(i)
    j=j+1
for i in oddList:
    sum=sum+i
     
print(f"{list} -> на нечётных позициях элементы {oddList}, ответ: {sum}")
"""


def ProductPairsListNumbers(list: list) -> list:
    """
    Произведение пар чисел списка, первого и последнего, второго и предпоследнего и тд.
    """
    newList = []
    if len(list) % 2 == 0:
        i = int(len(list)/2)-1
        j = i
        # j уменьшение, i увеличение
        newList = ProductPairs(list, j, i, newList)
    else:
        i = int(round(len(list)/2))
        j = i
        newList = ProductPairs(list, j, i, newList)
    newList.reverse()
    return newList


def ProductPairs(list, j, i, newList: list):
    while j >= 0:
        a = list[i]*list[j]
        newList.append(a)
        j = j-1
        i = i+1
    return newList

def DifferenceFractionalPartListElement (list:list) -> float:
    """
Разница между
максимальным и минимальным значением дробной части элементов
    """
    listResult = []
    for i in list:
        listFractional = math.modf(i)
        listResult.append(listFractional[0])
    max = listResult[0]
    min = listResult[1]
    if max < min:
        a = max
        max = min
        min = a
    for i in listResult:
        if max < i:
            max = i
        elif min > i:
            min = i
    return max-min

    import math
def DifferenceMAxMinElement (listResult:list) -> int:
    """
Разница между
максимальным и минимальным значением list int
    """
    max = listResult[0]
    min = listResult[1]
    if max < min:
        a = max
        max = min
        min = a
    for i in listResult:
        if max < i:
            max = i
        elif min > i:
            min = i
    return max-min
def DifferenceFractionalPartListElement (list:list) -> int:

    """
Разницу между
максимальным и минимальным значением дробной части элементов в виде int
    """
    listResult=[]
    for i in list:
        i=str(i)
        a= i.split(".")

        listResult.append(("0."+a[1]))
    for i in listResult:
        a=0
        if a<len(i):
            a=len(i) 
    j=10**(a-2)
    k=0
    listResultNew=[]
    for i in listResult:
        i=round(float(i)*j)
        listResultNew.append(i)
    conclusion=DifferenceMAxMinElement(listResultNew)
    return conclusion

def FibonacciSequence(number:int,list:list) -> list:
    
    """
    Cписок чисел Фибоначчи,  для "+" индексов
    """
    i=1
    num=1
    list=[0]
    while (i<=number):
        list.append(num)
        num=num+list[i-1]
        i+=1
    return list

def NegaFibonacciSequence(number:int,list:list) -> list:
    """
    Cписок чисел Фибоначчи,  для "-" индексов
    """
    listSecond=[]
    i=1
    while (i<=number):
        negaNum=(-1)**(i+1)*list[i]
        listSecond.append(negaNum)
        i+=1
    listSecond.reverse()
    return listSecond
    
def FibonacciSequencePlusNega(number:int) ->list:
    """
    список чисел Фибоначчи, в том числе для отрицательных индексов
    """
    number=int(number)
    list=[]
    list = FibonacciSequence(number,list)
    secondList=NegaFibonacciSequence(number,list)
    return secondList+list

