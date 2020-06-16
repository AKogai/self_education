s = input()
a, c = s.find('h'), s.rfind('h')
b, d = s[0:a], s[c + 1:]
print(b + d)
