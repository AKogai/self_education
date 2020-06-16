sY = int(input())
sX = int(input())
fY = int(input())
fX = int(input())
if (sY + sX) % 2 == 0 and (fY + fX) % 2 == 0:
    print('YES')
elif (sY + sX) % 2 != 0 and (fY + fX) % 2 != 0:
    print('YES')
else:
    print('NO')
