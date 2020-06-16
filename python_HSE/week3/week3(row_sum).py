n = float(input())
i = float(1)
sum = float(1 / i**2)
while i < n:
    i += 1
    sum = sum + (1 / i**2)
print(sum)
