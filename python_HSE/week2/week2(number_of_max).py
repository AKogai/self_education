a = int
max = 0
i = 0
while a != 0:
    a = int(input())
    if a > max:
        max = a
        i = 1
    elif a == max:
        i += 1
print(i)
