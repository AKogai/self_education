# Выведите все четные элементы списка.


n = list(input().split())
i = 0
while i <= len(n) - 1:
    if int(n[i]) % 2 == 0:
        print(n[i], end=' ')
    i += 1
