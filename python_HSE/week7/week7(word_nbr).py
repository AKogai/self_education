inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.read().split()
words = dict()
for word in lines:
    if word in words:
        print(words[word] + 1, end=' ')
        words[word] += 1
    else:
        print(0, end=' ')
        words[word] = 0
inFile.close()
