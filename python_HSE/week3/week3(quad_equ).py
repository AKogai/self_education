a, b, c = float(input()), float(input()), float(input())
D = float(b ** 2 - (4 * a * c))
x1 = ((b * -1) + D**0.5) / (2 * a)
x2 = ((b * -1) - D**0.5) / (2 * a)
if D == 0:
    print(x1)
elif D > 0:
    if x2 > x1:
        print(x1, x2)
    else:
        print(x2, x1)
