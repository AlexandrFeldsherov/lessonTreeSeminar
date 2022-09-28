# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

from function import CheckInputIntNumbers
from function import FibonacciSequencePlusNega

number=input("Введите челое число k : ")
number=CheckInputIntNumbers(number)
list=FibonacciSequencePlusNega(number)

print(f"для k = {number} список будет выглядеть так: {list}")
