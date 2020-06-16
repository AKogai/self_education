a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if a <= d and c <= e or c <= d and a <= e:
    print('YES')
elif a <= d and b <= e or b <= d and a <= e:
    print('YES')
elif b <= d and c <= e or c <= d and b <= e:
    print('YES')
else:
    print('NO')
