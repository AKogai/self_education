n = int(input())
n1 = [int(a) for a in input().split()]
m = int(input())
m1 = [int(a) for a in input().split()]
i = 0
n2, m2 = [], []
while i < len(n1):
    n2.append((n1[i], i))
    i += 1
i = 0
while i < len(m1):
    m2.append((m1[i], i))
    i += 1
n2.sort()
m2.sort()
fin = n1[:]
i, k = 0, 0
while i < len(n2):
    tmp_dest = abs(n2[i][0] - m2[k][0])
    fin[i] = n2[i][1], m2[k][1]
    while k < len(m2):
        if abs(n2[i][0] - m2[k][0]) <= tmp_dest:
            fin[i] = n2[i][1], m2[k][1] + 1
            tmp_dest = abs(n2[i][0] - m2[k][0])
            c = k
            if abs(n2[i][0] - m2[k][0]) == 0:
                break
            if k != len(m2) - 1:
                if abs(n2[i][0] - m2[k + 1][0]) > tmp_dest:
                    break
        k += 1
    k = c
    i += 1
fin.sort()
d = 0
while d < len(fin):
    print(fin[d][1], end=' ')
    d += 1
