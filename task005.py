# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

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
    return newList


def ProductPairs(list, j, i, newList: list):
    while j >= 0:
        a = list[i]*list[j]
        newList.append(a)
        j = j-1
        i = i+1
    return newList


list = [2, 3, 4, 5, 6]
newListResult = ProductPairsListNumbers(list)
print(f"{list} => {newListResult}")
