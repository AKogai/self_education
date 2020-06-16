n = int(input())
words = dict()
for i in range(n):
    line = list(map(str, input().split()))
    words[line[0]] = line[1]
    words[line[1]] = line[0]
key_f = input()
print(words[key_f])
