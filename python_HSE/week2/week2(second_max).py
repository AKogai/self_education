a = int(input())
max = a
tmp = 0
sec = 0
while a != 0:
    a = int(input())
    if a > max:
        tmp = max
        max = a
        sec = tmp
    elif a > sec and a <= max:
        sec = a
print(sec)
