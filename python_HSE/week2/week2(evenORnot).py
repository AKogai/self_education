a = int(input())
b = int(input())
c = int(input())
if ((a + b) % 2) != 0 or\
        ((c + b) % 2) != 0 or\
        ((a + c) % 2) != 0:
    print('YES')
else:
    print('NO')
