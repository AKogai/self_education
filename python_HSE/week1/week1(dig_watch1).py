N = int(input())
a = ((N // 60) % 24)
b = ((N % 1440) % 60)
print(a, b)
