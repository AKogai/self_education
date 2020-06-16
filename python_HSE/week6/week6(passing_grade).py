inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
people_list = []
c = []
for line in lines:
    people_list.append(line.split())
k = int(people_list[0][0])
people_list = people_list[1:]
for nline in people_list:
    if int(nline[-1]) >= 40 and int(nline[-2]) >= 40 and int(nline[-3]) >= 40:
        c.append(int(nline[-1]) + int(nline[-2]) + int(nline[-3]))
c.sort(reverse=True)
n = len(c)


def konkurs(n, k, c):
    if n <= k:
        return 0
    elif c[k] == c[0]:
        return 1
    for i in range(k, 0, -1):
        if c[i] < c[i - 1]:
            return c[i - 1]

print(konkurs(n, k, c), file=outFile)


inFile.close()
outFile.close()
