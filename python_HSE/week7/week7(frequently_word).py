inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.read().split()
words = dict()
for word in lines:
    if word in words:
        words[word] += 1
    else:
        words[word] = 0
print(max(sorted(words.keys()), key=lambda x: words[x]))
inFile.close()