inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.read()
lines = lines.split()
end = set(lines)
print(len(end))
