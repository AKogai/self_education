inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.read().split()
words = dict()
for word in lines:
    if word in words:
        words[word] += 1
    else:
        words[word] = 0
words = sorted(words, key=lambda x: (-words[x], x))
for word in words:
    print(word)
inFile.close()