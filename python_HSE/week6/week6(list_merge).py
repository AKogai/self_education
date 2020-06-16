# Даны два целочисленных списка A и B,
# упорядоченных по неубыванию. Объедините
# их в один упорядоченный список С
# (то есть он должен содержать len(A)+len(B)
# элементов). Решение оформите в виде функции
# merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность
# O(len(A)+len(B)). Модифицировать исходные
# списки запрещается. Использовать функцию
# sorted и метод sort запрещается.


def merge(a, b):
    if len(a) < len(b):
        a, b = b, a
    i = 0
    j = 0
    newList = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            newList.append(a[i])
            i += 1
        elif a[i] >= b[j]:
            newList.append(b[j])
            j += 1
    if i == len(a):
        while j < len(b):
            newList.append(b[j])
            j += 1
    else:
        while i < len(a):
            newList.append(a[i])
            i += 1
    return (newList)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
merge(a, b)
print(*merge(a, b))
