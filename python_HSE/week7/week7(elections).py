inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
i = 0
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
cand = dict()
for candidate in lines:
    cand[candidate.rstrip()] = 0
for i in range(len(lines)):
    if lines[i] in cand:
        cand[lines[i]] += 1
temp = sorted(cand, key=lambda x: (-cand[x], x))
if cand[temp[0]] > len(lines) / 2:
    print(temp[0], file=outFile)
else:
    print(temp[0], file=outFile)
    print(temp[1], file=outFile)
inFile.close()
outFile.close()
