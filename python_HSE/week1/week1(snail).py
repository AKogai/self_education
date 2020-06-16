H = int(input())
A = int(input())
B = int(input())
d = A - B
n = ((H - A + (d - 1)) // d) + 1
print(n)
