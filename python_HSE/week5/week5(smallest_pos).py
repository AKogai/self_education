# Выведите значение наименьшего из всех
# положительных элементов в списке.
# Известно, что в списке есть хотя бы
# один положительный элемент, а значения
# всех элементов списка по модулю не
# превосходят 1000.


n = list(input().split())
i = 0
k = n[0]
t = n[0]
while i <= len(n) - 1:
    if int(n[i]) > 0:
        t = n[i]
        break
    i += 1
i = 0
while i <= len(n) - 1:
    if 0 < int(n[i]) < int(t):
        t = n[i]
    i += 1
print(t)
