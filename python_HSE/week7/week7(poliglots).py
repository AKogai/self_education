n = int(input())
lang = []
fin_sp, all_lang = set(), set()
for i in range(n):
    all_sp = set()
    k = int(input())
    for t in range(k):
        lang.append(input())
        all_sp.add(lang[-1])
        all_lang.add((lang[-1]))
    if i == 0:
        fin_sp = all_sp
    else:
        fin_sp &= all_sp
print(len(fin_sp))
print(*fin_sp, sep='\n')
print(len(all_lang))
print(*all_lang, sep='\n')
