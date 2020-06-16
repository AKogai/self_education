a = int
i = 1
k = 0
prev = 0
while a != 0:
    a = int(input())
    if a != prev:
        prev = a
        if i > k:
            k = i
        i = 1
    elif a == prev:
        i += 1
print(k)
