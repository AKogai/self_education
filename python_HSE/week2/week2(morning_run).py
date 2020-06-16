x, y = float(input()), float(input())
i = 1
while x < y:
    x = x + (x / 10)
    i += 1
print(i)
