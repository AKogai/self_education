# Дан список из N (N≤2*10⁵) элементов, которые принимают
# целые значения от 0 до 100 (100 включая). Отсортируйте
# этот список в порядке неубывания элементов. Выведите
# полученный список. Решение оформите в виде функции
# CountSort(A), которая модифицирует передаваемый ей
# список. Использовать встроенные функции сортировки
# нельзя.


def CountSort(A):
    cntMarks = [0] * 101
    for mark in A:
        cntMarks[mark] += 1
    i, x = 0, 0
    A = []
    for x in range(101):
        for i in range(cntMarks[x]):
            A.append(x)
    return A

A = [int(a) for a in input().split()]
print(*CountSort(A))
