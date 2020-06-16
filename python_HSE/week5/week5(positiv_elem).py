# Найдите количество положительных элементов в данном списке.


n = list(input().split())
i, k = 0, 0
while i <= len(n) - 1:
    if int(n[i]) > 0:
        k += 1
    i += 1
print(k)
