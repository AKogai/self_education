import sys


a = sys.argv[1]
c = 0
for d in range(len(a)):
    c += int(a[d])
print(c)
