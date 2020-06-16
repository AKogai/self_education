n = int(input())
clist = set()
temp_set = set()
res_set = set()
i = 1
for i in range(1, n + 1):
    clist.add(i)
res_set = clist
while True:
    temp = list(map(str, input().split()))
    if temp[0] == 'HELP':
        print(*(sorted(res_set)))
        break
    else:
        if temp[0] == 'YES':
            res_set &= temp_set
            temp_set = set()
        elif temp[0] == 'NO':
            res_set -= temp_set
            temp_set = set()
        else:
            k = 1
            for k in temp:
                temp_set.add(int(k))
