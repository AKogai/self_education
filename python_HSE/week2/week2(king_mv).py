sY = int(input())
sX = int(input())
fY = int(input())
fX = int(input())
if sY == (fY + 1) or sY == (fY - 1) or sY == fY:
    if sX == (fX + 1) or sX == (fX - 1) or sX == fX:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
