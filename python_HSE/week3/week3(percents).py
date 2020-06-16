P, X, Y = float(input()), float(input()), float(input())
tmp = int
tmp = (X * 100 + Y)
tmp = tmp + tmp * (P / 100)
Z = tmp
tmp = int(tmp % 100)
X = int((Z - tmp) // 100)
print(X, tmp)
